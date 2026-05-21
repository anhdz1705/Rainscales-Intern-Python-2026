# Viết chương trình đổi các từ ở đầu câu sang chữ hoa và những từ không phải đầu câu sang chữ thường.
# Ví dụ: nGuYen vAN a → Nguyen Van A

str1 = input("Nhap chuoi: ").split()
kq = []
for i in range(len(str1)):
    kq.append(str1[i].capitalize())
print(" ".join(kq)) 
