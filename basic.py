# noc = input("Enter the name of the customer : ")
# pn  = input("Enter the name of the product : ")
# pq  = int(input("Enter the number of the product quantity :"))
# pr  = int(input("Enter the value of the product price : "))
# #now from here calculation part will come
# amt = pq*pr
# gst = amt *18/100
# total = amt+gst
# #to save in a file
# pq1 = str (pq)
# pr1 = str (pr)
# a1  = str (amt)
# gst1 = str (gst)
# ta1 = str (total)
# f1 = open ("C:/Users/Admin/Desktop/cstrec/"+noc+".txt","w")


# Input = [12,35,9,56,24]
def swaplist(newlist):
    size=len(newlist)

    #swapping
    temp=newlist[0]         # storing the value of 0 indexing in temp variable.
    newlist[0]=newlist[size-1]  #storing the last indexing value at 0 indexing
    newlist[size-1]=temp    #

    return newlist
newlist=[12,35,9,56,24]
print (swaplist(newlist))


