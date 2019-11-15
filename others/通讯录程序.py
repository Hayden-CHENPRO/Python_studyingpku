print("""
|--- 欢迎进入通讯录程序 ---|
|--- 1：查询联系人资料  ---|
|--- 2：插入新的联系人  ---|
|--- 3：删除已有联系人  ---|
|--- 4：退出通讯录程序  ---|
""")

dictConts = {'小甲鱼':'020-88974651'}
code = eval(input("请输入相关的指令代码："))

if code == 1:
    name = input("请输入联系人姓名：")
    if name in dictConts.keys():
        print(name + ':' + dictConts[name])
    else:
        print("您输入的联系人不在通讯录中！")

elif code == 2:
    name = input("请输入联系人姓名：")
    if name not in dictConts.keys():
        num = input("请输入用户的联系电话：")
        dictConts[name] = num
        print("插入完成！")
    else:
        print("您输入的姓名在通讯录里中已存在 -->> %s" % (name + ':' + dictConts[name]) )
        ques = input("是否修改用户资料（YES/NO）:")
        if ques == 'YES':
            num = input("请输入用户联系电话：")
            dictConts[name] = num

elif code == 3:
    name = input("请输入联系人姓名：")
    dictConts.pop(name)

elif code == 4:
    print("|--- 感谢使用通讯录程序 ---|")
