Thuật toán A* (A-Star Search) - 
Tìm kiếm thông minh bằng Heuristic:
Các nút trong hàng đợi được sắp xếp theo giá trị hàm đánh giá $f(n)$ thấp nhất:
f(n) = g(n) + h(n)
g(n): Chi phí để đi từ trạng thái đầu đến trạng thái hiện tại.
h(n): Ước lượng chi phí từ hiện tại đến đích (ví dụ: Số ô sai vị trí).
Các bước chạy chi tiết:
Bước 1: Khởi tạo Priority Queue chứa nút ban đầu với f(n) = g(n) + h(n)
Bước 2: Lấy nút U có f(n) nhỏ nhất ra khỏi hàng đợi
Bước 3: Nếu U là Đích \rightarrow Xuất lời giải và kết thúc
Bước 4: Thêm U vào tập đóng (đã duyệt)
Bước 5: Với mỗi trạng thái con V của U:
    Tính g(V) = g(U) + 1 (hoặc tính theo số dãy ngược tùy cấu hình)
    Tính h(V) (Số ô sai).Tính $f(V) = g(V) + h(V)
    Nếu V chưa từng duyệt hoặc tìm thấy một đường đi tới $V$ có chi phí f(V) tốt hơn trước
    Thêm/Cập nhật V vào Priority Queue
Bước 6: Quay lại Bước 2