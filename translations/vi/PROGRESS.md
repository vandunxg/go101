# Tiến độ bản dịch Go 101

## Quy tắc cập nhật

- Chọn trang theo lộ trình bên dưới; dịch đầy đủ một trang trước khi chuyển trang khác.
- Sau khi soát bản dịch với nguồn tiếng Anh, chạy `python3 scripts/translation_status.py --mark-reviewed <đường-dẫn-nguồn>`.
- Chạy `python3 scripts/translation_status.py` để xem trang còn thiếu, đã cũ hoặc không còn nguồn.
- Không tự đánh dấu bản dịch là hiện hành khi upstream cập nhật.

## Trạng thái ban đầu

- Trang giới thiệu tiếng Việt: `translations/vi/pages/website/index.html`.
- Bản dịch các sách và bài viết đang chờ bắt đầu; xem báo cáo tự động bằng `python3 scripts/translation_status.py`.

## Lộ trình dịch

1. Trang chủ và giới thiệu: `pages/website/`, `pages/fundamentals/101.tmd`, `pages/fundamentals/101-about.tmd`.
2. Go Fundamentals 101: `pages/fundamentals/` — bắt đầu từ trang chỉ mục rồi theo thứ tự liên kết trong sách.
3. Go Generics 101: `pages/generics/`.
4. Go Optimizations 101: `pages/optimizations/`.
5. Go Details & Tips 101: `pages/details-and-tips/`.
6. Hỏi đáp, lỗi, quiz, ứng dụng và thư viện, blog: `pages/q-and-a/`, `pages/bugs/`, `pages/quizzes/`, `pages/apps-and-libs/`, `pages/blog/`.

