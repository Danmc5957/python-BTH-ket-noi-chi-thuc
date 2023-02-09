s=1
count=0
while s <= 100:
    if s % 5 == 0 or s % 3 == 1:
        count+=1
    s+=1
print("Có %d số thỏa mãn điều kiện" % count)