# Translation Style — English-first cho Go Developer Việt

## Mục tiêu văn phong

Bản dịch phải đọc như tài liệu kỹ thuật do Go developer Việt viết: trực tiếp, chính xác và tự nhiên. Dịch ngữ pháp, liên từ và diễn giải thông thường sang tiếng Việt; giữ English technical terms khi đó là cách dùng chuẩn hơn trong cộng đồng Go.

Giữ tone của Go 101: kỹ thuật, súc tích, có tính giải thích; không marketing, không cảm thán và không thêm lời bình của translator.

## English-first theo meaning, không theo token

Không ép dịch từng token có từ tiếng Việt tương đương.

- `channel` là Go concept → giữ `channel`.
- “send a value to a channel” → có thể dịch “gửi một value vào channel”.
- `map` là Go type → giữ `map`.
- “map a path to a handler” → dịch theo nghĩa của câu nếu đó không phải type `map`.
- `interface` là Go concept → giữ `interface`; “interface with a system” có thể dịch theo nghĩa thông thường.

Một technical concept phải dùng nhất quán trong cùng trang/section. Không xen kẽ tùy ý `goroutine` với “luồng nhẹ”, `slice` với “lát cắt”, `pointer` với “con trỏ”, hoặc `method` với “phương thức” khi đang nói cùng một concept.

## Technical verbs

Có thể giữ English khi tự nhiên và chính xác hơn, ví dụ: `allocate`, `initialize`, `iterate`, `compare`, `convert`, `assign`, `copy`, `append`, `delete`, `close`, `send`, `receive`, `block`, `synchronize`, `schedule`, `panic`, `recover`, `defer`, `benchmark`, `profile`, `compile`, `escape`.

Câu vẫn phải là câu tiếng Việt; không biến cả câu thành English.

## API, type, identifier và code

Giữ nguyên casing/spelling của mọi API/type/identifier, ví dụ: `int`, `any`, `error`, `Stringer`, `io.Reader`, `fmt.Printf`, `sync.Mutex`, `context.Context`, `go test`, `GOMAXPROCS`, `make`, `new`, `len`, `cap`, `append`, `close`.

Không dịch Go keyword, command output, compiler error, directive, file path, URL, anchor, module path hay code literal. Chỉ dịch comment trong code khi comment là prose giải thích của tài liệu và việc dịch không làm thay đổi ví dụ thực thi.

## Modal strength

Bảo toàn strength của source:

- `must` → thường là “phải”;
- `should` → “nên”, “cần” hoặc “phải” theo context gốc;
- `may` → “có thể”, “được phép” hoặc nghĩa phù hợp;
- `must not` → “không được” hoặc “không được phép”.

Không làm recommendation yếu đi hoặc mạnh hơn.

Ví dụ:

`Do not communicate by sharing memory; share memory by communicating.`

→ `Đừng giao tiếp bằng cách chia sẻ memory; hãy chia sẻ memory bằng cách giao tiếp.`

## Heading, title và cross-reference

Giữ cấu trúc title, number và anchor gốc để cross-reference không hỏng. Dịch phần prose của heading; giữ tên series/product/API, số version, identifier và route theo source.

Không tự thêm giải thích trong ngoặc sau mỗi English term, ví dụ tránh `goroutine (luồng nhẹ)` hay `slice (lát cắt)` lặp lại. Chỉ giải thích khi source hoặc context thật sự cần.

## Câu tiếng Việt và punctuation

- Viết câu ngắn, rõ subject/object, không dịch theo trật tự tiếng Anh máy móc.
- Dùng dấu câu tiếng Việt bình thường; đặt khoảng trắng hợp lý giữa prose và English technical terms.
- Không thêm “chúng ta”, “tôi”, “bạn” nếu source không yêu cầu. Có thể dùng “bạn” khi source trực tiếp hướng dẫn người đọc.
- Giữ ví dụ, phép so sánh và mức độ thận trọng của tác giả.
