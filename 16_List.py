# List Program
list = [1,2,"Hello",3.4]

list.append(2000)
print("The Append list is ",list)

list.insert(2,6)
print("The Insert value in list is ",list)

list1 = [10,20,30,40,50,50]
print("The Sum of list is ", sum(list1))

print("The Count element of list is ", list1.count(50))

print("The Length of list is ", len(list1))

list3 = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print("In the list index which element is present ",list3.index(2)) 

print("The List become find index and then add the element in that index element : ",list3.index(1,2))