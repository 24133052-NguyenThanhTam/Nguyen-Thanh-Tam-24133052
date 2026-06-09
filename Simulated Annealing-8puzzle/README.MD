thuật toán Simulated Annealing
Bước 1: Khởi tạo hệ thốngBật lò nung ($T = 25.0$):
    Đặt nhiệt độ ban đầu thật cao để các ô số dễ dàng nhảy tự do.Đặt ngưỡng đóng băng ($T_{min} = 0.05$): Khi lò nguội đến mức này, thuật toán sẽ dừng lại.Tính điểm hỗn loạn: Đo xem bàn cờ hiện tại đang cách đích bao xa (bằng khoảng cách Manhattan).
Bước 2: Chọn bừa một hướng điTìm lối đi:
    Xem ô trống có thể gạt sang hướng nào (Trái, Phải, Lên, Xuống).Bốc thăm ngẫu nhiên: Thay vì tính toán chọn hướng tốt nhất, thuật toán chỉ chọn đại duy nhất 1 hướng để đi thử (gọi là trạng thái kế tiếp $E_{kế}$).
Bước 3: So sánh độ tốt/xấu 
    Thuật toán lấy: $\Delta E = \text{Điểm cũ} - \text{Điểm mới}$ để xem bước đi vừa rồi tốt hay xấu:Nếu tốt ($\Delta E > 0$): Bàn cờ gọn gàng hơn -> Chấp nhận 100% để đi tiếp (Leo đồi tốt).Nếu xấu ($\Delta E \le 0$): Bàn cờ bị xáo trộn hơn -> Không từ chối ngay, mà chuyển sang Bước 4 để tính cơ hội.
Bước 4: Tung xúc xắc "Vượt bẫy" (Nếu gặp bước đi xấu)Tính tỷ lệ ăn may ($P$):
    Dựa vào nhiệt độ $T$ hiện tại để tính xác suất giữ lại bước đi xấu này.Tung xúc xắc: Lấy một số ngẫu nhiên từ $0$ đến $1$.Ra quyết định: * Nếu may mắn trúng tỷ lệ $P$ -> Vẫn chấp nhận đi tiếp dù đây là bước đi lùi. Việc này giúp bàn cờ nhảy ra khỏi các "hố kẹt" (thế bí cục bộ).Nếu trượt -> Hủy bước đi đó, giữ nguyên vị trí cũ.
Bước 5: Hạ nhiệt và Lặp lạiHạ nhiệt độ:
    Giảm bớt độ nóng của lò nung ($T = T \times 0.94$).Đặc điểm: * Lúc đầu lò còn nóng ($T$ cao): Thuật toán rất "dễ tính", hay đi lung tung để thử nghiệm.Lúc sau lò nguội dần ($T$ thấp): Thuật toán trở nên "khó tính", hầu như không chấp nhận đi lùi nữa mà chỉ đi thẳng về đích.Vòng lặp: Quay ngược lại Bước 2. Chu trình chạy liên tục cho đến khi bàn cờ xếp đúng vị trí đích hoặc lò bị đóng băng ($T \le 0.05$).