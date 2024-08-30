def zarb(n):
    """
    it is for *
    """
    
    for i in range(1, n + 1):#i
        for j in range(1, n + 1):#j
            print(i * j, end="     ")#چاپ کردن ضرب اعداد با یک فاصله
        print()  # یک خط خالی برای جدا کردن سطرها

n = int(input("Your number: "))#وارد کردن عدد

zarb(n)#صدا زدن تابع
