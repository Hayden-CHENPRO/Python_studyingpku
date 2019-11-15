passwordclt = "clt5683"
i = 0
password = input('请输入密码：')
passwordlist = list(password)
while '*' in passwordlist:
    input("密码中不能含有'*'号！您还有{0}次机会！请重新输入密码：".format(2 - i))
for i in range (2):
    if password == passwordclt:
        print('密码正确，进入程序......')
        break
    elif '*' in passwordlist:
        input("密码中不能含有'*'号！您还有{0}次机会！请重新输入密码：".format(2 - i))
    else:
        input ("密码输入错误！您还有{0}次机会！请输入密码：".format(2 - i))
        i += 1
