import pytesseract
import pyautogui
import cv2
import numpy as np

# 設定 Tesseract 的路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 確保這裡是你的 Tesseract 安裝路徑

MIN_GOLD_FOR_PURCHASE = 500  # 保留金幣門檻

def get_gold_amount():
    # 擷取金幣顯示區域的截圖
    screenshot = pyautogui.screenshot(region=(1450, 40, 100, 40))  # 調整為金幣位置
    screenshot.save("gold.png")  # 保存截圖供檢查
    
    # 將擷取的圖像轉為灰度
    img = cv2.imread("gold.png", cv2.IMREAD_GRAYSCALE)
    
    # 增強對比度
    img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

    # 應用自適應二值化增強清晰度
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 使用 Tesseract 進行 OCR 識別，並設置只識別數字
    gold_text = pytesseract.image_to_string(img, config='--psm 6 digits')
    gold_text = ''.join(filter(str.isdigit, gold_text))  # 保留數字部分

    try:
        gold_amount = int(gold_text)
        print("偵測到的金幣數量:", gold_amount)
        return gold_amount
    except ValueError:
        print("無法識別金幣數量。")
        return 0

def should_buy_card():
    gold = get_gold_amount()
    print(f"當前金幣: {gold}")
    return gold >= MIN_GOLD_FOR_PURCHASE
