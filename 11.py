def battery(k):
    """
    it is for time battery
    """
    if k <= 100 and k >= 1:#اگر کی بین 1 تا 100 بود چون باتری تا 100 درصد است
        time = sum(range(1,k+1))#یک متغیر تایم میسازیم
        return time#بعد این متغیر را برمیگردانیم
k = int(input("Nnmber(1 to 100): "))#حلا مقدار کی را از کاربر میگیریم
print(battery(k))#صدا کردن تابع