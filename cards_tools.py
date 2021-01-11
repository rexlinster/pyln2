#紀錄所有名片的字典

card_list = []



def show_menu():

   #顯示選單
    print("*"*50)

    print("歡迎使用名片管理系統[V1.0]")
    print("")
    print("1.新增名片")
    print("2.顯示名片")
    print("3.查詢名片")

    print("")
    print("0.離開系統：")


    print("*"*50)



def new_card():
    
    
    
    """新增名片"""
    #提示用戶輸入名片相關訊息
    print("-"*50)
    print("新增名片")
    print("-"*50)
    #以用戶輸入訊息建立字典
    name_str = input("請輸入姓名：")
    phone_str = input("請輸入電話:")
    qqid_str = input("請輸入QQ:")
    email_str = input("請輸入email:")

    card_dict = {"name" : name_str,
        "phone" : phone_str,
        "qqid" : qqid_str,
        "email" : email_str}
    #將名片字典加入列表中    
    card_list.append(card_dict)
    print(card_list)
    #提示用戶添加成功
    print("名片輸入完成%s" %name_str)



def show_allcards():
    """顯示所有名片"""
    print("-"*50)
    print("顯示所有名片")
    print("-"*50)
    #列印表頭
    for name in ["姓名","電話","QQ","EMAIL"] :
        print(name,end=" \t\t")

    print(" ")
    #列印分隔縣
    print("="*70)
    #遍歷名片列表並列印
    for card_dict in card_list :
        #print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],card_dict["phone"],card_dict["qqid"],card_dict["email"]))
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],card_dict["phone"],card_dict["qqid"],card_dict["email"]))



def query_cards():
    """查詢名片"""
    print("-"*50)
    print("查詢名片")
    print("-"*50)
