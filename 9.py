def print_number(num):
    """
    it is for creat number
    """
    num_str = str(num)#نوع عدد را تغیر میدهیم
    
    for i in num_str:#ساخت حلق با فور
        print(f"{i}: ", end="")#چاپ کردن ای در حلقه بالا  که اخرش یک فاصله دارد
        
        print(i * int(i))#ضرت  هر دو ای ها

user_input = int(input("Enter a number: "))#گرفتن عدد از کاربر
print_number(user_input)#چاپ و تمام
