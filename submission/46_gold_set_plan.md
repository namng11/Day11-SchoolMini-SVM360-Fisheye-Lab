# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Xe ngược chiều lóa sáng | Vật thể mờ nhòe do chói đèn pha | Giữ ego_body làm mốc | Soát chéo bởi chuyên gia |
| rear | Trẻ em/Vật nhỏ sát đuôi xe | Hình ảnh bị méo gập rất nặng | Căn chuẩn đường viền lens_border | Kiểm tra mù độc lập |
| left | Xe máy cắt ngang góc trái | Người/Xe bị cắt lẹm một nửa | Xác định kỹ vùng chồng lấn (seam) | Đối chiếu với quy tắc gán nhãn |
| right | Chướng ngại vật sát lề | Dễ nhầm với người đi bộ trên vỉa hè | Giữ chuẩn ranh giới lề đường | Kiểm tra mù độc lập |

- Khi nào cần refresh gold set (đổi camera, calibration hoặc rule): Khi hãng xe cập nhật phiên bản camera mới, đổi vị trí gắn cam làm thay đổi độ méo, hoặc khi luật gán nhãn có thay đổi lớn.
- Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box: Một chiếc xe máy đi ngang qua vùng tiếp giáp (seam) giữa camera trước và trái, khiến nó hiện trên cả 2 camera. Cần luật rõ ràng trước khi quyết định nối 2 box này làm một.
- Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera: Đặc thù biến dạng ảnh (méo), góc khuất và ánh sáng ở 4 camera là hoàn toàn khác nhau. Một model chạy tốt trên cam trước chưa chắc đã bắt đúng xe trên cam phải.
