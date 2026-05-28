thuật toán IDS (Sâu lặp tăng dần)
IDS giải quyết lỗi đi vô hạn của DFS bằng cách ép DFS chạy trong một cái "khung" độ sâu cố định.
Bước 1: Đặt giới hạn độ sâu ban đầu Limit = 0.
Bước 2 (Chạy DFS giới hạn): Gọi hàm đệ quy DFS bắt đầu từ trạng thái gốc:Nếu nút hiện tại là đích -> Dừng/Thành công.Nếu độ sâu hiện tại bằng Limit -> Không đi tiếp nữa, quay lui (Backtrack) lên nút cha để tìm nhánh khác.
Bước 3 (Tăng giới hạn): Nếu vòng DFS ở Bước 2 kết thúc mà không tìm thấy đích:Xóa toàn bộ lịch sử các nút đã duyệt khỏi bộ nhớ RAM để giải phóng không gian.Tăng Limit = Limit + 1.
Bước 4 (Lặp): Quay lại Bước 2 để chạy lại một chu kỳ DFS mới sâu hơn 1 tầng.