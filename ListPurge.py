#purge list function create an empty list and add only one of each element to the list

#def purge2(alist):
alist = [1,2,3,3,3,3,4]
blist = []
for i in alist:
    if i not in blist:
        blist.append(i)
    
print(blist)
#purge2([1,2,3,3,3,3,4])
blist = []
for i in range(len(alist)):
    if alist[i] not in blist:
        blist.append(alist[i])
    
#print(blist)
