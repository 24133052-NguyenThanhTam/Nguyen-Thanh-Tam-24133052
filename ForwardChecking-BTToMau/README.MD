Thuật toán Forward Checking (Nhìn trước loại trừ)
Thuật toán này thông minh hơn nhờ sở hữu một "bộ lọc" liên tục thu hẹp các khả năng để tránh đi sai đường.
Bước 1: Khởi tạo Miền giá trị (mien_ban_dau) Trước khi chạy, code tạo ra một cuốn sổ tay ghi nhớ miền giá trị cho cả 7 bang, ban đầu bang nào cũng có đủ 3 màu: ["Red", "Green", "Blue"].
Bước 2: Kiểm tra chặn đứng (Bước số 30) Tương tự, mỗi lần gán màu là self.so_buoc tăng 1. Nếu chạm ngưỡng 30 bước, hệ thống ngắt đệ quy ngay lập tức và báo kẹt.
Bước 3: Chọn màu và Nhuộm Canvas Thuật toán chọn thử một màu hợp lệ trong miền giá trị hiện tại của bang (ví dụ: gán WA = Đỏ), vẽ lên Canvas.
Bước 4: Nhìn trước và Lọc màu láng giềng Tạo một bản sao miền giá trị mới (mien_gia_tri_moi). Thuật toán quét các láng giềng chưa tô của WA (ở đây là NT và SA) rồi chủ động xóa màu Đỏ ra khỏi danh sách của hai bang này.
Bước 5: Phát hiện sớm bế tắc (Cắt tỉa nhánh) Code kiểm tra: Có bang láng giềng nào sau khi bị xóa màu Đỏ mà tập màu bị rỗng [] luôn không?
    Nếu có láng giềng bị rỗng màu: Nhánh này chắc chắn sai! Thuật toán hủy màu vừa gán ngay tại chỗ, không thèm đệ quy tiếp mà quay xe thử màu khác, tiết kiệm rất nhiều bước toán thừa.
    Nếu không có ai bị rỗng: Tự tin gọi đệ quy tiến sâu với tập mien_gia_tri_moi đã được lọc sạch.