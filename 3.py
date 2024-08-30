z1 = int(input("z1: "))#گرفتن
z2 = int(input("z2: "))#گرفتن
z3 = int(input("z3: "))#گرفتن
def mosallas(z1,z2,z3):
    """
    it is for mossallas
    """
    all = z1 + z2 + z3#ساخت یک تابع که جمع سه ضلع مثلث است
    if all == 180:#اگر همه انها برابر 180 بود
        print("yes")#مثلث است
    else:#در غیر این صورت
        print("no")#مثلث نیست

mosallas(z1,z2,z3)#صدا زدن تابع







