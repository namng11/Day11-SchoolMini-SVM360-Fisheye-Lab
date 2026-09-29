# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B4 | MISSING | 1 |
| center | B4 | SPURIOUS | 6 |
| center | C0 | SPURIOUS | 3 |
| edge | B4 | BOX_GEOMETRY | 1 |
| edge | B4 | IGNORE_SCOPE | 1 |
| edge | B4 | SPURIOUS | 1 |
| mid | B4 | ATTRIBUTE | 1 |
| mid | B4 | IGNORE_SCOPE | 1 |
| mid | B4 | MISSING | 6 |
| mid | B4 | SPURIOUS | 9 |
| mid | B4 | WRONG_CLASS | 1 |

## Top defects
- SPURIOUS: 19 (ví dụ frame adasind_019560.jpg)
- MISSING: 7 (ví dụ frame adasind_265065.jpg)
- IGNORE_SCOPE: 2 (ví dụ frame adasind_249480.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: Xong
- Cách sửa và ai nhận việc (`owner`): Xong
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): Xong
