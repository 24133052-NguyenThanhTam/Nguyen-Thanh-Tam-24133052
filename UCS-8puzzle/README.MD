UCS (Uniform Cost Search) - Tìm kiếm chi phí đồng đều
Bước 1 (Khởi tạo): Nạp cấu hình bàn cờ ban đầu vào Hàng đợi ưu tiên với chi phí tích lũy g = 0 (chưa đi bước nào) và danh sách hướng đi trống.
Bước 2 (Chọn bàn cờ tối ưu): Lấy cấu hình bàn cờ có số bước đi lũy kế g nhỏ nhất ở đầu hàng đợi ra để xét. Đánh dấu bàn cờ này đã duyệt.
Bước 3 (Kiểm tra đích): So sánh bàn cờ vừa lấy ra với ma trận đích. Nếu khớp hoàn toàn -> Dừng và xuất chuỗi bước đi ngắn nhất. Nếu sai -> Chuyển sang Bước 4.
Bước 4 (Dịch chuyển ô trống): Từ vị trí ô trống 0, thử di chuyển sang các hướng hợp lệ: Lên, Xuống, Trái, Phải. Mỗi hướng di chuyển tạo ra một bàn cờ con mới với chi phí tăng thêm 1 bước (g_{\text{con}} = g_{\text{cha}} + 1).
Bước 5 (Cập nhật hàng đợi): Lọc các bàn cờ con vừa sinh ra:Nếu cấu hình bàn cờ đó chưa từng xuất hiện -> Nạp vào hàng đợi ưu tiên kèm theo hướng đi vừa di chuyển (Ví dụ: "Phải", "Len").Hàng đợi tự động sắp xếp để đẩy các bàn cờ có ít bước đi hơn lên đầu. Quay lại Bước 2.