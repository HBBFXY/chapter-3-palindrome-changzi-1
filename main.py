input_number=input("请输入一个5位数字:")
if len(input_number) !=5 or not
input_number.isdigit():
  print("请输入有效的5位数字!")
else:
  if input_number == input_number[::-1]:
    print("是回文数")
  else:
    print("不是回文数")
