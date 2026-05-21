# Viết chương trình tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi.

str = input("Nhap chuoi: ")
max_char = str[0]
for i in str:
    if str.count(i) > str.count(max_char):
        max_char = i
print(max_char)