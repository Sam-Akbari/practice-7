def chairs(i1, i2):
    """
    it for chairs
    """
    # ابتدا لیست‌ها را با هم مقایسه می‌کنیم
    matching_count = sum(1 for a, b in zip(i1, i2) if a == b)
    return matching_count
#گرفتن از کاربر
i1 = input("i1: ")
i2 = input("i2: ")

# تعداد مشابه‌ها را محاسبه می‌کنیم
r = chairs(i1, i2)

print(r/2)
