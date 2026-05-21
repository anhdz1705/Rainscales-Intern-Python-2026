# Viết chương trình đảo ngược thứ tự các từ có trong chuỗi.
#  Ví dụ: nhập "lap trinh bang ngon ngu python" → xuất: "python ngu ngon bang trinh lap"

str = input("Nhap chuoi: ").split()
reversed = str[::-1]
print(" ".join(reversed))

