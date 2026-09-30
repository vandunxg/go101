# Tiến độ bản dịch Go 101

## Quy tắc cập nhật

- Chọn trang theo lộ trình bên dưới; dịch đầy đủ một trang trước khi chuyển trang khác.
- Sau khi soát bản dịch với nguồn tiếng Anh, chạy `python3 scripts/translation_status.py --mark-reviewed <đường-dẫn-nguồn>`.
- Chạy `python3 scripts/translation_status.py` để xem trang còn thiếu, đã cũ hoặc không còn nguồn.
- Không tự đánh dấu bản dịch là hiện hành khi upstream cập nhật.

## Đã dịch

Đã dịch và đối chiếu cấu trúc 30 trang trong `pages/fundamentals/`. Source blob SHA của từng trang đã được ghi trong `.sync-state.json`.

- `pages/fundamentals/101.tmd`
- `pages/fundamentals/introduction.tmd`
- `pages/fundamentals/keywords-and-identifiers.tmd`
- `pages/fundamentals/basic-code-elements-introduction.tmd`
- `pages/fundamentals/packages-and-imports.tmd`
- `pages/fundamentals/go-toolchain.tmd`
- `pages/fundamentals/basic-types-and-value-literals.tmd`
- `pages/fundamentals/constants-and-variables.tmd`
- `pages/fundamentals/operators.tmd`
- `pages/fundamentals/expressions-and-statements.tmd`
- `pages/fundamentals/control-flows.tmd`
- `pages/fundamentals/control-flows-more.tmd`
- `pages/fundamentals/line-break-rules.tmd`
- `pages/fundamentals/function-declarations-and-calls.tmd`
- `pages/fundamentals/function.tmd`
- `pages/fundamentals/defer-more.tmd`
- `pages/fundamentals/exceptions.tmd`
- `pages/fundamentals/panic-and-recover-more.tmd`
- `pages/fundamentals/panic-and-recover-use-cases.tmd`
- `pages/fundamentals/pointer.tmd`
- `pages/fundamentals/nil.tmd`
- `pages/fundamentals/string.tmd`
- `pages/fundamentals/struct.tmd`
- `pages/fundamentals/value-conversions-assignments-and-comparisons.tmd`
- `pages/fundamentals/value-part.tmd`
- `pages/fundamentals/type-system-overview.tmd`
- `pages/fundamentals/method.tmd`
- `pages/fundamentals/interface.tmd`
- `pages/fundamentals/channel.tmd`
- `pages/fundamentals/channel-closing.tmd`

## Tiếp tục

- Tiếp tục dịch các trang còn thiếu trong `pages/fundamentals/`, sau đó đi theo thứ tự `pages/generics/`, `pages/optimizations/`, `pages/details-and-tips/`, `pages/q-and-a/`, `pages/bugs/`, `pages/quizzes/`, `pages/apps-and-libs/`, và `pages/blog/`.
- Với các trang HTML không có nguồn `.tmd`, dịch file HTML tương ứng theo đúng hướng dẫn trong `AGENTS.md`.
- Kiểm tra trạng thái bằng `python3 scripts/translation_status.py` trước mỗi đợt cập nhật.
