def count(word):
    """
    its for count vowels alphabets
    """
    vowels = "aeiou"#حروف صدادار
    pronunciation_count = 1#مقدار 1
    for char in word:#ساخت حلقه برای کلمه 
        if char in vowels:#ساخت شرط
            pronunciation_count *= 2#مقدار حرف
    return pronunciation_count#برگزداندن مقدار
input_word = input("Word(6 letters):")#گرفتن کلمه از کاربر
cp = count(input_word)#شمارنده

print(cp)#چاپ و تمام

