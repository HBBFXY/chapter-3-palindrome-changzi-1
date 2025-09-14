def is_palindrome():
    while True:
        num = input("请输入一个5位数字（输入e退出）：")
        if num.lower() == 'e':
            print("程序已退出。")
            break
        if len(num) != 5:
            print("输入错误，请确保输入一个5位数字。")
            continue
        if not num.isdigit():
            print("输入错误，请确保输入的是数字。")
            continue
        if num == num[::-1]:
            print("是回文数。")
        else:
            print("不是回文数。")

is_palindrome()
