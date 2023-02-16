n = int(input("Nhập số tự nhiên: "))

s=1
for i in range(2, n+1):
    s=s+1/i
print("S=",round(s, 2))