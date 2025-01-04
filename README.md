# Instagram Unfollow Bot

## Overview

This project is a Selenium-based bot designed to automate the process of unfollowing users on Instagram who do not follow you back. The bot interacts with the Instagram website, logging into your account, identifying users who do not follow you back, and unfollowing them.

## Features

- Logs into your Instagram account securely.
- Fetches the list of users you follow and your followers.
- Compares both lists to identify non-mutual followers.
- Automates the process of unfollowing users who do not follow you back.

## Requirements

### Prerequisites

- Python (3.7 or later)
- Google Chrome Browser
- Chromedriver (compatible with your Chrome version)

### Python Libraries

Install the following Python libraries before running the bot:

```bash
pip install selenium
pip install requests
```

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/arthfs/instagram-unfollow-bot.git
   cd instagram-unfollow-bot
   ```

2. **Download Chromedriver**

   - Find the correct version for your Chrome browser [here](https://chromedriver.chromium.org/downloads).
   - Place the `chromedriver` file in the project directory.

3. **Download Your Instagram Data**

   - Request your Instagram data from the Instagram app or website.
   - Once downloaded, extract the data and locate the `followers.json` and `following.json` files.

4. **Configure Paths in ****`functions.js`**

   - In the `functions.js` file, provide the paths to the `followers.json` and `following.json` files. Update the code as follows:
     ```javascript
     file_1 = open("path to following's file", 'r')
     json_1 = json.load(file_1)
     data_1 = json_1["relationships_following"]
     followings = [d['string_list_data'][0]['value'] for d in data_1]

     file_2 = open("path to follower's file", 'r')
     json_2 = json.load(file_2)
     followers = [d['string_list_data'][0]['value'] for d in json_2]
     ```

5. **Configure Instagram Credentials**

   - In the `mass_unfollowing.py` file, locate the following lines:
     ```python
     usr = driver.find_element(By.NAME, 'username')
     usr.send_keys('your username')

     passw = driver.find_element(By.NAME, 'password')
     passw.send_keys('your password')
     ```
   - Replace `'your username'` and `'your password'` with your Instagram username and password.

6. **Run the Bot**

   ```bash
   python mass_unfollowing.py
   ```

## Usage

1. The bot will open a Chrome browser instance and navigate to Instagram.
2. It will log in using the credentials provided in the script.
3. It uses the `not_following` function from `functions.js` to retrieve a list of users who do not follow you back.
4. The bot will automate the process of unfollowing these users.

## File Structure

```
instacchromedriver
|— mass_unfollowing.py
|— functions.js
|— README.md
```

## Important Notes

- **Instagram Rate Limits:** Be cautious when using the bot to avoid triggering Instagram’s anti-bot measures. Add delays between actions if necessary.
- **Account Security:** Use the bot responsibly and avoid sharing your credentials.

## Disclaimer

This project is for educational purposes only. The use of bots to automate Instagram actions may violate Instagram’s terms of service. Use it at your own risk.

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

