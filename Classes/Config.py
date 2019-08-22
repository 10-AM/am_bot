import json
class Configs():
    def __init__(self):
        with open('am_bot_data/configs.json', 'r') as configsJson:
            configDict = json.loads(configsJson.read())
            discordDict = configDict["discord"]
            self.discord_client_id = discordDict["client-id"]
            self.discord_client_secret = discordDict["client-secret"]
            self.discord_token = discordDict["token"]