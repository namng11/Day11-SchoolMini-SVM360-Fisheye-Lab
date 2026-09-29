# Quan sát vạch ô đỗ

- Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh): Các vạch sơn màu trắng chia từng ô đỗ xe ở ngay góc tiền cảnh (dưới cùng bên phải) và cụm ô đỗ xe ở giữa sân bên trái.
- Một vạch/dấu sơn hoặc biên **không** vẽ, và vì sao: Đường sơn màu vàng nét đứt/liền kéo dài ngang qua sân ở phía xa bên phải. Vì đây là vạch phân làn/chỉ dẫn lối đi chung của bãi, không phải vạch phân chia một ô đỗ xe cụ thể nào cả.
- Polygon `free_space` dừng ở đâu; có phần bị che nào không: Dừng ở ranh giới bên ngoài của các dãy ô đỗ xe (không lấn vào trong ô đỗ). Kéo dài đến sát hàng rào phía xa. Không có vật cản lớn nào che khuất ngoài chiếc xe tải nhỏ màu đỏ ở phía xa bên trái.
- Ca chưa chắc cần hỏi người soát (nếu không có, ghi “không có”): Vùng mặt sân sát hàng rào ở tít phía xa khá mờ, khó phân định chính xác đâu là lề đường và đâu là mặt đường chạy.
