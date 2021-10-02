#linear Queue 
#linear Queue uses FIFO(first in first out )method


def enqueue(a): # for adding element in list
    element = int(input("Enter a number"))
    a.append(element)


def dequeue(a): # for poping element in list
    if len(a) == 0:
        print("Queue is underflow")
    else:
        element = a.pop(0)
        print("dequeue number is :", element)


def peak(a): # for displaying the peak element in list
    if len(a) == 0:
        print("Queue is underflow")
    else:
        element = a[0]
        print("Peak element is :", element)


def display(a): # for displaying whole list 
    if len(a) == 0:
        print("Queue is underflow")
    else:
        print(a)


a = []
while True:
    choice = int(input(
        "press 1 for enqueue \npress 2 for dequeue\npress 3 for peak element\npress 4 for display list\npress any other keys exit ")) # making choices for calling the functions
    if choice == 1:
        enqueue(a)
    elif choice == 2:
        dequeue(a)
    elif choice == 3:
        peak(a)
    elif choice == 4:
        display(a)
    else: 
        break # for exit the program
