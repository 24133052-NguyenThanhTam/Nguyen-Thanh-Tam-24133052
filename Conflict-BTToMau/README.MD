GIAI ĐOẠN 1: BỘ LỌC CUNG AC3 (Chạy ngầm trước)
Mục đích: Loại bỏ sớm các màu chắc chắn gây sai sót để thu hẹp không gian tìm kiếm.
Bước 1 (Gom cung): Hệ thống tự động tạo danh sách các cặp bang sát vách nhau (gọi là các cung ràng buộc). Lúc này, nhãn dưới mỗi bang đều hiển thị đủ 3 màu khả dụng: [RGB].
Bước 2 (Cắt tỉa màu lỗi): Thuật toán duyệt qua từng cung. Nếu phát hiện một màu của bang này chắc chắn gây trùng màu với mọi lựa chọn của bang hàng xóm, màu đó sẽ bị xóa bỏ thẳng tay khỏi bộ nhớ.
Bước 3 (Lan truyền): Việc xóa màu này được lan truyền sang các bang lân cận khác. Trên màn hình, bạn sẽ thấy nhãn chữ [RGB] của một số bang bị rút ngắn lại (ví dụ chỉ còn [RG]), báo hiệu dữ liệu đã được lọc sạch mâu thuẫn.
GIAI ĐOẠN 2: TÔ MÀU BẢN ĐỒ BACKTRACKING (Nhuộm màu trực quan)
Mục đích: Sử dụng hàm conflict để gán màu thực tế lên giao diện Canvas.
Bước 4 (Duyệt màu rút gọn): Robot bắt đầu tô màu tuần tự từng bang. Vòng lặp chỉ thử nghiệm các màu đã được bộ lọc AC3 chứng minh là an toàn ở Giai đoạn 1.
Bước 5 (Gọi hàm conflict): Trước khi đổ màu lên đa giác, hệ thống gọi hàm conflict. Hàm này quét nhanh qua các hàng xóm xung quanh:Nếu Trùng màu láng giềng đã tô: Báo có xung đột -> Thuật toán bỏ qua màu này để thử phương án khác.Nếu Không trùng ai cả: Báo an toàn -> Cho phép chuyển sang Bước 6.
Bước 6 (Nhuộm màu và Về đích): Khi xác nhận an toàn, Canvas lập tức nhuộm vùng đất đó thành màu thực tế (Đỏ, Xanh lá, Xanh dương), tăng số bước toán và đệ quy tiến lên cho đến khi toàn bộ bản đồ được phủ kín màu sắc hoàn hảo.