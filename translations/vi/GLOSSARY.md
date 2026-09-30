# Glossary — Go 101 tiếng Việt

Glossary là baseline, không phải whitelist. Với technical term chưa có trong danh sách, giữ English nếu đó là cách viết chuẩn và tự nhiên hơn trong ngữ cảnh Go/software engineering.

## Nguyên tắc

- Cùng một technical concept dùng nhất quán trong cùng trang/section.
- API/type/package/identifier giữ nguyên spelling và casing.
- Không tự thêm bản dịch tiếng Việt trong ngoặc sau mỗi English term.
- Một từ vừa có nghĩa kỹ thuật vừa có nghĩa đời thường phải được dịch theo meaning của câu.
- Chỉ bổ sung glossary khi term xuất hiện lặp lại hoặc dễ tạo cách dùng không nhất quán.

| Nhóm | Thuật ngữ ưu tiên giữ nguyên |
| --- | --- |
| Go core | Go, runtime, compiler, Go toolchain, module, package, import path, workspace, standard library, keyword, identifier, literal, constant, variable, value, zero value, nil |
| Types | type, type definition, type alias, underlying type, named type, unnamed type, type parameter, type argument, type constraint, type set, interface, method set, comparable, generic, instantiation |
| Containers | array, slice, map, string, channel, element, index, key, capacity |
| Functions | function, method, receiver, closure, callback, variadic function, defer, panic, recover, return value |
| Pointers/memory | pointer, reference, address, allocation, stack, heap, escape analysis, garbage collector, garbage collection (GC), memory block, memory layout, memory model |
| Concurrency | goroutine, channel, send, receive, close, select, synchronization, atomic operation, data race, race condition, deadlock, blocking, scheduler, happens-before, wait group, mutex |
| Errors | error, error value, error interface, panic, stack trace, exception-like behavior |
| Reflection/unsafe | reflection, reflect, unsafe, pointer arithmetic, addressability, settable value |
| Tooling | build, compile, link, test, benchmark, profile, debug, formatter, linter, Go command, `go vet` |
| Design/API | API, abstraction, encapsulation, contract, invariant, implementation, interface satisfaction, embedding, promotion, method expression, method value |

## Mapping style quan trọng

| Source concept | Style ưu tiên |
| --- | --- |
| goroutine | goroutine |
| channel | channel |
| slice | slice |
| map | map |
| interface | interface |
| method set | method set |
| type parameter | type parameter |
| type constraint | type constraint |
| type set | type set |
| zero value | zero value |
| nil | nil |
| pointer | pointer |
| reference | reference |
| receiver | receiver |
| embedding | embedding |
| method promotion | method promotion |
| panic / recover / defer | panic / recover / defer |
| data race | data race |
| memory model | memory model |
| happens-before | happens-before |
| garbage collection (GC) | garbage collection (GC) |
| runtime | runtime |
| Go toolchain | Go toolchain |
| type assertion | type assertion |
| type switch | type switch |
| range clause | range clause |
| escape analysis | escape analysis |
| raw string literal | raw string literal |

## Thuật ngữ theo ngữ cảnh

Các từ `value`, `type`, `function`, `variable`, `memory`, `operation`, `assignment`, `conversion`, `comparison`, `call`, `statement`, `expression`, `scope`, `block`, `field`, `method` có thể dịch hoặc giữ English theo ngữ cảnh. Dùng nhất quán trong từng section và không dịch khi chúng là một phần của API/identifier/literal.

## Bổ sung glossary

Khi gặp term mới:

1. Xác định đây có phải technical/domain concept trong Go hay không.
2. Kiểm tra cách dùng của term trong source, Go spec, API hoặc code context của trang.
3. Nếu English làm câu rõ và chuẩn hơn, giữ English.
4. Dùng nhất quán trong toàn trang.
5. Chỉ thêm vào glossary sau khi term lặp lại hoặc dễ gây không nhất quán.
