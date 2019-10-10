Class TracNghiem có thuộc tính là: câu hỏi, 4 phương án trả lời, đáp án, trả lời
của người chơi. 
Class DSTracNghiem có thuộc tính là:: số câu hỏi, mảng TracNghiem, số câu trả lời
đúng.
* Class DSTracNghiem: lấy câu hỏi từ sqlalchemy . cấu trúc DB tự nghĩ.  Phương thức kiemtra() sử dụng hàm static TracNghiem::kiemtra() để kiểm tra người chơi với từng câu hỏi trong có đúng không và đếm số câu trả lời đúng.
* Class DSTracNghiem: Phương thức phanloai(): nếu số câu trả lời đúng >80%:
xuat sac;
  - nếu số câu trả lời đúng >=60%: “Rat tot”
  - nếu số câu trả lời đúng <60% : “Va qua roi”.


Tự thiết kế kịch bản sử dụng cho người dùng. 
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
2

Kiem tra xong.
Rat tot, tra loi dung 69 %

