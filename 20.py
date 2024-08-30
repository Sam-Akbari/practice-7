def happy_pairs(n, m, p):
    """
    it is for pressents
    """
    #ایجاد حلقه و متغیر ساختن
    total_guests = n + m + p
    if n == 0 or m == 0:
        happy_pairs = p
    else:
        happy_pairs = (n + m) // 2
    return happy_pairs#برگرداندن

# مثال‌های ورودی
t = int(input())
for _ in range(t):#حلقه
    n, m, p = map(int, input().split())
    result = happy_pairs(n, m, p)
    print(result)#چاپ مقدار و تمام
