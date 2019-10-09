Class TracNghiem có thuộc tính là: câu hỏi, 4 phương án trả lời, đáp án, trả lời
của người chơi
Class DSTracNghiem có thuộc tính là:: số câu hỏi, mảng TracNghiem, số câu trả lời
đúng. Viết các phương thức thực hiện:
* Class TracNghiem: phương thức đọc doc() 1 câu hỏi từ bcvt.dat vào 1 đối
* Class TracNghiem: phương thức hiển thị hienthi() 1 câu hỏi
* Class TracNghiem: Phương thức kiemtra() kiểm tra trả lời của người chơi có
giống với đáp án không?
* Class DSTracNghiem: phương thức đọc doc() 1 danh sách câu hỏi từ bcvt.dat
* Class DSTracNghiem: Phương thức kiemtra() sử dụng hàm
TracNghiem::kiemtra() để kiểm tra người chơi với từng câu hỏi trong danh
sách có đúng không và đếm số câu trả lời đúng.
* Class DSTracNghiem: Phương thức phanloai(): nếu số câu trả lời đúng >80%:
xuat sac;
  - nếu số câu trả lời đúng >=60%: “Rat tot”
  - nếu số câu trả lời đúng <60% : “Can phai tim hieu them ve truong”.

file bcvt.data: dòng đầu ghi số câu hỏi; dòng tiếp ghi nội dung câu hỏi đầu; 4 dòng
tiếp ghi 4 phương án trả lời; dòng tiếp ghi STT của đáp án đúng; tương tự với các câu
còn lại. 


Ví dụ:

Khoa CNTT cua PTIT hoc may nam?

* 3 nam 
* 4 nam
* 5 nam
* 4.5 nam

4

Ten tieng Viet cua PTIT la gi?
* Hoc vien Cong nghe Buu chinh Vien thong
* Truong Cong nghe Buu chinh Vien thong
* Hoc vien Buu chinh
* Hoc vien Buu chinh Vien thong

1

PTIT truc thuoc bo nao?
* Bo Giao duc va Dao tao
* Bo Thong tin va Truyen thong
* Bo Khoa hoc va Cong nghe
* Ca 3 bo tren 
