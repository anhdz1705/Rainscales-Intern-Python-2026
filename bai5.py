# Viết hàm kiểm tra xem trong chuỗi có ký tự số hay không. 
# Nếu có, tách các số đó ra thành một mảng riêng.

str = input("Nhap chuoi: ")
num = []
for i in str:
    if i.isdigit():
        num.append(i)
print(num)