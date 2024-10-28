import pytesseract
import pyautogui
import cv2

def get_card_info(card_position):
    screenshot = pyautogui.screenshot(region=card_position)
    screenshot.save("card.png")
    img = cv2.imread("card.png")
    card_text = pytesseract.image_to_string(img, lang="chi_sim")
    return card_text

def check_cards(LEFT_CARD_POS, MIDDLE_CARD_POS, RIGHT_CARD_POS):
    cards = [
        get_card_info(LEFT_CARD_POS),
        get_card_info(MIDDLE_CARD_POS),
        get_card_info(RIGHT_CARD_POS)
    ]
    return cards
