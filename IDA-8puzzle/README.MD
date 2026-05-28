Thuật toán IDA* (Iterative Deepening A*) - Tìm sâu lặp chi phí tăng dần
Thuật toán IDA* giải quyết bài toán ngốn RAM của A*. Thay vì lưu toàn bộ các nút vào bộ nhớ, IDA* chạy bằng DFS đệ quy để tiết kiệm RAM, nhưng giới hạn độ sâu bằng một Ngưỡng chi phí (Threshold) bằng giá trị f(n).
Các bước chạy chi tiết (Vòng lặp chạy thực tế)
Giả sử bàn cờ ban đầu có trạng thái S.
Vòng lặp 1: Đặt Ngưỡng = f(S) = g(S) + h(S).Chạy hàm DFS_IDA từ nút S.Trong lúc đệ quy đi sâu xuống, nếu gặp bất kỳ nút nào có f(n) > Ngưỡng -> Cắt tỉa nhánh đó luôn (không đi sâu nữa) và trả về giá trị f(n) bị vượt đó.Nếu tìm thấy Đích trong vòng lặp này -> Dừng, thành công.
Vòng lặp 2: Nếu Vòng 1 không tìm thấy đích, lấy giá trị f(n) nhỏ nhất trong số các nhánh đã bị cắt tỉa ở vòng trước để làm Ngưỡng mới.Xóa toàn bộ lịch sử đệ quy (giải phóng RAM hoàn toàn).Chạy lại DFS_IDA từ nút S với Ngưỡng mới rộng hơn.Vòng lặp tiếp theo: Cứ liên tục nới rộng Ngưỡng cho đến khi nhánh DFS chạm được vào trạng thái Đích.