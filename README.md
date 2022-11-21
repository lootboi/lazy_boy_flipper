# lazy boy flipper

![this is a flipper](./img/flipper.gif)

**The lazy boy flipper excels at two different functionalities:**
1. Finding and retreiving data concerning any collection available on the [Joepegs Marketplace](https://joepegs.com/).
2. Alerting the user of any new listings according to either attribute or floor parameters.

While there are other community made tools, such as [Avalytics](https://www.avalytics.xyz/), that provide a lot of the same information, the lazy boy flipper is able to differentiate itself by allowing users to better visualize and utilize data concerning a collections NFT's. Where it does fall short, however, is in aggregating marketplace data from [Kalao](https://marketplace.kalao.io/) or [Campfire](https://campfire.exchange/) - but there's not a lot of volume on these other markeplaces so it's not that big of a loss ;)

Initially I wanted this to purchase and list NFT's as well. However, Joepegs Marketplace is set up so that creating an ask order occurs off chain, and requires special permission to gain access to outside of their website. Because of this, creating listings is not feasible within the script - although purchases still occur on-chain and I will eventually add this feature into the repository.

This project is also **completely open-source**! so customize it, break it, and bastardize until you are content with the script.

## Requirements

**Need these no matter what**

- ```python3``` - [Download](https://www.python.org/downloads/)
- Joepegs API Key - [Get one here](https://docs.google.com/forms/d/e/1FAIpQLSc15ukzANESa2QDT8EQfgvHx14lAFsnK6WxMJy4bh0nE_G-pw/viewform)

**Not required but necessary if you wish to use any of the scanning functionality:**
- Discord Account - [Create an Account](https://discord.com/)
- Discord Bot - [Learn how here](https://www.upwork.com/resources/how-to-make-discord-bot)

## Setup

1. Clone this repo using your preferred cloning method
2.Download all of the required modules in ```requirements.txt```. You can do this by running: ```pip install -r /path/to/requirements.txt``` anywhere within the project directory (as long as the path is accurate)
3. Create a file in the main project directory called ```.env```. In it you can copy the content within ```ENV_EXAMPLE``` and paste it within ```.env```. Now you can fill in each variable using your own information!
    1. It should look like this [image]
    2. ```JOEPEG_API_KEY``` = Your API key that you received by filling out the form above
    3. ```DISCORD_KEY``` = The bot's key that you are given when you created the Discord Bot account
    4. ```CHANNEL_ID``` = An ID used to identify the Discord channel you wish to have the bot send notifications in. (You can figure out how to find this [here](https://www.remote.tools/remote-work/how-to-find-discord-id))
    
## Usage 

![press start, or are you scared](./img/start.gif)

In order to start the script, navigate to the ```/python``` folder and run the following command:
```python main.py```

From there, the script will prompt you to enter various options to decide what it should do for you. I reccomend starting out by checking your API connection first, as if it is not properly configured, you will encounter only errors (and nothing useful)!

## Initial Options
1. ```Test Connection``` - Tests the Joepeg API key that you provided and prints the status code.
2. ```Trending Collections``` - Outputs basic information of the top 10 trending collection on the Joepegs Marketplace.
3. ```Collection Options``` - Takes the user to additional options available concerning collection data.

## Collection Options
1. ```Get Collection Overview``` - Given a collection address, returns holisitic data concerning the collection.
2. ```View Item Info``` - Given a collection address and item ID, returns information concerning that specific item.
3. ```View Items based on Attribute``` - Returns the cheapest items listed as 'buy now' filtered by specific attributes.
4. ```Scan Options``` - Takes the user to additional options available concerning scanning for new listings.
5. ```Visualize Collection Attribute Data``` - Visualizes a collections attribute data using a bar graph.
6. ```Get Rarest Items (If Ranking is Available)``` - Returns x amount of items based off of rarity.

## Scan Options
1. ```Scan for new listings using an attribute``` - Scans and notifies users through Discord of new listings in a collection that have a specified attribute.
2. ```Scan for new listings using a minimum floor price``` - Scans and notifies users through Discord of new listings in a collection within a specific maximum prices.

## Contributing

![contributing is a good thing to do](./img/handshake.gif)

If you would like to contribute, create a Pull Request and I will approve it if I think that it has some value. If not, I will try to give you feedback as to why it was not included in the public repository.
