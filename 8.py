def find(n):
    """
    search fanction
    """
    divisors_count = 0#مقدار اولیه صفر است و باید باشد
    divisors_sum = 0#مقدار اولیه صفر است و باید باشد

    for i in range(1, n + 1):
        divisors_count += len([d for d in range(1, i + 1) if i % d == 0])#حالا به صفر مقدار میدهیم
        divisors_sum += sum([d for d in range(1, i + 1) if i % d == 0])#به صفر مقدار میدهیم

    return divisors_count, divisors_sum#و چاپ انها

n = int(input("Enter: "))#حالا از کاربر مقداری را میگیریم
count, total_sum = find(n)#بدست اوردن حاصل
print(count, total_sum)#چاپ حاصل
