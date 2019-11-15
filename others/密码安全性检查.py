passwd = input("请输入需要检查的密码组合：")
lenth = len(passwd)
str = '~!@#$%^&*()_=-/,.?<>;:\[]{}|'
numb = '0123456789'
alpha = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
for each in passwd:
    st = 1 if each in str else 0
    if st:
        break
for each in passwd:
    nt = 1 if each in numb else 0
    if nt:
        break
for each in passwd:
    at = 1 if each in alpha else 0
    if at:
        break
if lenth <= 8 or passwd.isalnum():
    print('您的密码安全评定为：低')
    print('''请按以下方式提升您的密码级别:
                    1.密码必须由数字、字母及特殊字符三种组合
                    2.密码只能由字母开头
                    3. 密码长度不能低于16位''')
elif lenth >= 16 and (st and nt and at) and (passwd[0] in alpha):
    print('您的密码安全评定为：高\n请继续保持')
else:
    print('您的密码安全评定为：中')
    print('''请按以下方式提升您的密码级别:
                    1.密码必须由数字、字母及特殊字符三种组合
                    2.密码只能由字母开头
                    3. 密码长度不能低于16位''')
