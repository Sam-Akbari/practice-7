def find(m, s):
    """
    it is for search
    """
    smallest = [0] * m#ساخت متغیر
    remaining_sum = s#ساخت متغیر
    for i in range(m - 1, -1, -1):#ساخت حلقه
        digit = min(9, remaining_sum)#عدد کوچکتر
        smallest[i] = digit#عدد کوچکتر
        remaining_sum -= digit

    largest = [0] * m
    remaining_sum = s
    for i in range(m):#ساخت حلقه
        digit = min(9, remaining_sum)#ساخت متغیر
        largest[i] = digit#ساخت متغیر
        remaining_sum -= digit

    smallest_num = int("".join(map(str, smallest)))#برای جایگذاری
    largest_num = int("".join(map(str, largest)))#برای جایگزاری

    return smallest_num, largest_num#برگرداندن عدد

m, s = map(int, input("Enter: ").split())#گرفتن مقدار از کاربر
smallest_result, largest_result = find(m, s)#پیدا کردن
print(smallest_result, largest_result)#چاپ عدد و تمام
