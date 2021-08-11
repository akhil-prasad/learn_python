l=[]
n=int(input("enter the size of the list: "))
for i in range (n) :
    a=int(input())
    l.append(a)
new_list=[]

for i in l: 
    if i not in new_list: 
        new_list.append(i)

        
print(new_list)
        



    
