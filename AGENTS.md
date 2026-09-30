# Go 101 Vietnamese Translation Rules

Tài liệu này là hướng dẫn bắt buộc cho người và AI agent dịch Go 101 sang tiếng Việt. Đọc tài liệu này, `translations/vi/TRANSLATION_STYLE.md`, `translations/vi/GLOSSARY.md` và `translations/vi/PROGRESS.md` trước khi dịch hoặc thay đổi tooling dịch.

## 1. Source of truth

- Trang nguồn tiếng Anh hiện hành từ `go101/go101:master` là source of truth. Trong repo fork, các file nguồn thường nằm tại `pages/`.
- Không dịch từ trí nhớ, bản dịch trên Internet, phiên bản Go 101 cũ, hay kiến thức Go hiện tại nếu nội dung đó khác nguồn.
- Đọc toàn bộ file nguồn được giao trước khi dịch. Có thể đọc trang liên kết trước/sau chỉ để hiểu ngữ cảnh ở ranh giới, không được sao chép nội dung của trang khác vào output được giao.
- English source và ứng dụng Go 101 là upstream-owned, chỉ đọc. Bản dịch tiếng Việt nằm dưới `translations/vi/`, với cùng đường dẫn tương đối:
  - `pages/fundamentals/introduction.tmd` → `translations/vi/pages/fundamentals/introduction.tmd`
  - `pages/website/index.html` → `translations/vi/pages/website/index.html`
- Giữ nguyên English source. Không ghi đè, di chuyển, đổi tên hoặc thay thế nó bằng bản dịch.
- `translations/vi/.sync-state.json` ghi source blob SHA đã được người dịch soát. Chỉ cập nhật SHA sau khi đối chiếu bản dịch với đúng revision nguồn.

## 2. Dịch đầy đủ và trung thực

Dịch đầy đủ mọi nội dung có nghĩa trong trang nguồn:

- heading, paragraph, list và table;
- caption, note, warning, tip và phần tóm tắt;
- prose quanh code;
- chú thích code nếu đó là nội dung giải thích cho người đọc;
- visible label và alt text của ảnh, khi không phải identifier hay asset path;
- HTML/TapirMD nội dung hiển thị cho người đọc.

Không được:

- tóm tắt, bỏ câu, bỏ ví dụ hoặc thêm ví dụ;
- thêm giải thích, ghi chú của translator hay reasoning mới;
- thay đổi mức độ khuyến nghị của tác giả;
- cập nhật nội dung theo phiên bản Go mới hơn;
- sửa lỗi kỹ thuật mà agent cho là có trong nguồn;
- tái sắp xếp section chỉ để bản dịch trông dễ đọc hơn.

## 3. Technical accuracy

Technical accuracy được ưu tiên cao nhất. Khi readability mâu thuẫn với độ chính xác, giữ cách diễn đạt chính xác hơn.

- Giữ nguyên Go keyword, identifier, API/type/package name, command, flag, file path, URL, anchor, command output và configuration key.
- Nếu không chắc technical term có nên dịch, giữ English theo `translations/vi/GLOSSARY.md`.
- Nếu không chắc code hoặc output có nên sửa, giữ nguyên.
- Không dịch literal mà người đọc phải gõ hoặc code cần biên dịch/chạy.
- Nếu nguồn không đọc hay không xác định được chắc chắn, không đoán. Dùng marker tạm thời ở vị trí an toàn cho markup:

  ```html
  <!-- REVIEW: source text unclear in pages/path/file.tmd near source line N -->
  ```

  Marker phải được xử lý trước khi mark-reviewed hoặc merge.

## 4. Trang là một phần của tài liệu liên tục

Mỗi file là một phần của Go 101, không phải tài liệu độc lập. File có thể bắt đầu/kết thúc giữa ý, đoạn văn, danh sách, code listing, table, quote, HTML block hoặc TapirMD directive.

- Không tự thêm opening/closing text để làm trang trông hoàn chỉnh.
- Giữ heading hierarchy, thứ tự section và ranh giới đầu/cuối đúng như nguồn.
- Chỉ dùng trang lân cận để hiểu context tại boundary.

## 5. Ownership và chống ghi đè

- Mỗi worker chỉ tạo hoặc sửa đúng file đích đã được giao.
- Được đọc source, glossary, progress và trang lân cận khi cần context.
- Không sửa file của worker khác, `.sync-state.json`, `PROGRESS.md` hay tooling trừ khi task ghi rõ là batch review, QA repair hoặc merge.
- Khi dịch song song, mỗi task phải có source path và destination path duy nhất.
- Không commit/push từ worker trừ khi task giao rõ. Agent điều phối gom trang đã review thành batch.

## 6. Markup, code và page furniture

- `.tmd` dùng TapirMD. Giữ nguyên syntax heading, directives, fences, inline formatting, HTML block, anchor, link và image path.
- `.html` là fragment được render trong template có sẵn. Giữ nguyên cấu trúc tag, attribute, class, ID, href/src, comment điều khiển và code; không thêm `<!doctype html>`.
- Giữ nguyên bảng, danh sách, link, URL, image asset và route nội bộ. Với route nội bộ, builder sẽ trỏ sang `/vi/` nếu đã có bản dịch current; nếu chưa có thì dùng English source route.
- Không đưa vào bản dịch các thành phần layout lặp không phải nội dung thực, như running header/footer, số trang đứng riêng, crop artifact hay tiêu đề lặp chỉ để định vị. Với Go 101 source files, chỉ loại bỏ chúng khi chắc chắn đó là generated/layout-only content.

## 7. Definition of Done cho một trang

Một trang chỉ hoàn tất khi:

- đã dịch đầy đủ nội dung thuộc trang, không thêm nội dung ngoài source;
- code/API/identifier/literal và markup cần giữ nguyên;
- TapirMD/HTML hợp lệ, links, tables, list và ảnh không bị biến dạng;
- heading, section order, code fence, directive và boundary đầu/cuối đã được đối chiếu với source;
- không còn marker `REVIEW` và không còn lỗi OCR/extraction có thể xác minh;
- terminology nhất quán theo glossary trong toàn trang;
- source blob SHA đã được ghi nhận để coordinator mark-reviewed.

## 8. Required workflow

1. Đọc tài liệu rules/style/glossary/progress và toàn bộ source page.
2. Dịch vào đúng path dưới `translations/vi/pages/`.
3. Soát source với translation: prose, code comments, links, images, tables, HTML/TapirMD, heading/order/fence/directive.
4. Coordinator chạy:

   ```sh
   python3 scripts/translation_status.py
   python3 scripts/build_pages.py --check-only
   python3 scripts/translation_status.py --mark-reviewed pages/path/source.tmd
   ```

5. Cập nhật `PROGRESS.md`, glossary nếu có thuật ngữ lặp lại, và `.sync-state.json` chỉ sau bước review.
6. Khi upstream đổi source, đọc lại phần thay đổi và cập nhật bản dịch; không tự đổi SHA để làm trang thành current.

## 9. Upstream sync, Pages và license

- Upstream sync chỉ lấy `go101/go101:master` vào nhánh sync/PR; không ghi trực tiếp upstream content vào `master`.
- Sau sync, source đổi SHA sẽ được báo stale cho đến khi review lại.
- `/vi/` chứa Vietnamese landing page và các route đã dịch; English source không bị sửa. Stale/unreviewed pages không được deploy.
- Generated `_site/` không commit.
- License upstream cho phép phân phối bản dịch ngôn ngữ khác khi mỗi trang dịch hiển thị link tới `https://go101.org`, `https://www.tapirgames.com` và `https://x.com/TapirLiu`; static builder chịu trách nhiệm thêm các link này.
