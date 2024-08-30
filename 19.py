def happy_pairs(n, m, p):
    """
    it is for dinner desk
    """
    # تعداد زوج‌های خوشحال برابر با جمع کف تقسیم بر 2 تعداد دانشجوها و اساتید است
    return (n // 2) + (m // 2) + (p // 2)

t = int(input("Enter: "))#گرفتن
#ایجاد حلقه
for _ in range(t):#
    n, m, p = map(int, input("Enter: ").split())#گرفتن
    result = happy_pairs(n, m, p)
    print(result)#چاپ و تمام
