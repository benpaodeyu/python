

import tool

while True:
    tool.shows()
    select = input("请输入你的选择:")
    if select == "1":
        print("功能：新建名片")
        tool.add_cards()

    elif select == "2":
        print("功能：显示全部名片")
        tool.all_show()

    elif select == "3":
        print("功能：名片的查询与修改")
        tool.check_cards()

    elif select == "0":
        print("退出系统")
        break
    elif select == "4":
        print("功能：保存名片")
        tool.save_cards()
    elif select == "5":
        print("功能：加载名片")
        tool.load_cards()
    else:
        print("请输入正确的选择")