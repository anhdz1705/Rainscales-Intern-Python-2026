# Viết chương trình chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa.
str = input("Nhap chuoi: ").split()

for i in range(len(str)):
    str[i] = str[i][0].upper() + str[i][1:]
print(" ".join(str))
