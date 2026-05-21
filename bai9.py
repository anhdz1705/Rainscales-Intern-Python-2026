# Viết chương trình nhập vào một chuỗi ký tự, kiểm tra xem chuỗi đó có đối xứng không.
# Chuỗi đối xứng là chuỗi mà khi viết ngược lại vẫn giống như ban đầu.
str = input("Nhap chuoi: ")
if str == str[::-1]:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")