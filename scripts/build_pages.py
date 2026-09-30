#!/usr/bin/env python3
"""Build Go 101's Vietnamese translation for GitHub Pages."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
from posixpath import dirname, join, normpath
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
VI_ROOT = ROOT / "translations" / "vi"
VI_PAGES = VI_ROOT / "pages"
SYNC_STATE = VI_ROOT / ".sync-state.json"
RENDERER = ROOT / "scripts" / "tmd-renderer"

URL_ATTR = re.compile(r'(?P<prefix>\b(?:href|src|action|poster|data-src)\s*=\s*)(?P<quote>["\'])(?P<url>[^"\']*)(?P=quote)', re.I)
FIRST_HEADING = re.compile(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", re.I | re.S)
TAGS = re.compile(r"<[^>]+>")
JS_STATIC_URL = re.compile(r'(?P<quote>["\'])(?P<url>/static/[^"\']*)(?P=quote)')

PAGE_STYLE = """<style>
.go101-translation-switch{position:fixed;z-index:9999;right:16px;top:12px;display:flex;gap:4px;padding:4px;border:1px solid #bbb;border-radius:999px;background:#fff;box-shadow:0 2px 10px #0002;font:14px/1.2 system-ui,sans-serif}
.go101-translation-switch a{padding:6px 10px;border-radius:999px;color:#1459a6;text-decoration:none}
.go101-translation-switch a[aria-current=page]{background:#1459a6;color:#fff}
.go101-translation-credit{margin:2rem 0 1rem;padding-top:1rem;border-top:1px solid #ddd;font-size:small}
@media print{.go101-translation-switch{display:none}}
</style>"""


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def base_path(repo: str | None, explicit: str | None) -> str:
    if explicit is not None:
        value = explicit
    elif repo and not repo.rsplit("/", 1)[-1].endswith(".github.io"):
        value = "/" + repo.rsplit("/", 1)[-1] + "/"
    else:
        value = "/"
    return "/" + value.strip("/") + "/" if value != "/" else "/"


def load_state() -> dict[str, str]:
    if not SYNC_STATE.exists():
        return {}
    data = json.loads(SYNC_STATE.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"invalid translation state: {SYNC_STATE}")
    return {str(key): str(value) for key, value in data.items()}


def route_for(relative: Path) -> str:
    group = relative.parent.name
    if group == "website":
        return "" if relative.name == "index.html" else relative.name
    prefix = "article" if group == "fundamentals" else group
    return f"{prefix}/{relative.with_suffix('.html').name}"


def current_translations(state: dict[str, str]) -> list[tuple[str, Path, Path]]:
    candidates = list(VI_PAGES.rglob("*.tmd")) if VI_PAGES.exists() else []
    if VI_PAGES.exists():
        candidates.extend(path for path in VI_PAGES.rglob("*.html") if not path.with_suffix(".tmd").exists())
    result: list[tuple[str, Path, Path]] = []
    for translated in sorted(candidates):
        relative = translated.relative_to(VI_PAGES)
        source = PAGES / relative
        if not source.is_file():
            print(f"Skipping orphan translation: {translated.relative_to(ROOT)}", file=sys.stderr)
            continue
        key = f"pages/{relative.as_posix()}"
        if state.get(key) != git_blob_sha(source):
            print(f"Skipping unreviewed or stale translation: {key}", file=sys.stderr)
            continue
        result.append((route_for(relative), source, translated))
    return result


def validate_layout() -> None:
    if not (ROOT / "go.mod").is_file() or not PAGES.is_dir() or not (ROOT / "web" / "static").is_dir():
        raise FileNotFoundError("Run this script from a complete go101 repository checkout")
    for translated in (*VI_PAGES.rglob("*.tmd"), *VI_PAGES.rglob("*.html")) if VI_PAGES.exists() else ():
        if not (PAGES / translated.relative_to(VI_PAGES)).is_file():
            print(f"Orphan translation: {translated.relative_to(ROOT)}", file=sys.stderr)


def rewrite_url(url: str, base: str, route: str, vi_routes: set[str]) -> str:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
        return url
    prefix = base.rstrip("/")
    path = parsed.path
    if prefix and (path == prefix or path.startswith(prefix + "/")):
        path = path[len(prefix):]
    route_path = path.lstrip("/")

    if not route_path or route_path == "index.html":
        destination = prefix + "/vi/" if prefix else "/vi/"
    elif route_path == "static" or route_path.startswith("static/"):
        destination = prefix + "/" + route_path if prefix else "/" + route_path
    elif route_path.startswith("vi/"):
        destination = prefix + "/" + route_path if prefix else "/" + route_path
    elif route_path in vi_routes:
        destination = prefix + "/vi/" + route_path if prefix else "/vi/" + route_path
    else:
        destination = "https://go101.org/" + route_path
    return urlunsplit((urlsplit(destination).scheme, urlsplit(destination).netloc, urlsplit(destination).path, parsed.query, parsed.fragment))


def rewrite_fragment_urls(fragment: str, base: str, route: str, vi_routes: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        raw_url = match.group("url")
        parsed = urlsplit(raw_url)
        if not parsed.scheme and not parsed.netloc and not parsed.path.startswith("/") and parsed.path.endswith(".html"):
            target = normpath(join(dirname(route), parsed.path))
            while target.startswith("../"):
                target = target[3:]
            target = "" if target == "index.html" else target
            prefix = base.rstrip("/")
            if target in vi_routes:
                destination = (prefix + "/vi/" + target) if target else (prefix + "/vi/" if prefix else "/vi/")
            else:
                destination = "https://go101.org/" + target if target else "https://go101.org/"
            url = urlunsplit((*urlsplit(destination)[:3], parsed.query, parsed.fragment))
        else:
            url = rewrite_url(raw_url, base, route, vi_routes)
        return match.group("prefix") + match.group("quote") + url + match.group("quote")

    return URL_ATTR.sub(replace, fragment)


def resource_route(group: str) -> str:
    if group == "website":
        return ""
    return "article" if group == "fundamentals" else group


def copy_page_resources(output: Path, pairs: list[tuple[str, Path, Path]]) -> None:
    groups = {source.parent.name for _, source, _ in pairs}
    for group in groups:
        resources = PAGES / group / "res"
        if resources.is_dir():
            relative = Path("vi") / resource_route(group) / "res"
            shutil.copytree(resources, output / relative, dirs_exist_ok=True)
        translated_resources = VI_PAGES / group / "res"
        if translated_resources.is_dir():
            relative = Path("vi") / resource_route(group) / "res"
            shutil.copytree(translated_resources, output / relative, dirs_exist_ok=True)


def make_document(fragment: str, route: str, base: str, vi_routes: set[str]) -> str:
    title_match = FIRST_HEADING.search(fragment)
    title = html.unescape(TAGS.sub("", title_match.group(1))).strip() if title_match else "Go 101"
    title = title or "Go 101"
    prefix = base.rstrip("/")
    english_route = "https://go101.org/" + route if route else "https://go101.org/"
    vi_route = prefix + "/vi/" + route if route else (prefix + "/vi/" if prefix else "/vi/")
    home = prefix + "/vi/" if prefix else "/vi/"
    converted = rewrite_fragment_urls(fragment, base, route, vi_routes)

    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Bản dịch tiếng Việt Go 101.">
  <link rel="icon" href="{prefix}/static/go101/images/101-v1.ico">
  <link id="css-bs" rel="stylesheet" href="{prefix}/static/bootstrap/v4.5.0/css/bootstrap.min.css">
  <link id="css-go101" rel="stylesheet" href="{prefix}/static/go101/css/v99992-light.css">
  <link id="css-prism" rel="stylesheet" href="{prefix}/static/prism/2020-08-03-light/prism.css">
  <script id="js-prism" src="{prefix}/static/prism/2020-08-03-light/prism.js"></script>
  <script>var theme = "light";</script>
  <title>{html.escape(title)} · Go 101 Tiếng Việt</title>
  {PAGE_STYLE}
</head>
<body>
  <nav class="go101-translation-switch" aria-label="Ngôn ngữ">
    <a href="{english_route}" lang="en">EN</a>
    <a href="{vi_route}" lang="vi" aria-current="page">VI</a>
  </nav>
  <div class="container">
    <div class="row nav-bar-with-borders">
      <div class="col-xs-6 col-sm-4 nav-item-active"><a href="{home}"><small>Trang chủ</small></a></div>
      <div class="col-xs-6 col-sm-4 nav-item-inactive"><a href="https://go101.org/"><small>Go 101 · English</small></a></div>
    </div>
    <main>{converted}</main>
    <footer class="go101-translation-credit">
      <p>Bản dịch tiếng Việt từ <a href="https://go101.org">Go 101</a>, do <a href="https://x.com/TapirLiu">@TapirLiu</a> viết.
      Hãy ủng hộ tác giả bằng cách chơi <a href="https://www.tapirgames.com">Tapir’s games</a>.</p>
    </footer>
  </div>
  <script src="{prefix}/static/jquery/jquery.min-v1.11.2.js"></script>
  <script src="{prefix}/static/go101/js/v992.js"></script>
</body>
</html>
'''


def make_portal(base: str) -> str:
    prefix = base.rstrip("/")
    vi = prefix + "/vi/" if prefix else "/vi/"
    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Go 101 · Chọn ngôn ngữ</title>
  {PAGE_STYLE}
</head>
<body><main class="container">
  <h1>Go 101</h1>
  <p>Chọn ngôn ngữ để đọc:</p>
  <p><a href="{vi}">Tiếng Việt</a> · <a href="https://go101.org/">English</a></p>
  <footer class="go101-translation-credit">
    <p>Bản dịch tiếng Việt từ <a href="https://go101.org">Go 101</a>, do <a href="https://x.com/TapirLiu">@TapirLiu</a> viết.
    Hãy ủng hộ tác giả bằng cách chơi <a href="https://www.tapirgames.com">Tapir’s games</a>.</p>
  </footer>
</main></body>
</html>
'''


def make_translation_placeholder(base: str) -> str:
    prefix = base.rstrip("/")
    vi = prefix + "/vi/" if prefix else "/vi/"
    return f'''<!doctype html>
<html lang="vi">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Go 101 · Tiếng Việt</title>{PAGE_STYLE}</head>
<body><main class="container">
  <h1>Go 101 · Tiếng Việt</h1>
  <p>Bản dịch trang chủ đang được cập nhật. Bạn có thể đọc bản tiếng Anh trên website chính thức.</p>
  <p><a href="https://go101.org/">Go 101 · English</a></p>
  <p><a href="{vi}">Trang chủ tiếng Việt</a></p>
  <footer class="go101-translation-credit">
    <p>Bản dịch tiếng Việt từ <a href="https://go101.org">Go 101</a>, do <a href="https://x.com/TapirLiu">@TapirLiu</a> viết.
    Hãy ủng hộ tác giả bằng cách chơi <a href="https://www.tapirgames.com">Tapir’s games</a>.</p>
  </footer>
</main></body></html>
'''


def rewrite_static_js(directory: Path, base: str) -> None:
    prefix = base.rstrip("/")
    if not prefix:
        return
    for path in directory.rglob("*.js"):
        data = path.read_text(encoding="utf-8", errors="replace")
        data = JS_STATIC_URL.sub(lambda match: f'{match.group("quote")}{prefix}{match.group("url")}{match.group("quote")}', data)
        path.write_text(data, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", help="GitHub Pages base path, e.g. /go101/; defaults from GitHub Actions")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--check-only", action="store_true", help="validate paths and source revisions without building")
    args = parser.parse_args()

    try:
        validate_layout()
        state = load_state()
        pairs = current_translations(state)
        vi_routes = {route for route, _, _ in pairs}
        if args.check_only:
            print(f"Translation paths valid; {len(pairs)} current Vietnamese page(s) ready for Pages.")
            return 0

        base = base_path(os.environ.get("GITHUB_REPOSITORY"), args.base_url)
        output = args.output.resolve()
        if output == ROOT or (ROOT in output.parents and output != ROOT / "_site"):
            raise ValueError("output must be _site/ or a directory outside the repository")
        if output.exists():
            shutil.rmtree(output)
        output.mkdir(parents=True)

        static_source = ROOT / "web" / "static"
        shutil.copytree(static_source, output / "static", dirs_exist_ok=True)
        rewrite_static_js(output / "static", base)
        copy_page_resources(output, pairs)

        with tempfile.TemporaryDirectory(prefix="go101-vi-") as temp_dir:
            temp = Path(temp_dir)
            rendered_pages = render_tmd_pages(pairs, temp)
            for route, _, translated in pairs:
                if translated.suffix == ".tmd":
                    fragment = rendered_pages[route].read_text(encoding="utf-8")
                else:
                    fragment = translated.read_text(encoding="utf-8")
                local = output / "vi" / (route or "index.html")
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_text(make_document(fragment, route, base, vi_routes), encoding="utf-8")

        if "" not in vi_routes:
            fallback = output / "vi" / "index.html"
            fallback.parent.mkdir(parents=True, exist_ok=True)
            fallback.write_text(make_translation_placeholder(base), encoding="utf-8")

        (output / "index.html").write_text(make_portal(base), encoding="utf-8")
        print(f"Built Vietnamese Go 101 site in {output}; {len(vi_routes)} page(s). English pages link to go101.org.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Build failed: {error}", file=sys.stderr)
        return 1


def render_tmd_pages(pairs: list[tuple[str, Path, Path]], temp: Path) -> dict[str, Path]:
    tmd_pairs = [(route, translated) for route, _, translated in pairs if translated.suffix == ".tmd"]
    if not tmd_pairs:
        return {}
    binary = temp / "tmd-renderer"
    subprocess.run(["go", "build", "-o", str(binary), "."], cwd=RENDERER, check=True)
    arguments: list[str] = []
    outputs: dict[str, Path] = {}
    rendered = temp / "rendered"
    rendered.mkdir(parents=True, exist_ok=True)
    for index, (route, translated) in enumerate(tmd_pairs):
        destination = rendered / f"{index}.html"
        arguments.extend((str(translated), str(destination)))
        outputs[route] = destination
    subprocess.run([str(binary), *arguments], check=True)
    return outputs


if __name__ == "__main__":
    raise SystemExit(main())
