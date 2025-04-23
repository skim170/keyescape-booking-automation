# KeyEscape Auto Booker 🎯

This Python script automates the reservation process for the [KeyEscape](https://www.keyescape.com/) escape room using Selenium. It automatically selects the location, date, theme, and time slot, and proceeds to fill out the required booking form.

## 📌 Features

- Automatically navigates to the KeyEscape booking page
- Selects a specific branch (`우주라이크`), date (`28`), and theme (`US`)
- Waits until reservations are available and refreshes as needed
- Selects an available time slot (e.g., `09:55`)
- Fills in user information automatically
- Makes the reservation with a single run

## ⚙️ Requirements

- Python 3.x
- Google Chrome browser installed

### Install dependencies

You can install all required packages using:

```bash
pip install selenium webdriver-manager
```

## 🚀 How to Use
1. Clone the repository or download the script.
2. Run the script:
```bash
python keyescape_auto_booker.py
```
3. The script will:
  - Open Chrome
  - Navigate to the reservation page
  - Wait and retry until an available time slot appears
  - Auto-fill your reservation details and submit the form

📝 Note: You may want to update the reservation information (name, phone number, number of people, etc.) before running the script.

## 🔐 Important
This script is intended for educational and personal use only.

Avoid abusing the service; be respectful of the site's policies.

## 📄 Disclaimer
This tool interacts with a third-party website via automation. The layout or behavior of the site may change, which can break the script. Use at your own risk.

## ✍️ Author
Seonghun Kim
[Liberty University | Computer Science (2025)]
South Korea 🇰🇷
