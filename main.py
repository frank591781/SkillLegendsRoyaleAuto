import time
from gold_checker import should_buy_card
from card_checker import check_cards
from actions import click_card, click_random_buy

# 定義各卡片位置
LEFT_CARD_POS = (640, 580, 120, 180)
MIDDLE_CARD_POS = (840, 580, 120, 180)
RIGHT_CARD_POS = (1040, 580, 120, 180)

# 定義符合條件的普通卡牌字典及其等級權重（數字越小優先級越高）
TARGET_CARDS = {
    "持續下毒": 3,
    "持續易傷": 3,
    "能量回復": 3,
    "攻擊提升": 3,
    "持續冰凍": 3,
    "自然之癒": 3,
    "基礎護盾": 3,
    "精靈契約": 3,
    "基礎怒氣": 3,
    "生命提升": 3,
    "暴擊提升": 3,
    "閃避提升": 3
}

# 定義金卡字典及其較高的優先級
GOLD_CARDS = {
    "無畏連擊": 1,
    "完美反射": 1,
    "神聖爆破": 1,
    "聖光復活": 1,
    "治癒法陣": 1,
    "先發制人": 1,
    "毒性爆發": 1,
    "霜凍新星": 1,
    "最終防禦": 1,
    "無盡雷劫": 1,
    "雙子精靈": 1,
    "怒火中燒": 1
}

# 合併字典
ALL_CARDS = {**GOLD_CARDS, **TARGET_CARDS}

while True:
    if should_buy_card():
        cards = check_cards(LEFT_CARD_POS, MIDDLE_CARD_POS, RIGHT_CARD_POS)

        # 遍歷檢查是否有符合條件的牌，根據權重優先選擇
        for idx, card in enumerate(cards):
            card_name = next((name for name in ALL_CARDS if name in card), None)
            if card_name:
                card_position = [LEFT_CARD_POS, MIDDLE_CARD_POS, RIGHT_CARD_POS][idx]
                click_card(card_position, card_name)  # 傳遞 card_name 給 click_card
                break
        else:
            # 如果三張牌都不符合條件，則點擊隨機購買
            click_random_buy()

    else:
        print("金幣不足，結束購買，或是等待戰鬥結束")

    time.sleep(1)  # 每 1 秒檢查一次
