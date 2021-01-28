arr=[]
n=int(input("no of items: "))
for i in range(0,n):
    arr.append([])
    name = input("name: ")
    score = float(input("score: "))
    arr[i].append(score)
    arr[i].append(name)
minimum_val=min(arr)
x=arr[arr.index(minimum_val)][0]
loop=True
while loop:
    if arr==[]:
        break            
    elif arr[arr.index(min(arr))][0]==x:
        arr.remove(min(arr))
    else:
        break
minimum_val2=min(arr)
y=arr[arr.index(minimum_val2)][0]
while loop:
    if arr==[]:
        break
    elif arr[arr.index(min(arr))][0]==y:
        print (arr[arr.index(min(arr))][1])
        arr.remove(min(arr))
    else:
        break
