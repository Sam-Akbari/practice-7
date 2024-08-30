def find(k):
    """
    search fanction
    """

    # تعداد ارقام در هر گروه از اعداد (1 تا 9، 10 تا 99، ...)
    group_size = 9
    # تعداد اعداد در هر گروه
    group_count = 1
    # تعداد ارقام در هر گروه
    digit_count = 1

    # پیدا کردن گروه مورد نظر
    while k > group_size * group_count * digit_count:
        k -= group_size * group_count * digit_count
        group_size *= 10
        group_count *= 10
        digit_count += 1

    # پیدا کردن عدد مورد نظر در گروه
    num_in_group = (k - 1) // digit_count
    target_num = group_count + num_in_group

    # پیدا کردن رقم مورد نظر در عدد
    digit_index = (k - 1) % digit_count
    kth_digit = int(str(target_num)[digit_index])

    return kth_digit

# ورودی‌ها را دریافت کنید
k = int(input("Enter: "))
result = find(k)
print(result)

