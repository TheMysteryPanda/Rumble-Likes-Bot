
# Rumble Likes Bot

This script automates the process of liking Rumble videos using multiple bot accounts and proxies. It simulates user interactions to log in and like a video on Rumble using Selenium, undetected Chrome, and a rotating list of proxies.

## Features
- **Multi-threading**: Run multiple bots simultaneously to like a Rumble video.
- **Proxy Support**: Uses rotating proxies to bypass IP restrictions.
- **User-Agent Rotation**: Randomly selects a user-agent to mimic real browser usage.
- **Customizable**: You can modify the number of bots, starting count, and target video/channel URL.

## Requirements
- Selenium
- Undetected Chromedriver
- Fake UserAgent
- Proxies (stored in a database)
- A SQL Database for bot accounts and proxy management

## Installation

1. Clone this repository.
   ```bash
   git clone https://github.com/TheMysteryPanda/Rumble-Likes-Bot,git
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have a database set up to store your bot accounts and proxies.

4. Run the bot:
   ```bash
   python3 like_video.py 10 1 https://www.rumble.com/video.html
   ```

## Usage

Call the main function `start_rumble_likes()` with the following parameters:
- `amount_of_bots`: Number of bots to run concurrently.
- `start_count`: Starting index for the bot accounts.
- `channel_url`: The URL of the Rumble video to like.

Example:
```python
start_rumble_likes(amount_of_bots=10, start_count=0, channel_url="https://rumble.com/videolink")
```

For further assistance or if you wish to purchase Rumble likes, visit our [shop](https://fame.cheap/shop/rumble/likes).

## SEO Keywords
Here are some useful keywords that you can click to visit our shop:

- [Buy Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Rumble Likes Service](https://fame.cheap/shop/rumble/likes)
- [Rumble Automation Bot](https://fame.cheap/shop/rumble/likes)
- [Increase Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Rumble Likes Tool](https://fame.cheap/shop/rumble/likes)
- [Purchase Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Get More Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Fame Cheap Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Automated Rumble Likes](https://fame.cheap/shop/rumble/likes)
- [Boost Rumble Video](https://fame.cheap/shop/rumble/likes)
- [Rumble Engagement Service](https://fame.cheap/shop/rumble/likes)
- [Buy Rumble Votes](https://fame.cheap/shop/rumble/likes)
- [Rumble Like Bot](https://fame.cheap/shop/rumble/likes)

## License
This project is licensed under the MIT License.
