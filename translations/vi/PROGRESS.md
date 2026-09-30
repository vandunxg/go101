# Tiến độ bản dịch Go 101

## Quy tắc cập nhật

- Chọn trang theo lộ trình bên dưới; dịch đầy đủ một trang trước khi chuyển trang khác.
- Sau khi soát bản dịch với nguồn tiếng Anh, chạy `python3 scripts/translation_status.py --mark-reviewed <đường-dẫn-nguồn>`.
- Chạy `python3 scripts/translation_status.py` để xem trang còn thiếu, đã cũ hoặc không còn nguồn.
- Không tự đánh dấu bản dịch là hiện hành khi upstream cập nhật.

## Đã dịch

Đã dịch và đối chiếu cấu trúc 86 trang trên nhiều nhóm tài liệu. Source blob SHA của từng trang đã được ghi trong `.sync-state.json`. Source blob SHA của từng trang đã được ghi trong `.sync-state.json`.

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

- `pages/fundamentals/memory-model.tmd`
- `pages/fundamentals/memory-layout.tmd`
- `pages/fundamentals/memory-block.tmd`
- `pages/fundamentals/concurrent-synchronization-overview.tmd`
- `pages/fundamentals/memory-leaking.tmd`
- `pages/fundamentals/concurrent-synchronization-more.tmd`
- `pages/fundamentals/concurrent-common-mistakes.tmd`
- `pages/fundamentals/concurrent-atomic-operation.tmd`
- `pages/fundamentals/channel-use-cases.tmd`
- `pages/fundamentals/evaluation-orders.tmd`
- `pages/fundamentals/summaries.tmd`
- `pages/fundamentals/type-embedding.tmd`
- `pages/fundamentals/reflection.tmd`
- `pages/fundamentals/details.tmd`
- `pages/fundamentals/unsafe.tmd`
- `pages/fundamentals/value-copy-cost.tmd`
- `pages/fundamentals/tips.tmd`
- `pages/fundamentals/more.tmd`
- `pages/fundamentals/unofficial-faq.tmd`
- `pages/fundamentals/101-about.tmd`
- `pages/fundamentals/acknowledgements.tmd`
- `pages/fundamentals/blocks-and-scopes.tmd`
- `pages/fundamentals/bounds-check-elimination-old.tmd`
- `pages/fundamentals/generic.tmd`
- `pages/fundamentals/go-sdk.tmd`
- `pages/fundamentals/panic-and-recover-more-newer.tmd`
- `pages/fundamentals/panic-and-recover-more-old.tmd`
- `pages/fundamentals/quizzes.tmd`
- `pages/fundamentals/bounds-check-elimination.tmd`
- `pages/fundamentals/100-updates.tmd`
- `pages/fundamentals/tools.tmd`
- `pages/fundamentals/tool-gold.tmd`
- `pages/fundamentals/tool-golds.tmd`
- `pages/generics/100-updates.tmd`
- `pages/generics/111-acknowledgements.html`
- `pages/optimizations/0.1-introduction.html`
- `pages/q-and-a/canonicalize-strings.tmd`
- `pages/q-and-a/clone-slices.tmd`
- `pages/q-and-a/create-slices.tmd`
- `pages/q-and-a/delete-contiguous-slice-elements.tmd`
- `pages/quizzes/const-1.tmd`
- `pages/q-and-a/iterate-bytes-in-a-string.tmd`
- `pages/q-and-a/iterate-runes-in-a-string.tmd`
- `pages/quizzes/const-2.tmd`
- `pages/q-and-a/make-dirty-byte-slices.tmd`
- `pages/quizzes/defer-1.tmd`
- `pages/q-and-a/take-string-byte-addresses.tmd`
- `pages/quizzes/call-1.tmd`
- `pages/quizzes/channel-1.tmd`
- `pages/quizzes/defer-2.tmd`
- `pages/quizzes/const-3.tmd`
- `pages/q-and-a/101.tmd`
- `pages/quizzes/const-4.tmd`
- `pages/bugs/go-build-directive-not-work.tmd`
- `pages/quizzes/loop-1.tmd`
- `pages/quizzes/slice-1.tmd`

## Tiếp tục

- Tiếp tục dịch các trang còn thiếu trong `pages/fundamentals/`, sau đó đi theo thứ tự `pages/generics/`, `pages/optimizations/`, `pages/details-and-tips/`, `pages/q-and-a/`, `pages/bugs/`, `pages/quizzes/`, `pages/apps-and-libs/`, và `pages/blog/`.
- Với các trang HTML không có nguồn `.tmd`, dịch file HTML tương ứng theo đúng hướng dẫn trong `AGENTS.md`.
- Kiểm tra trạng thái bằng `python3 scripts/translation_status.py` trước mỗi đợt cập nhật.
