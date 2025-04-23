# KeyEscape Auto Booker 🎯

This Python script automates the reservation process for the [KeyEscape](https://www.keyescape.co.kr/) escape room using Selenium. It automatically selects the location, date, theme, and time slot, and proceeds to fill out the required booking form.

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

\`\`\`bash
pip install selenium webdriver-manager
\`\`\`
