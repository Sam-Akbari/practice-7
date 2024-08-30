def passport(valid_alphabet, test_code):
    """
    it is for code
    """
    #ساخت متغیر
    valid_set = set(valid_alphabet.lower() + valid_alphabet.upper())
    test_set = set(test_code.lower() + test_code.upper())

    return test_set.issubset(valid_set)#برگرداندن متغیر

def main():
    """
    and it is for input
    """
    #مقداری که کاربر میدهد
    n, t = input("Enter: ").split()#
    n = int(n)

    #ساخت کد تخفیف با حلقه
    for i in range(n):
        code = input()#گرفتن
        if passport(t, code):
            print("Yes")#درست
        else:
            print("No")#غلط
#صدا زدن تابع با شرط
if __name__ == "__main__":
    main()
