NHÓM I: TÌM KIẾM MÙ (UNINFORMED SEARCH)

1. Thuật toán BFS (Breadth-First Search)
    Bước 1: Khởi tạo một hàng đợi Queue (FIFO - Vào trước ra trước). Đẩy trạng thái bàn cờ ban đầu (start_state) vào đầu hàng đợi.
    Bước 2: Khởi tạo một tập hợp visited = set() dùng để lưu trữ các cấu hình đã duyệt, tiến hành thêm start_state vào tập hợp này.
    Bước 3: Kiểm tra xem Queue có bị rỗng hay không. Nếu rỗng, thuật toán dừng lại và báo Thất bại (Không tìm thấy lời giải). Ngược lại, lấy trạng thái đầu tiên ra khỏi Queue, gọi đây là nút hiện tại U.
    Bước 4: Kiểm tra đích: So sánh cấu hình của U với TRANG_THAI_DICH_PHANG. Nếu trùng khớp hoàn toàn, thuật toán dừng lại, trích xuất chuỗi hành động và báo Thành công.
    Bước 5: Xác định vị trí của ô trống (số 0) trên bàn cờ U. Thử nghiệm di chuyển ô trống này theo 4 hướng hợp lệ (Trái, Phải, Lên, Xuống) để tạo ra các trạng thái con V.
    Bước 6: Duyệt qua từng trạng thái con V vừa được sinh ra: Nếu V chưa từng nằm trong tập visited, thực hiện thêm V vào tập visited đồng thời đẩy V vào cuối hàng đợi Queue.
    Bước 7: Quay trở lại thực hiện tiếp Bước 3.

2. Thuật toán DFS (Depth-First Search)
    Bước 1: Khởi tạo một ngăn xếp Stack (LIFO - Vào sau ra trước). Đẩy trạng thái ban đầu vào Stack kèm theo thông tin quản lý: (start_state, danh_sách_hành_động, độ_sâu = 0).
    Bước 2: Kiểm tra xem Stack có bị rỗng hay không. Nếu rỗng, thuật toán dừng lại và báo Thất bại. Ngược lại, bóc phần tử nằm ở đỉnh trên cùng của Stack ra, gọi là nút U.
    Bước 3: Kiểm tra đích: Nếu cấu hình của nút U trùng khớp hoàn toàn với trạng thái đích, thuật toán lập tức dừng lại và xuất lời giải (Thành công).
    Bước 4: Kiểm tra giới hạn: Nếu mức độ_sâu của nút U đã đạt tới ngưỡng giới hạn tối đa được lập trình cấu hình, thuật toán sẽ bỏ qua nút này, tiến hành Quay lui (Backtrack) bằng cách nhảy thẳng về Bước 2 để xét nút khác.
    Bước 5: Di chuyển ô trống (số 0) của nút U theo các hướng hợp lệ để sinh ra danh sách các trạng thái con V.
    Bước 6: Với mỗi trạng thái con V, nếu V chưa từng xuất hiện trên nhánh đường đi hiện tại (để tránh tạo vòng lặp vô hạn), thực hiện đẩy V lên trên đỉnh ngăn xếp Stack kèm mức độ sâu tăng 1 đơn vị (độ_sâu + 1).
    Bước 7: Quay trở lại thực hiện tiếp Bước 2.

3. Thuật toán IDS (Iterative Deepening Search)
    Bước 1: Thiết lập mức giới hạn chiều sâu ban đầu cho hệ thống tìm kiếm là Limit = 0.
    Bước 2: Kích hoạt một chu kỳ chạy thuật toán DFS giới hạn chiều sâu: Hệ thống tiến hành tìm kiếm từ trạng thái gốc nhưng chặn tuyệt đối không cho phép đi sâu vượt quá mức Limit hiện tại.
    Bước 3: Kiểm tra trong quá trình quét của chu kỳ: Nếu phát hiện bất kỳ nút nào trùng khớp với trạng thái đích, lập tức dừng toàn bộ chương trình và báo Thành công.
    Bước 4: Nếu chu kỳ DFS kết thúc (đã duyệt hết tất cả các khả năng trong tầm với) mà vẫn không tìm ra đích, thuật toán tiến hành giải phóng bộ nhớ RAM bằng cách xóa sạch lịch sử các nút đã duyệt của chu kỳ vừa rồi.
    Bước 5: Thực hiện nới lỏng tầm nhìn bằng cách tăng giới hạn chiều sâu lên một tầng: Limit = Limit + 1.
    Bước 6: Quay trở lại Bước 2 để bắt đầu một chu kỳ tìm kiếm DFS mới sâu hơn.

NHÓM II: TÌM KIẾM CÓ GỢI Ý (INFORMED SEARCH)

4. Thuật toán Greedy Best-First Search (Tham lam)
    Bước 1: Khởi tạo một hàng đợi ưu tiên Priority Queue (Min-Heap - cấu trúc tự động sắp xếp phần tử có điểm nhỏ nhất lên đầu) và một tập hợp lưu trữ visited = set().
    Bước 2: Tính toán khoảng cách Heuristic $h(start)$ (Khoảng cách Manhattan - tổng khoảng cách dịch chuyển ô số về đúng vị trí) cho trạng thái ban đầu, sau đó đẩy trạng thái này vào Heap.
    Bước 3: Kiểm tra Heap. Nếu Heap rỗng, thuật toán dừng và báo Thất bại. Ngược lại, trích xuất trạng thái có giá trị Heuristic $h$ nhỏ nhất ra khỏi Heap, gọi là nút U.
    Bước 4: Nếu U trùng khớp với trạng thái đích, dừng thuật toán và trả về chuỗi kết quả hành động (Thành công).
    Bước 5: Thêm trạng thái U vào tập visited để đánh dấu đã xử lý. Thực hiện trượt ô trống để tạo ra danh sách các trạng thái con V.
    Bước 6: Xét từng trạng thái con V: Nếu V chưa nằm trong tập visited, tiến hành tính giá trị ước lượng khoảng cách $h(V)$ của nó, sau đó đẩy V kèm điểm số này vào Priority Queue.Bước 7: Quay trở lại thực hiện tiếp Bước 3.

5. Thuật toán A* Search
    Bước 1: Khởi tạo một hàng đợi ưu tiên Priority Queue (Min-Heap) và một tập đóng quản lý các nút đã tối ưu closed_set = set().
    Bước 2: Tính toán điểm tổng quát ban đầu cho trạng thái gốc: $f(start) = g(start) + h(start) = 0 + Manhattan(start)$. Đẩy trạng thái gốc vào Heap.
    Bước 3: Nếu Heap rỗng, thuật toán kết thúc và báo Thất bại. Ngược lại, trích xuất trạng thái có tổng chi phí $f(n)$ thấp nhất ra khỏi Heap, gọi là nút U.
    Bước 4: Nếu U chính là trạng thái đích, thuật toán dừng lại, xuất ra chuỗi đường đi tối ưu ngắn nhất (Thành công).
    Bước 5: Đưa nút U vào tập closed_set. Thực hiện di chuyển ô trống để tạo ra danh sách các trạng thái con V.
    Bước 6: Xét từng trạng thái con V vừa sinh ra:Nếu V đã nằm trong tập closed_set, bỏ qua không xử lý.Tính toán chi phí đường đi thực tế mới: $g(V) = g(U) + 1$.Tính toán khoảng cách ước lượng còn lại: $h(V) = Manhattan(V)$.Tính toán tổng điểm: $f(V) = g(V) + h(V)$.Nếu V chưa từng có tên trong Heap, hoặc đường đi mới này giúp tối ưu chi phí hơn giá trị cũ từng lưu trước đó, tiến hành thêm hoặc cập nhật trạng thái V vào Heap với điểm số $f(V)$ mới.
    Bước 7: Quay trở lại thực hiện tiếp Bước 3.

6. Thuật toán IDA* (Iterative Deepening A*)
        Bước 1: Tính toán giá trị Heuristic ban đầu của trạng thái gốc: ngưỡng = Manhattan(start_state).
        Bước 2: Kích hoạt một chu kỳ chạy thuật toán tìm kiếm theo chiều sâu (DFS) cải tiến, xuất phát từ trạng thái gốc với chiếc "khung" giới hạn chi phí tổng quát $f(n) = g(n) + h(n)$ không được vượt quá ngưỡng hiện tại.
        Bước 3: Trong quá trình DFS duyệt nhánh, tính toán điểm $f$ của nút con $V$ vừa sinh ra: $f(V) = g(V) + h(V)$.Nếu $V$ trùng khớp với trạng thái đích $\rightarrow$ Lập tức dừng toàn bộ chương trình và báo Thành công.Nếu điểm $f(V) > ngưỡng$ $\rightarrow$ Nhánh này bị cắt tỉa ngay lập tức (thuật toán không đi sâu xuống tiếp mà thực hiện Quay lui (Backtrack) về nút cha), đồng thời ghi nhận lại giá trị $f(V)$ này vào danh sách các điểm bị vượt ngưỡng.
        Bước 4: Nếu chu kỳ DFS kết thúc mà không tìm thấy đích, tiến hành tìm giá trị $f$ nhỏ nhất trong số các nút đã từng bị cắt tỉa ở Bước 3.
        Bước 5: Cập nhật lại giới hạn tầm nhìn cho chu kỳ kế tiếp: Gán ngưỡng bằng giá trị nhỏ nhất vừa tìm được ở Bước 4.Bước 6: Giải phóng bộ nhớ RAM để xóa     sạch lịch sử duyệt của vòng cũ, sau đó quay trở lại thực hiện tiếp Bước 2.

NHÓM III: TÌM KIẾM CỤC BỘ (LOCAL SEARCH)

7. Thuật toán Hill Climbing (Leo đồi dốc nhất)
    Bước 1: Gán cấu hình bàn cờ ban đầu làm trạng thái hiện tại, tính toán điểm lỗi Heuristic (Khoảng cách Manhattan) của nó.
    Bước 2: Từ trạng thái hiện tại, sinh ra đồng loạt tất cả các trạng thái con kế cận hợp lệ bằng cách dịch chuyển ô trống (tối đa 4 hướng).
    Bước 3: Đánh giá điểm Manhattan cho toàn bộ các trạng thái con vừa sinh ra, tìm và lọc chọn ra duy nhất nút con tối ưu nhất (có điểm số nhỏ nhất - ít lỗi nhất).
    Bước 4: Thực hiện so sánh điểm số: Nếu nút con tối ưu nhất này có điểm chất lượng tốt hơn (nhỏ hơn) so với trạng thái cha hiện tại, gán trạng thái hiện tại bằng nút con này.
    Bước 5: Đánh giá điều kiện dừng: Nếu không có nút con nào đạt điểm tốt hơn trạng thái hiện tại, thuật toán lập tức dừng lại. Lúc này, nếu trạng thái hiện tại trùng khớp với đích $\rightarrow$ Báo Thành công, ngược lại $\rightarrow$ Báo Thất bại (Thuật toán bị kẹt ở đỉnh cục bộ).
    Bước 6: Quay trở lại thực hiện tiếp Bước 2.

8. Thuật toán Local Beam Search (Tìm kiếm chùm cục bộ với K=3)
    Bước 1: Khởi tạo một "chùm" (Beam) chứa song song $K=3$ trạng thái (thường được chọn lọc từ các nút con tốt nhất sinh ra từ nút gốc).
    Bước 2: Quét qua toàn bộ các trạng thái đang nằm trong chùm hiện tại. Nếu phát hiện có bất kỳ trạng thái nào trùng khớp với đích, dừng thuật toán và báo Thành công.
    Bước 3: Thực hiện mở rộng đồng loạt tất cả các hướng đi có thể của cả 3 trạng thái trong chùm để tạo ra một danh sách tổng hợp chứa tất cả các trạng thái con.
    Bước 4: Tính toán giá trị lỗi Heuristic (Khoảng cách Manhattan) cho từng trạng thái con nằm trong danh sách tổng hợp đó.
    Bước 5: Tiến hành sắp xếp danh sách tổng hợp theo thứ tự điểm số từ nhỏ đến lớn (từ tốt đến xấu) và chỉ giữ lại đúng 3 trạng thái con có điểm số tốt nhất để làm chùm mới cho vòng lặp tiếp theo; xóa bỏ hoàn toàn tất cả các trạng thái con còn lại.
    Bước 6: Đánh giá điều kiện kẹt: Nếu chùm mới được chọn không có nút nào cải thiện điểm tốt hơn so với chùm cũ, thuật toán dừng lại báo kẹt cực trị cục bộ. Ngược lại, lấy chùm mới thay thế chùm cũ và quay về Bước 2.

9. Thuật toán Steepest Ascent Hill Climbing (Leo đồi dốc nhất)
    Bước 1: Thiết lập cấu hình bàn cờ ban đầu làm trạng thái hiện tại (current_state) và tính toán điểm lỗi Heuristic (Khoảng cách Manhattan) của nó.
    Bước 2: Từ current_state, trượt ô trống (số 0) theo tất cả các hướng hợp lệ để sinh ra đồng loạt toàn bộ các trạng thái con kế cận (tối đa 4 hướng).
    Bước 3: Đánh giá và tính toán điểm khoảng cách Manhattan cho tất cả các trạng thái con vừa được sinh ra ở Bước 2.
    Bước 4: Lọc chọn ra duy nhất một trạng thái con có bước cải tiến mạnh mẽ nhất – tức là nút con sở hữu điểm số Manhattan nhỏ nhất (có "độ dốc" tối ưu nhất).
    Bước 5: Thực hiện so sánh: Nếu điểm Manhattan của nút con tốt nhất này nhỏ hơn điểm Manhattan của nút cha hiện tại, tiến hành gán current_state bằng nút con tối ưu này để bước tiếp.
    Bước 6: Kiểm tra điều kiện kẹt đồi: Nếu nút con tốt nhất cũng không thể cải thiện điểm số tốt hơn nút cha hiện tại $\rightarrow$ Thuật toán dừng lại ngay lập tức.Nếu lúc dừng, current_state trùng khớp với trạng thái đích $\rightarrow$ Báo Thành công.Nếu chưa đạt đích $\rightarrow$ Báo Thất bại (Thuật toán đã rơi vào bẫy kẹt ở đỉnh cục bộ).
    Bước 7: Quay trở lại thực hiện tiếp Bước 2.

10. Thuật toán Stochastic Hill Climbing (Leo đồi ngẫu nhiên)
    Bước 1: Gán trạng thái bàn cờ ban đầu làm trạng thái hiện tại (current_state), tính toán khoảng cách Manhattan của nó.
    Bước 2: Di chuyển ô trống xung quanh vị trí hiện tại để phát triển toàn bộ các trạng thái con kề cận.
    Bước 3: Tính toán điểm Heuristic cho các nút con và tiến hành lọc: Chỉ giữ lại những nút con nào có điểm số tốt hơn (nhỏ hơn) so với điểm của nút cha current_state. Các nút bằng điểm hoặc tệ hơn sẽ bị loại bỏ hoàn toàn.
    Bước 4: Kiểm tra danh sách lọc được ở Bước 3: Nếu danh sách này trống rỗng (không có nút con nào tốt hơn cha) $\rightarrow$ Thuật toán dừng lại và kết luận bị kẹt đỉnh đồi cục bộ.
    Bước 5: Nếu danh sách có phần tử, thuật toán tiến hành lựa chọn ngẫu nhiên một nút con bất kỳ nằm trong danh sách các nút tốt hơn đó (thay vì chọn nút tốt nhất hay nút đầu tiên).
    Bước 6: Gán current_state bằng nút con vừa bốc thăm ngẫu nhiên được ở Bước 5.Bước 7: Kiểm tra nếu current_state đạt đích $\rightarrow$ Báo Thành công. Ngược lại, quay trở lại thực hiện tiếp Bước 2.

11. Thuật toán Random Restart Hill Climbing (Leo đồi khởi động lại ngẫu nhiên)
    Bước 1: Gán cấu hình bàn cờ ban đầu từ giao diện làm trạng thái xuất phát hiện tại (current_state) và thiết lập một giới hạn số lần khởi động lại tối đa (ví dụ: max_restarts = 50) để tránh vòng lặp vô hạn.
    Bước 2: Tính toán điểm lỗi Heuristic (Khoảng cách Manhattan) cho current_state.
    Bước 3 (Giai đoạn Leo đồi dốc nhất - Steepest Ascent):
        Bước 3.1: Từ current_state, di chuyển ô trống (số 0) theo các hướng hợp lệ để sinh ra đồng loạt toàn bộ các trạng thái con kế cận (tối đa 4 hướng).
        Bước 3.2: Đánh giá điểm Manhattan cho tất cả các trạng thái con vừa sinh ra và lọc chọn ra duy nhất một nút con tối ưu nhất (có điểm số nhỏ nhất).
        Bước 3.3: So sánh điểm số: Nếu nút con tốt nhất này có điểm Manhattan nhỏ hơn current_state, tiến hành gán current_state bằng nút con này và quay lại Bước 3.1 để tiếp tục bò lên đỉnh.
    Bước 4 (Đánh giá kết quả leo đồi): Khi giai đoạn ở Bước 3 dừng lại (không còn nút con nào tốt hơn cha), hệ thống sẽ tiến hành kiểm tra:Nếu current_state trùng khớp hoàn toàn với trạng thái đích $\rightarrow$ Thuật toán dừng lại, trích xuất toàn bộ chuỗi hành động tích lũy và báo Thành công.Nếu current_state chưa đạt đích (tức là thuật toán đã bị kẹt ở một đỉnh cục bộ/cao nguyên) $\rightarrow$ Chuyển sang Bước 5.
    Bước 5 (Kích hoạt Đột biến / Khởi động lại): * Kiểm tra số lần đã khởi động lại, nếu vượt quá giới hạn cho phép thì dừng và báo Thất bại.Ngược lại, thuật toán tiến hành hành động Restart: Tự động tráo đổi ngẫu nhiên các ô số của bàn cờ hiện tại một số bước để tạo ra một trạng thái xuất phát hoàn toàn mới (khác hoàn toàn vị trí bị kẹt).Gán current_state bằng trạng thái mới sinh ra này.
    Bước 6: Tăng biến đếm số lần restart lên 1 đơn vị, sau đó quay trở lại Bước 2 để thực hiện một chu trình leo đồi hoàn toàn mới từ vị trí mới.

NHÓM IV: KHÔNG GIAN NIỆM TIN (BELIEF-STATE SEARCH)

12. Thuật toán Belief Search
    Bước 1: Đọc trạng thái từ giao diện, dịch chuyển thử một bước hợp lệ để tạo ra một cấu hình nhiễu chắc chắn giải được. Gom hai trạng thái này lại thành một tập hợp gọi là Trạng thái Niềm tin ban đầu (Initial Belief State).
    Bước 2: Khởi tạo một hàng đợi Queue (FIFO) và đẩy tập hợp Initial Belief State vào. Đánh dấu tập này vào danh sách đã duyệt visited.
    Bước 3: Nếu Queue rỗng, dừng và báo Thất bại. Ngược lại, lấy tập niềm tin hiện tại ra khỏi đầu hàng đợi Queue.
    Bước 4: Kiểm tra điều kiện đích đặc biệt: Quét qua toàn bộ các cấu hình bàn cờ giả định đang có trong tập niềm tin hiện tại. Nếu tất cả các trường hợp giả định này đều đã đồng loạt trùng khớp với trạng thái đích thực tế $\rightarrow$ Thuật toán dừng lại và báo Thành công.
    Bước 5: Thử áp dụng đồng loạt cùng một hành động dịch chuyển (Trái hoặc Phải hoặc Lên hoặc Xuống) cho tất cả các trạng thái bên trong tập niềm tin hiện tại để tạo ra tập niềm tin con mới.
    Bước 6: Nếu tập niềm tin con mới sinh ra chưa từng xuất hiện trong tập visited, tiến hành thêm nó vào tập visited đồng thời đẩy nó vào cuối hàng đợi Queue.
    Bước 7: Quay trở lại thực hiện tiếp Bước 3.

13. Thuật toán Belief Goal
    Bước 1: Khởi tạo Trạng thái Niềm tin ban đầu (chứa trạng thái thực tế và trạng thái nhiễu giả định) tương tự như Bước 1 của thuật toán Belief Search.
    Bước 2: Tạo một hàng đợi ưu tiên Priority Queue (Min-Heap). Điểm ưu tiên để sắp xếp một nút niềm tin được tính bằng: Số lượng trạng thái giả định còn lại trong tập (độ bất định) + Tổng số bước đi thực tế.
    Bước 3: Trích xuất tập niềm tin có tổng điểm số ưu tiên thấp nhất (tập có độ mơ hồ thấp nhất và tốn ít chi phí nhất) ra khỏi Heap.
    Bước 4: Kiểm tra đích: Nếu toàn bộ các phần tử giả định trong tập niềm tin này đều đã hội tụ hoàn toàn về trạng thái đích $\rightarrow$ Dừng thuật toán và xuất lời giải (Thành công).
    Bước 5: Dịch chuyển đồng loạt các ô số trong tập niềm tin hiện tại theo 4 hướng để sinh ra các tập niềm tin con mới.
    Bước 6: Tính toán điểm ưu tiên mới cho các tập con chưa duyệt và nạp chúng vào Heap để định hướng thuật toán liên tục thu hẹp kích thước tập niềm tin về mức tối thiểu (hội tụ về 1 bàn cờ duy nhất).
    Bước 7: Quay trở lại thực hiện tiếp Bước 3.

NHÓM V: THỎA MÃN RÀNG BUỘC CSP

14. Thuật toán Backtracking (Quay lui)
    Bước 1: Kiểm tra cấu hình bàn cờ hiện tại: Nếu đã trùng khớp hoàn toàn với trạng thái đích, lập tức trả về chuỗi hành động và báo Thành công.
    Bước 2: Xác định vị trí ô trống (số 0) và lấy ra danh sách các hướng di chuyển hợp lệ xung quanh chưa được thử nghiệm tại bước này.
    Bước 3: Thử chọn một hành động gán nhãn (ví dụ: Lên), thực hiện dịch chuyển ô trống để sinh ra cấu hình bàn cờ mới.
    Bước 4: Kiểm tra ràng buộc hợp lệ: Nếu trạng thái mới sinh ra không vi phạm ràng buộc (không bị trùng lặp lại các cấu hình đã đi qua trong lịch sử của nhánh tìm kiếm hiện tại), thuật toán tiến hành gọi đệ quy sâu xuống để tiếp tục giải từ trạng thái mới này.
    Bước 5: Nếu lệnh gọi đệ quy ở bước dưới trả về kết quả thành công, tiếp tục truyền chuỗi hành động lên nút cha và kết thúc thuật toán.
    Bước 6: Nếu lệnh gọi đệ quy trả về thất bại (gặp nhánh cụt), thuật toán thực hiện Quay lui (Backtrack) bằng cách hoàn tác lại bước đi vừa rồi (trượt ô số ngược trở lại vị trí cũ) và quay lại Bước 3 để thử nghiệm hướng tiếp theo.
    Bước 7: Nếu đã thử nghiệm hết toàn bộ các hướng di chuyển tại nút hiện tại mà đều dẫn đến thất bại, trả về giá trị lỗi (None).

15. Thuật toán Forward Checking (Kiểm tra phía trước)
    Bước 1: Dựa trên khung thuật toán quay lui Backtracking, tiến hành thử nghiệm gán một bước đi dịch chuyển ô trống tiếp theo cho bàn cờ.
    Bước 2: Ngay sau khi thực hiện dịch chuyển, thuật toán tiến hành kỹ thuật "nhìn trước" bằng cách quét qua miền giá trị hành động khả dĩ của bước tiếp theo ngay sau nó.
    Bước 3: Tiến hành lọc sạch và loại bỏ tất cả các hướng đi ở bước kế tiếp nếu hướng đi đó vi phạm ràng buộc (ví dụ: dẫn bàn cờ quay ngược lại trạng thái vừa xét hoặc đi vào thế kẹt cứng).
    Bước 4: Đánh giá điều kiện cắt tỉa: Nếu phát hiện miền giá trị của bước đi kế tiếp bị trống rỗng (bằng 0 - không còn bất kỳ hướng nào đi tiếp được nữa), thuật toán kết luận nhánh này chắc chắn bế tắc.
    Bước 5: Thực hiện cắt tỉa nhánh sớm ngay lập tức mà không cần tốn tài nguyên đệ quy sâu xuống bên dưới, kích hoạt quay lui để chọn hướng đi khác nhằm tiết kiệm bộ nhớ.

16. Thuật toán AC3 (Arc Consistency)
    Bước 1: Khởi tạo một hàng đợi cung ràng buộc Queue_Arcs chứa tất cả các cặp mối quan hệ ràng buộc bước đi kề cạnh nhau trên không gian trạng thái bàn cờ.
    Bước 2: Lấy một cặp cung ràng buộc $(X_i, X_j)$ ra khỏi hàng đợi để phân tích tính nhất quán.
    Bước 3: Duyệt qua các hướng đi trong miền giá trị của bước $X_i$. Nếu có một hướng đi của $X_i$ khiến cho bước $X_j$ không thể tìm được bất kỳ hướng đi nào tiếp theo hợp lệ, tiến hành xóa bỏ hướng đi lỗi đó ra khỏi miền giá trị của $X_i$.
    Bước 4: Kiểm tra biến động cung: Nếu miền giá trị của $X_i$ bị thay đổi (bị thu hẹp), thực hiện đẩy ngược lại tất cả các cung lân cận có liên quan đến $X_i$ vào lại hàng đợi Queue_Arcs để cập nhật dây chuyền cho toàn bộ hệ thống.
    Bước 5: Lặp lại quy trình cho đến khi hàng đợi cung rỗng, bảo đảm miền giá trị của mọi bước đi đều hoàn toàn nhất quán trước khi chuyển giao cho bộ lọc tìm kiếm thực tế.
