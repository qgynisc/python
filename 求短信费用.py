'''
题目1：短信资费
【题目描述】
	用手机发短信，一条短信资费为0.1元，但限定一条短信的内容在70个字以内（包括70个字）。如果你一次所发送的短信超过了70个字，则会按照每70个字一条短信的限制把它分割成多条短信发送。假设已经知道你当月所发送的短信的字数，试统计一下你当月短信的总资费。
【输入描述】
	第一行是整数n，表示当月发送短信的总次数，接着n行每行一个整数，表示每次短信的字数。
【输出描述】
	输出一行，当月短信总资费，单位为元，精确到小数点后1位。
'''

# 方法一
# l = int(input('请输入行数：'))
# sum = 0
# while l > 0 :
#     num = int(input('输入短信字数：'))
#     if num%70 == 0 :
#         sum += num//70*0.1
#     else:
#         sum += (num//70 + 1)*0.1
#     l -= 1
# print('%0.1f' % sum)

# 方法二
# import math
# l = int(input('请输入行数：'))
# sum = 0
# while l > 0 :
#     num = int(input('输入短信字数：'))
#     sum += math.ceil(num/70)*0.1
#     l -= 1
# print('%0.1f' % sum)


# 方法三 (此方法列出费用详单)
l = int(input('请输入行数：'))
sum = 0
dxf = []
while l > 0 :
    num = int(input('输入短信字数：'))
    if num%70 == 0 :
        dxf.append(num//70*0.1)
    else:
        dxf.append((num//70 + 1)*0.1)
    l -= 1
for x in dxf:
    sum += x
print(dxf, '%0.2f' %sum)