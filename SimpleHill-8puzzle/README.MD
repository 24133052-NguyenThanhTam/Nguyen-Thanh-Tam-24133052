Bước 1 (Tính Cost hiện tại): Xác định cấu hình bàn cờ hiện hành và đếm Số ô sai vị trí của nó .
Bước 2 (Kiểm tra đích): Nếu số ô sai bằng 0 -> Đã giải xong, dừng thuật toán thành công.
Bước 3 (Kiểm tra từng hướng): Ô trống lần lượt dịch chuyển thử theo các hướng hợp lệ (Trái -> Phải -> Lên -> Xuống). Mỗi hướng tạo ra một bàn cờ con.
Bước 4 (Nhảy bước lập tức): Đếm số ô sai của bàn cờ con vừa sinh ra .Nếu Cost{con} < Cost{cha} (Số ô sai giảm đi) -> Máy chốt luôn hướng đi này, thay đổi bàn cờ hiện tại thành bàn cờ con và quay lại Bước 2 ngay lập tức (không cần kiểm tra các hướng còn lại).
Bước 5 (Báo kẹt): Nếu đã xoay ô trống sang mọi hướng xung quanh mà không có bất kỳ cấu hình nào làm giảm được số ô sai so với ban đầu -> Thuật toán rơi vào Đỉnh cục bộ (Local Minimum) và dừng chạy.