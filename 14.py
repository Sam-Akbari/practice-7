def find_max_number():
    """
    it is rot find big number or max
    """
    n = int(input("n: "))#گرفتن از کاربر ان
    numbers = list(map(int, input("a: ").split()))#گرفتن از کاربر ای

    max_number = max(numbers)#پیدا کردن بزرگترین عدد

    print(max_number)#چاپ بزرگترین عدد

find_max_number()#صدا زدن تابع
