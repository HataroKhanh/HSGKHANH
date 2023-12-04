"""
Viết một chương trình chấp nhận đầu vào là một câu, 
đếm số chữ cái và chữ số trong câu đó.
 Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""
a=input()
k=0;s=0
for i in a:
    if i.isdigit():s+=1
    elif i.isalpha():k+=1
print(f"Ki tu:{k}\nSo:{s}")