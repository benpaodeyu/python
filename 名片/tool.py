import os
list = []
#记录查询到的名片中姓名信息
target_card = {}
def shows():
    print("*"*40)
    print("1新建名片")
    print("2显示全部")
    print("3名片的查询与修改")
    print("4保存数据到文件")
    print("5数据加载到当前文件中")
    print("0退出系统")
    print("*" * 40)

#新增名片，将每个名片的内容放进字典，最后将所有的字典组合成一个列表
def add_cards():

    #dic = {}
    name = input("请输入你的名字：")
    phone = input("请输入你的电话：")
    email = input("请输入你的邮箱：")
    # dic["姓名"]=name
    # dic["电话"]=phone
    # dic["邮箱"]=email
    dic = {"姓名":name,"电话":phone,"邮箱":email}
    list.append(dic)
    print(list)


#列出所有添加的名片
def all_show():
    #判断列表的长度，如果长度大于0表示有数据
    if len(list)>0:
        #输出一个表头
        print("姓名\t 电话\t 邮箱\t")
        for message in list:
            print("%s\t\t %s\t\t %s\t\t"%(message["姓名"],message["电话"] ,message["邮箱"]))
            # print(message["姓名"] ,message["电话"] ,message["邮箱"])
    else:
        print("没有名片信息")

def check_cards():
    if len(list)>0:
        target = input("请输入你要查找的姓名：")
        for message in list:
            if target == message["姓名"]:
                print("姓名\t 电话\t 邮箱\t")
                print("%s\t\t %s\t\t %s\t\t" % (message["姓名"], message["电话"], message["邮箱"]))
                # print(message["姓名"] ,message["电话"] ,message["邮箱"])
                #在这里添加break表示当查询到后退出if语句，否则会继续向下查询
                #将查询到的名片姓名信息定义为全局变量，便于后期修改使用
                global target_card
                target_card = message
                manager()
                break
        #将else写在这里，以免每次查询不到都会输出一次查找的姓名不存在
        else:
            print("查找的姓名不存在")
    else:
        print("没有名片信息")


def manager():
    while True:
        option = input("请输入你想做的操作 1.修改/ 2.删除/ 3.返回上一级/：")
        if option == "1":
            update ()
        elif option =="2":
            delete ()
        elif option =="4":
            print("返回上一级")
            break
        else:
            print("请输入正确的操作选项：")

#
def update():
    target_card["姓名"]=input("请修改输入姓名:")
    target_card["电话"]=input("请修改输入电话:")
    target_card["邮箱"]=input("请修改输入邮箱:")

def delete():
    list.remove(target_card)

def save_cards():
    file =open("data.txt","w")
    file.write(str(list))
    file.close()

def load_cards():
    if  os.path.exists("data.txt")==True:
        file = open("data.txt","r")
        count = eval(file.read())
        global list
        list = count
        file.close()


