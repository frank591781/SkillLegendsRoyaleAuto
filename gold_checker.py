import pytesseract
import pyautogui
import cv2

# 設定 Tesseract 的路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 替換成你的Tesseract安裝路徑

MIN_GOLD_FOR_PURCHASE = 500  # 保留金幣門檻

def get_gold_amount():
    # 擷取金幣顯示區域的截圖 (根據畫面調整 x, y, width, height)
    screenshot = pyautogui.screenshot(region=(1600, 100, 120, 50))
    screenshot.save("gold.png")
    img = cv2.imread("gold.png")
    gold_text = pytesseract.image_to_string(img, config='--psm 6')
    gold_text = ''.join(filter(str.isdigit, gold_text))  # 保留數字部分
    try:
        return int(gold_text)
    except ValueError:
        return 0

def should_buy_card():
    gold = get_gold_amount()
    print(f"當前金幣: {gold}")
    return gold >= MIN_GOLD_FOR_PURCHASE
