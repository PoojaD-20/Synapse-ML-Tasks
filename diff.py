lst=['0001','0011','0101','1011','1101','1111']
new_lst=[]
for i in lst:
    new_lst.append(int(i,2))
print("New List: ",new_lst)
diff = 10000
n=len(new_lst) 
for i in range(n-1):
        if new_lst[i+1] - new_lst[i] < diff:
            diff=new_lst[i+1] - new_lst[i]
            arr=[new_lst[i],new_lst[i+1]]
print(arr)            
print(diff)    