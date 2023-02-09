year = int(input("Nhập năm:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Năm", year, "là năm nhuận")
else:
    print("Năm", year, "không là năm nhuận")
