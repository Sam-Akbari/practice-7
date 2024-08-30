n = int(input("N: "))#گرفن ان از کاربر
m = int(input("M: "))#گرفتن ام از کاربر
def home_kabootar():
    """
    it is for count birds houses
    """
    if n >= m:#اگر حرف او درست بود
        print("Yes")#درست چاپ میشود
    elif n <= m:#اگر حرف او غلط باشد
        print("No")#غلط چاپ میشود
    elif n == m:#یا اگر مساوی بودند
        print("Yes")#باز هم حرف او درست میشود
home_kabootar()#و در اخر صدا زدن تابع