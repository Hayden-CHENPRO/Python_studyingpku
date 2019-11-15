def enterprogram():
    print("""
    |--- 新建用户：N/n ---|
    |--- 登录账号：E/e ---|
    |--- 退出程序：Q/q ---|
    """)

    code = input("|--- 请输入指令代码：")
    datebase = {'小甲鱼':'FishC'}
    k = 1;i = 1

    if code == 'N' or code == 'n' :
        admin = input("请输入用户名：")
        while k :
            if admin in datebase:
                admin = input("该用户名已被使用，请重新输入：")
            else:
                passw = input("请输入密码：")
                datebase[admin] = passw
                print("注册成功，赶紧试试登录吧~")
                k = 0

    if code == 'E' or code == 'e':
        admin = input("请输入用户名：")
        while i :
            if admin not in datebase:
                admin = input("您输入的用户名不存在，请重新输入：")
            else:
                passw = input("请输入密码：")
                while k :
                    if passw == datebase[admin]:
                        print("欢迎进入小鱼干第一个用户登录系统！")
                        k = 0
                    else:
                        passw = input("密码错误，请重新输入:")
                    i = 0

    if code == 'Q' or code == 'q':
        print("感谢使用此程序！")


enterprogram()