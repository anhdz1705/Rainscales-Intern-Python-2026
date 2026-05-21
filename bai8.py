# Viết chương trình đổi chữ xen kẽ: một chữ hoa và một chữ thường.
#  Ví dụ: nhập "ABCDEfgh" → xuất: "AbCdEfGh"
str = input("Nhap chuoi: ")
kq = ""

for i in range(len(str)):
    if i % 2 ==0:
        kq += str[i].upper()
    else:
        kq += str[i].lower()
print(kq)