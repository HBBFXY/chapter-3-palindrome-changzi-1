While True:
input_number=input("请输入一个5位数字(输入e退出):")
if input_number()=='e':
  print("程序已退出")
  break
if len(input_number) !=5 or not
input_number.isdigit():
  print("输入错误,请输入有效的5位数字:")
  continue
else:
  if input_number == input_number[::-1]:
    print("是回文数")
  else:
    print("不是回文数")
