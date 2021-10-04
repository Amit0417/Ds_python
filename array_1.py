from array import *
arr1 = array('i',[])
size = int(input("Enter the size of array: "))
for i in range(size):
    val = int (input("Enter the elements of array: "))
    arr1.append(val)
print(arr1)

def insert_element_specific_location(arr1,loc):
    if loc>=len(arr1):
        print("Array Out of Bound")
    else:
        val = int (input("Enter the value :"))
        arr1.insert(loc,val)
        
def remove_element_specific_location(arr1):
    val = int (input("Enter the index value :"))
    arr1.pop(val)

while True:
    choice = int (input("\n Enter 1 update element in specific location\n Enter 2 for remove element in specific location\n Enter 3 for Display the array\n Enter 4 for length of array\n Enter 5 for exit\n"))
    if choice == 1:
        loc = int(input("Enter the location index of element :"))
        insert_element_specific_location(arr1,loc)
    elif choice == 2:
        remove_element_specific_location(arr1)
    elif choice == 3:
        print(arr1)
    elif choice == 4:
        print("length of array :",len(arr1))
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")