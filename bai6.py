# Viết hàm cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên.
def cat_chuoi(str):
    ten = str[-1]
    ho_lot = " ".join(str[:-1])
    return ten, ho_lot
str = input("Nhap ho va ten: ").split()
ten, ho_lot = cat_chuoi(str)
print("Ho lot: ", ho_lot)
print("Ten: ", ten)