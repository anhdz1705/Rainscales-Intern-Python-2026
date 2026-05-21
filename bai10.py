# Viết chương trình nhập vào một số có 3 chữ số, xuất ra dòng chữ mô tả giá trị con số đó.
#  Ví dụ: nhập 123 → xuất: "một trăm hai mươi ba"

num = int(input("Nhap so 3 chu so: "))
so = ["","mot", " hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

tram = num // 100
chuc = (num % 100) // 10
dv = num % 10

kq = so[tram] + " tram"
if chuc == 0 and dv != 0:
    kq += " le " + so[dv]
elif chuc == 1:
    kq += " muoi "
    if dv == 5:
        kq += "lam"    
    else:
        kq += so[dv]    
elif chuc > 1:
    kq += " " + so[chuc] + " muoi "
    if dv != 0:
        if dv == 1:
            kq += "mốt" 
        elif dv == 5:
            kq += "lăm" 
        else:
            kq += so[dv]
print(kq)