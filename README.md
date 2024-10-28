
# Skill Legends Royale Auto-Buy Bot

An automated bot for purchasing specific cards in **Skill Legends Royale**, designed to enhance gameplay by prioritizing essential and high-value cards. This bot utilizes OCR to identify card names and follows a predefined list of priority cards for optimal efficiency.

## Features
- Automatically identifies and buys cards based on user-defined priority.
- Utilizes OCR (Optical Character Recognition) for card text recognition.
- Customizable priority settings for different card types (e.g., gold, blue, regular).
- Easy-to-modify Python scripts for further customization.

## Requirements
- **Python 3.x**
- **Tesseract OCR** (for text recognition)
- **Required Python packages**:
  - `opencv-python-headless`
  - `pytesseract`
  - `pyautogui`

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/SkillLegendsRoyaleAuto.git
   ```
2. **Navigate into the project directory**:
   ```bash
   cd SkillLegendsRoyaleAuto
   ```
3. **Install the required packages**:
   ```bash
   pip install opencv-python-headless pytesseract pyautogui
   ```
4. **Install Tesseract OCR**:
   - Download and install Tesseract from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) or the [Windows installer](https://digi.bib.uni-mannheim.de/tesseract/).
   - Set the Tesseract executable path in your code (if required).

## Usage
1. **Configure Card Priorities**:
   - In `main.py`, edit the `GOLD_CARDS` and `TARGET_CARDS` dictionaries to define the priority cards for auto-buy.

2. **Run the Bot**:
   - Use the following command to start the bot:
     ```bash
     python main.py
     ```

3. **Customizing**:
   - Adjust the time interval and card recognition logic as needed in `main.py` and `actions.py`.

## File Structure
- `main.py`: Main script to run the bot.
- `actions.py`: Contains functions for clicking and interacting with the game interface.
- `card_checker.py`: Functions for checking and recognizing card names.
- `gold_checker.py`: Handles checking of in-game currency (gold) availability.

## Notes
- Make sure the game is running in 1920x1080 resolution for accurate card detection.
- Regularly check and update card priority settings to adapt to game updates or personal strategy.

## Disclaimer
This bot is intended for educational purposes only. Use at your own risk.
