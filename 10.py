def find(n, l, r):
    """
    it is for find
    """
    if l * (r - l + 1) >= n:#ساخت شرط 
        return 1#چاپ 1
    
    for days in range(2, n + 1):#ساخت حلقه روز از 2 تا ان
        hours = days * (l + r) // 2#ساخت متغیر ساخت
        if hours >= n:#ساخت شرط
            return days#برگرداند متغیر روز ها
    
    return -1#برگرداندن 1 منفی

n = int(input("Enter: "))#گرفتن عدد از کاربر
l, r = map(int, input("Enter: ").split())#تعریف ال و ار که از کاربر میگیریم در یک از اسپلیت و مپ استفاده میکنیم برای اینکه هر دو متغیر را در یک خط از اربر بگیریم

result = find(n, l, r)#تابع 
print(result)#چاپ تابع
