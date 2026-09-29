# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_249480.jpg
- L2 edge IGNORE_SCOPE
## adasind_261480.jpg
- L4 mid SPURIOUS
## adasind_265065.jpg
- L5 mid IGNORE_SCOPE
- L4 center SPURIOUS
- R5 mid MISSING
- R7 mid MISSING

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 4 | 4 | 0 | 1 |
| mid | 13 | 11 | 2 | 1 |
| edge | 0 | 0 | 0 | 0 |
