Thuật toán BFS (Breadth-First Search) - Tìm kiếm theo chiều rộng
Thuật toánBFS sử dụng một hàng đợi Queue (FIFO - Vào trước ra trước). Nó duyệt qua tất cả các nút ở độ sâu hiện tại trước khi di chuyển xuống tầng sâu hơn.
Các bước chạy chi tiết
Bước 1: Khởi tạo Queue chứa trạng thái ban đầu. Khởi tạo tập hợp Visited (đã duyệt) để tránh lặp lại trạng thái.Bước 2: Kiểm tra nếu Queue rỗng thì kết thúc (Thất bại). Ngược lại, lấy trạng thái đầu tiên ra khỏi Queue (gọi là nút U).
Bước 3: Kiểm tra nếu U là Trạng thái Đích -> Trích xuất đường đi và dừng thuật toán.
Bước 4: Thêm U vào tập Visited.
Bước 5: Tìm các ô hàng xóm của U (bằng cách di chuyển ô 0). Với mỗi nút con V sinh ra:Nếu V chưa nằm trong Visited và chưa có trong Queue -> Thêm $V$ vào cuối Queue.
Bước 6: Quay lại Bước 2.Hình dung: BFS quét bàn cờ theo từng lớp cắt ngang. Lớp 1 bước đi -> Lớp 2 bước đi ->Lớp 3 bước đi... Do đó chắc chắn tìm được đường ngắn nhất.