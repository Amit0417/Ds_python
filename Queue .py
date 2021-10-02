def enqueue(a):
    element = int(input("Enter a number"))
    a.append(element)


def dequeue(a):
    if len(a) == 0:
        print("Queue is underflow")
    else:
        element = a.pop(0)
        print("dequeue number is :", element)


def peak(a):
    if len(a) == 0:
        print("Queue is underflow")
    else:
        element = a[0]
        print("Peak element is :", element)


def display(a):
    if len(a) == 0:
        print("Queue is underflow")
    else:
        print(a)


a = []
while True:
    choice = int(input(
        "press 1 for enqueue \npress 2 for dequeue\npress 3 for peak element\npress 4 for display list\npress any other keys exit "))
    if choice == 1:
        enqueue(a)
    elif choice == 2:
        dequeue(a)
    elif choice == 3:
        peak(a)
    elif choice == 4:
        display(a)
    else:
        break
