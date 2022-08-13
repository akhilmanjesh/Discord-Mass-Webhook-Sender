import requests

whList = ["https://discord.com/api/webhooks/-/-",
"https://discordapp.com/api/webhooks/-/-",
"https://discord.com/api/webhooks/-/-",
"https://discord.com/api/webhooks/-/-"]


Start = int(input("Message: 1 \nEmbed:   2 \nChoice:  "))


while True:
    if Start == 1:
        message = input("Message: ")
        data = {
            "content": f"{message}"
        }
        for url in whList:
            result = requests.post(url, json=data)
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print("Successfully Sent, code {}.".format(
                    result.status_code))
    elif Start == 2:
        ticker = input("Ticker: ")
        leverage = input("Leverage: ")
        colorEmbed = input("Short or Long: ")
        entry = input("Entry Price: ")
        duration = input("Quick or Slow: ")
        port = input("Percent of Portfolio: ")
        colorId = 11484371

        if colorEmbed == "Short":
            colorId = 16711680 # Red Decimal
        if colorEmbed == "Long":
            colorId = 2096896 # Green Decimal

        data = {
                "username": "Akhil"
                # Change to any name you want it to send as
            }

        data["embeds"] = [
            {
                "title": f"Ticker: {ticker} | Leverage: {leverage}",
                "color": colorId,
                "fields": [
                    {
                        "name": f"Entry: {entry}",
                        "value": f"\nQuick or Slow: {duration}\n\nPercent of Portfolio: {port}"
                    }
                ],
                "footer": {
                "text": "Akhil"
                # Change to any name you want it to send as
                }
            }
        ]
        for url in whList:
            # Below is to change what is being sent based on which webhook it is being sent to
            if url == "https://discord.com/api/webhooks/-/-":
                data["content"] = "<@&#########>" # Exchange copied role id from discord with hashtags to ping role you want
                result = requests.post(url, json=data)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                else:
                    print("Successfully Sent, code {}.".format(
                        result.status_code))
            elif url == "https://discord.com/api/webhooks/-/-":
                data["content"] = "<@&#########>" # Exchange copied role id from discord with hashtags to ping role you want
                result = requests.post(url, json=data)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                else:
                    print("Successfully Sent, code {}.".format(
                        result.status_code))
            else:
                result = requests.post(url, json=data)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                else:
                    print("Successfully Sent, code {}.".format(
                        result.status_code))
    else:
        print("Error")
