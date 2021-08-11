n=int(input("Input a number "))
d = dict()

for x in range(n):
    d[x] = int(input())

print(d) 
del d[2]
print("The dictionary after removing third key",d)

