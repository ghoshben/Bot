# PlaceIndia bot 

This bot is for PlaceIndia! This bot automatically fetches orders every few minutes, to prevent bots from working against each other.

## Installation instructions

Before you start, make sure your pixel latency has expired!

1. Install the [Tampermonkey](https://www.tampermonkey.net/) browser extension.
2. Click on this link: [https://github.com/PreciousWarrior/Bot/raw/master/placeindiabot.user.js](https://github.com/ghoshben/Bot/raw/master/placeindiabot.user.js). If all goes well, Tampermonkey should offer you to install a userscript. Click on **Install**.
3. Reload your **r/place** tab. If everything went well, you'll see "Get access token..." at the top right of your screen. The bot is now active, and will keep you informed of what it is doing via these notifications at the top right of your screen.

## Disadvantages of this bot

- When the bot places a pixel, it looks to yourself as if you can still place a pixel, when the bot has already done this for you (so you are in the 5 minute cooldown).
- The bot does not yet take into account an existing cooldown, so it assumes that when you open **r/place** you can immediately place a pixel. In the worst case scenario, your first pixel could waste 4 minutes and 59 seconds of time.
