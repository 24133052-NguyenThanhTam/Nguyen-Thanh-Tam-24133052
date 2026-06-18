GIAI ĐOẠN 1: BỘ LỌC AC3 TIỀN XỬ LÝ (Tỉa cung lỗi)
Giai đoạn này chạy ngầm ngay khi bấm nút nhằm "dọn dẹp" trước các màu chắc chắn gây sai sót.

Bước 1: Thiết lập danh sách cung (AC3_Giai_Doan_Dau) Chương trình quét toàn bộ bản đồ và gom tất cả các cặp vùng sát vách nhau thành các cặp cung ràng buộc (ví dụ: (WA, NT), (NT, WA)...). Tất cả được nạp vào một hàng đợi chung. Lúc này, mọi bang trên bản đồ đều hiển thị nhãn miền giá trị ban đầu là đủ 3 màu: [RGB].

Bước 2: Rút cung ra đối chiếu (Remove_Inconsistent_Values) Thuật toán liên tục lấy cặp cung đầu tiên (Xi, Xj) ra khỏi hàng đợi. Máy sẽ kiểm tra: Với mỗi màu trong nhãn [RGB] của Xi, có tồn tại màu nào ở láng giềng Xj sao cho hai bang khác màu nhau không? Nếu một màu của Xi chắc chắn gây trùng màu với mọi lựa chọn của Xj, màu đó bị xóa bỏ thẳng tay.

Bước 3: Lan truyền làn sóng lọc màu Nếu Xi vừa bị xóa bớt màu, các láng giềng khác của nó cũng có nguy cơ bị ảnh hưởng lây. Code sẽ đẩy ngược các cung liên quan vào lại hàng đợi để tái kiểm tra. Trên màn hình Canvas, bạn sẽ thấy các nhãn chữ [RGB] dưới tên bang bị co ngắn lại (ví dụ chỉ còn [RG] hoặc [R]), báo hiệu không gian tìm kiếm đã được thu hẹp tối đa và an toàn.

GIAI ĐOẠN 2: QUAY LUI TÔ MÀU BẢN ĐỒ (Backtracking)
Sau khi AC3 lọc xong dữ liệu sạch, hàm backtracking_to_mau lập tức nhảy vào cuộc để nhuộm màu trực quan lên giao diện.

Bước 4: Duyệt màu theo danh sách rút gọn Robot bắt đầu tiến hành tô màu tuần tự từ bang đầu tiên (WA). Thay vì thử mò mẫm cả 3 màu như các thuật toán cũ, vòng lặp lúc này chỉ chọn các màu đã được AC3 giữ lại sau đợt thanh lọc ở Giai đoạn 1.

Bước 5: Nhuộm màu trực quan và Đệ quy tiến tới Khi chọn được một màu hợp lệ, hệ thống gán màu cho bang đó, tăng biến đếm self.so_buoc lên 1, và lệnh cập nhật giao diện lập tức nhuộm vùng đất đó thành màu thực tế (Đỏ, Xanh lá, hoặc Xanh dương) trên Canvas. Sau khi tô xong, hàm tự động gọi đệ quy để nhảy sang bang kế tiếp.

Bước 6: Hoàn thành và Khóa bản đồ Nhờ có bộ lọc AC3 dọn đường từ trước, robot Backtracking chạy cực kỳ mượt mà, gần như không bị xung đột và không phải quay lui (xóa màu làm lại) giữa chừng. Khi tất cả các bang đều đã được gán màu thành công, bản đồ phủ kín màu sắc, chương trình dừng lại và xuất thông báo hoàn thành lời giải.