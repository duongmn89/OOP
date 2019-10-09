Tạo 1 class SinhVien gồm các thuộc tính: mã, họ, đệm, tên, điểm, giới tính và
các phương thức thực hiện:
* Phương thức khởi tạo SinhVien () tạo 1 SinhVien trống
* Phương thức nhập nhap() 1 SinhVien từ bàn phím
* Phương thức hiển thị hienthi() 1 SinhVien ra màn hình
* Phương thức đọc docfile(ifstream) 1 SinhVien từ file sinhvien.dat
* Phương thức ghi ghiFile(ofstream) 1 SinhVien ra file sinhvien.dat
Lưu ý: tự xác định cấu trúc file sinhvien.dat
* Chồng toán tử nhập1 SinhVien từ bàn phím
* Chồng toán tử hiển thị 1 SinhVien ra màn hình
* Phương thức sosanhTen(SinhVien sv) so sánh 2 họ tên với nhau (trả về 0 nếu
bằng nhau, -1 nếu sv nhỏ hơn, 1 nếu sv lớn hơn)

Tạo class DSSinhVien sử dụng class SinhVien ở , gồm các thuộc tính số
sinh viên, mảng SinhVien. Viết các phương thức thực hiện:
* Phương thức khởi tạo DSSinhVien() khởi tạo 1 danh sách rỗng
* Phương thức timkiem(ID) trả về chỉ số sinh mảng của sinh viên có mã tương
ứng
* Phương thức sua(SinhVien sv) sửa sinh viên có ID là sv.ID thành dữ liệu như
sv (dùng b để tìm chỉ số mảng)
* Phương thức xoa(int id) để xoá sinh viên có ID tương ứng (dung b để tìm chỉ
số mảng)
* Phương thức them(SinhVien sv) để them 1 sinh viên vào danh sách
* Phương thức sapxepHoTen() để sắp xếp lại sinh viên theo họ tên ABC
* Phương thức Lưu danh sách sinhvien vào file sinhvien.dat
* Phương thức Đọc danh sách sinh viên từ file sinhvien.dat
