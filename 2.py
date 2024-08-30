x1 = int(input("x1: "))#گرفتن
x2 = int(input("x2: "))#گرفتن
y1 = int(input("y1: "))#گرفتن
y2 = int(input("y2: "))#گرفتن
def room(x1,y1,x2,y2):
    """
    for rooms
    """
    if x1 == x2:
        print("Horizontal")
    if y1 == y2:
        print("Vertical")
    else:
        print("Try again")
room(x1,y1,x2,y2)#صدا زدن تابع