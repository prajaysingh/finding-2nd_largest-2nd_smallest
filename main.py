num = [4,7,3,2,2,8,8,5,5,8]
newlist =[]
leng = len(num)
flag = False
for i in range(leng):
    for j in range (i+1,leng):
        if ((num[i]==num[j]) and (i==leng-2) and (j==leng-1)): #This condition is to test if the 2nd last item and last item is equal. This will avoid to miss appending of last item
            flag = True
            newlist.append(num[i])
            break
        elif (num[i]==num[j]): #If 2 items are equal we will break the inner loop and start comparing next item
            flag = True
            break
        else : #If 2 items are not equal, we will append the current item to new list
            flag = False

            
    if (flag == False):
        newlist.append(num[i])
print(newlist)
newlist.sort()
print(newlist)
len2= len(newlist)
print ("2nd Smallest item =", newlist[1])
print ("2nd Largest item =", newlist[len2-2])
    

