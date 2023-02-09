n = int(input("Nhập số tự nhiên: "))

s=0
for i in range(n+1):
    s=s+1/i
print("S=",round(s, 2))