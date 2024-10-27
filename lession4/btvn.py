menu = {
    "DADDY": "0984037755",
    "MAMA": "0379948755" ,
    "Chi_HIEU": "0377116112", 
    "CHI_VAN" : "0989842032",
    "CHI_LAN" : "0239283933",
}
Tinh_nag = {
    "Show_menu": 1,
    "Search": 2,
    "So_luong_danh_ba": 3,
    "Kiem_tra_so_dt": 4,
}

# print(Tinh_nag)
# def Show_menu(Menu):
#     for ten, sdt in Menu.items():
#         print(f"{ten} - {sdt}")
        

# def Search(Nhaptennguoidung):
#     x = input("Nhập tên người muốn tìm : ")
#     for ten,sdt in Nhaptennguoidung.items():
#         if ten == x:
#             print(f"{x} có số điện thoại là : {sdt}")
#         if  x not in Nhaptennguoidung.items() :
#             print("Không tìm thấy số điện thoại")
# def So_luong_danh_ba(soluong):
#     print(f"Số lượng danh bạ là : {len(soluong)}")
# def Kiem_tra_so_dt(Kiemtra):
#     sdt = int(input("Nhập vào số điện thoại muốn kiểm tra :"))
#     for ten,sodienthoai in Kiemtra.items():
#         if sdt == sodienthoai:
#             return ten, sodienthoai
#         else:
#             return None, None
# while True:
#     y = int(input("Nhập vào tính năng từ 1 đến 5 :"))       
#     if y == 1:
#         Show_menu(menu)
#     if y == 2:
#         Search(menu)
#     if y == 3:
#         So_luong_danh_ba(menu)
#     if y == 4:
#         ten, sodienthoai = Kiem_tra_so_dt(menu)
#         if ten is not None:
#             print(f"{ten} có số điện thoại là {sodienthoai}")
#         else:
#             print("Không tìm thấy số điện thoại")
#     if y == 5:
#         print("Đã thoát danh bạ")
#         break
    


"""
Coding Convention -> Quy tắc chuẩn hoá code


1. Snake case
tất cả các chữ viết thường và cách nhau bằng dấu gạch dưới
Ví dụ: kiem_tra_so_dien_thoai
2. Camel Case
kiemTraSoDienThoai -> chữ đầu tiên viết thường và các chữ còn lại viết hoa
Ví dụ: KiemTraSoDienThoai
3. UPPERCASE
viết hoa tất cả các ký tự
KIEMTRASODIENTHOAI

ten bien và ten hàm 
Sử dụng snake_case

Khi chúng ta định nghĩa 1 hằng số -> Sử dụng UPPERCASE

2. Cách viết hàm và vòng lặp
Khi sử dụng hàm và vòng lặp các cậu 1 khoảng gọi space 4 <=> 4 dấu cách hoặc 1 nut tab
=> indent trong python


Ký tự xuống dòng: \n

"""


"""

append -> thêm vào cuối cùng
insert -> thêm vào 1 vị trí được chỉ định
remove -> xoá tất cả phần tử có giá trị được điền vào
pop -> xoá phần tử có vị trí được chỉ định -> nếu không chỉ định vị trí -> xoá phần tử cuối cùng



"""



tuple_2 = (
    ("Ha Noi", 100000),
    ("Ha Giang", 200000),
    ("Ha Nam", 300000),
    ("Ha Tinh", 400000),
    ("Ha Dong", 500000),
    ("Ha Tay", 600000),
    ("Hai Phong", 700000),
    ("Hai Duong", 800000),
    ("Hai Phong", 900000),
)

"""
1. hiển thị thông tin các dịa phương
Tỉnh Hà Nội - Mã vùng 100000
Tình hà giang - Mã vùng 200000


2. Đếm số lượng mã vùng có trong CSDL

3. Kiểm tra mã vùng tồn tại hay không
+ Nhập tên tỉnh
-> Nếu có thì in: Tỉnh Hà Nội - Mã vùng 100000
-> Nếu không thì in: Không tìm thay trong CSDL

"""





