def prime_factors(x):
    """
    it is for factors
    """
    factors = []#ساخت متغیر فاکتور
    #ساخت شرط تا وقتی که
    while x % 2 == 0:
        factors.append(2)
        x //= 2
        #ساخت شرط با فور
    for i in range(3, int(x**0.5) + 1, 2):
        while x % i == 0:#شرط تا وقتی که
            factors.append(i)
            x //= i
    if x > 2:
        factors.append(x)
    return factors#برگرداندن

def digit_sum(x):
    """
    it is for sum
    """
    return sum(int(digit) for digit in str(x))#برگرداندن مجموع

def calculate_D(x):
    """
    it is for حساب کردن
    """
    #ساخت متغیر و برگرداندن ان
    prime_factors_sum = sum(prime_factors(x))
    digit_sum_value = digit_sum(x)
    return prime_factors_sum + digit_sum_value

t = int(input("Enter: "))#گرفتن از کاربر
for _ in range(t):#حاقه
    n = int(input())#گرفتن
    parent = calculate_D(n)
    if parent == n:
        print("No")#نه
    else:
        print("Yes")#بله
