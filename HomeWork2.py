str1=str(input())
print(str1)
k=0
for elem in str1:
    if elem.isdigit():
        k += int(elem)
        print(elem)
print("k=" ,k)