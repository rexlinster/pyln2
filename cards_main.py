import cards_tools

#顯示全部,#查詢名片pass

while True :
# TODO(小明) #3 顯示功能選項
    cards_tools.show_menu()





    action_str = input("請選擇希望執行的工作：")
    print("您選擇的操作是[%s]" %action_str)

#1,2,3對名片的操作
    if action_str in ["1","2","3"] :
#新增名片
        if action_str == "1" :

            cards_tools.new_card()
#顯示全部
        elif action_str == "2":

            cards_tools.show_allcards()

        elif action_str == "3":
            cards_tools.query_cards()
    elif action_str == "0":
        print("歡迎再次使用[名片管理系統]")
        break
#        pass
    else :
        print("您輸入不正確，請重新輸入")

