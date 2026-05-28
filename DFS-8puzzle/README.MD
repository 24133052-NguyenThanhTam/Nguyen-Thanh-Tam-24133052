Thuật toán DFS (Depth-First Search) - Tìm kiếm theo chiều sâu
Thuật toán DFS sử dụng cấu trúc Stack (LIFO - Vào sau ra trước) hoặc cơ chế đệ quy. Nó đi sâu nhất có thể theo một nhánh cho đến khi gặp ngõ cụt mới quay lui (Backtrack).
Các bước chạy chi tiết
Bước 1: Khởi tạo Stack chứa trạng thái ban đầu.
Bước 2: Nếu Stack rỗng-> Thất bại. Ngược lại, lấy trạng thái ở đỉnh Stack ra (nút U).
Bước 3: Nếu U là Trạng thái Đích -> Kết thúc.
Bước 4: Thêm U vào Visited.
Bước 5: Sinh các nút con V của U. Với mỗi nút con V chưa duyệt:Đẩy V vào đỉnh Stack.
Bước 6: Quay lại Bước 2.
Hình dung: DFS giống như đi trong mê cung, cứ rẽ bừa vào một ngách sâu hun hút cho tới khi đập đầu vào tường mới chịu lùi lại tìm ngách khác. Với 8-Puzzle, nếu không giới hạn độ sâu, DFS có thể chạy tới hàng triệu bước đi luẩn quẩn