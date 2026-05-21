# Viết chương trình nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự.

str = input("Nhap chuoi: ").lower()
count = {}
for i in str:
    if i != " ":
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
print(count)