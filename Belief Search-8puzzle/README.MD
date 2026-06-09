Tìm kiếm mù theo chiều rộng (BFS)
Bước 1: Khởi tạo hệ thống
    Tạo Queue: Chuẩn bị một danh sách rỗng hoạt động theo kiểu "Vào trước, xử lý trước" (FIFO).
    Nạp bàn cờ đầu: Đẩy cấu hình bàn cờ hiện tại của bạn vào vị trí đầu tiên của Queue.
    Tạo danh sách Đã duyệt: Ghi nhận bàn cờ đầu tiên này vào bộ nhớ để chống thuật toán đi lặp lại một vị trí.
    Đặt Bộ đếm RAM: Cài đặt số lượng nút đã quét ban đầu bằng 1.
Bước 2: Bóc tách và Kiểm tra đích
    Lấy phần tử đầu: Rút cấu hình bàn cờ đang đứng ở vị trí đầu tiên trong Queue ra để bắt đầu xử lý.
    So sánh với Đích: Kiểm tra xem các số trên bàn cờ vừa lấy ra đã xếp đúng thứ tự từ 1 đến 8 chưa.
    Ra quyết định: Nếu Đúng thì dừng thuật toán và xuất đường đi. Nếu Sai thì chuyển tiếp sang Bước 3.
Bước 3: Tìm các hướng đi hợp lệ
    Định vị ô trống: Tìm vị trí hiện tại của số 0 (ô trống) trên bàn cờ đang xét.
    Liệt kê hướng dịch: Xác định xem số 0 có thể gạt sang hướng nào (Trái, Phải, Lên, Xuống) mà không bị vượt ra ngoài viền 3x3.
Bước 4: Kiểm tra trùng và Nạp vào Queue
    Tạo bàn cờ mới: Thử gạt số 0 theo từng hướng hợp lệ ở Bước 3 để tạo ra các bàn cờ con tương ứng.
    Lọc trùng: Đối chiếu từng bàn cờ con vừa tạo với danh sách Đã duyệt.
    Đẩy vào Queue: Nếu bàn cờ con đã trùng thì vứt bỏ. Nếu mới hoàn toàn thì lưu nó vào danh sách Đã duyệt, cộng thêm 1 vào bộ đếm RAM và đẩy nó vào cuối Queue.
Bước 5: Lặp lại vòng tuần hoàn
    Quay lại: Thuật toán tự động quay ngược trở về Bước 2 để bóc phần tử tiếp theo đang đứng đầu Queue.
    Vòng lặp: Quá trình Bước 2 -> Bước 3 -> Bước 4 -> Bước 2 sẽ chạy liên tục cho đến khi tìm thấy đích hoặc Queue trống rỗng.