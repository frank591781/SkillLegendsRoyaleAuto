import pyautogui

# 定義各按鈕位置
RANDOM_BUY_BUTTON_POS = (1150, 750)  # 請替換為隨機購買按鈕的座標

def click_card(card_position, card_name):
    pyautogui.click(card_position)
    print(f"購買指定牌：{card_name}")

def click_random_buy():
    pyautogui.click(RANDOM_BUY_BUTTON_POS)
    print("執行隨機購買")
    
# 目前不打算新增洗牌按鈕
