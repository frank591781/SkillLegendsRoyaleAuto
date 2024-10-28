import time
from gold_checker import should_buy_card
from card_checker import check_cards
from actions import click_card, click_random_buy

# 定義各卡片位置
LEFT_CARD_POS = (933, 444, 117, 32)    # 左邊卡片的座標和區域
MIDDLE_CARD_POS = (1211, 444, 117, 32)  # 中間卡片的座標和區域
RIGHT_CARD_POS = (1484, 444, 117, 32)   # 右邊卡片的座標和區域

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

# 定義藍卡字典及其等級權重
BLUE_CARDS = {
    "戰時狂熱": 2,
    "先鋒攻擊": 2,
    "精神振奮": 2,
    "毒性傷害": 2,
    "毒性外衣": 2,
    "戰前下毒": 2,
    "時間詛咒": 2,
    "傷害專精": 2,
    "戰前易傷": 2,
    "能量大招": 2,
    "充能傷害": 2,
    "略量大招": 2,
    "護盾重擊": 2,
    "防禦專精": 2,
    "戰前護盾": 2,
    "戰前冰凍": 2,
    "冰凍傷害": 2,
    "冰凍外殼": 2,
    "怒火釋放": 2,
    "忘卻疼痛": 2,
    "狂怒延長": 2,
    "呼喚守衛": 2,
    "死亡勳章": 2,
    "精靈彈珠": 2,
    "放療射線": 2,
    "醫療爆炸": 2,
    "吸血傷害": 2,
    "生命之擊": 2,
    "生命剛強": 2,
    "魔法抵禦": 2,
    "戰時狂暴": 2,
    "生命暴擊": 2,
    "魔法暴擊": 2,
    "靈巧反擊": 2,
    "戰時靈巧": 2,
    "魔法閃避": 2
}

# 合併所有卡片字典
ALL_CARDS = {**GOLD_CARDS, **BLUE_CARDS, **TARGET_CARDS}

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
