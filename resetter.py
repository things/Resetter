from datetime import datetime
import subprocess
import time
import requests
import os

x = ""

print("__________                      __    __                 \n\______   \ ____   ______ _____/  |__/  |_  ___________  \n |       _// __ \ /  ___// __ \   __\   __\/ __ \_  __ \ \n |    |   \  ___/ \___ \\  ___/|  |  |  | \  ___/|  | \/ \n |____|_  /\___  >____  >\___  >__|  |__|  \___  >__|    \n        \/     \/     \/     \/                \/        ")
print("made by github.com/things")
print("")
print("")
key = input("Please enter your access token : ")

os.system("cls")

print("__________                      __    __                 \n\______   \ ____   ______ _____/  |__/  |_  ___________  \n |       _// __ \ /  ___// __ \   __\   __\/ __ \_  __ \ \n |    |   \  ___/ \___ \\  ___/|  |  |  | \  ___/|  | \/ \n |____|_  /\___  >____  >\___  >__|  |__|  \___  >__|    \n        \/     \/     \/     \/                \/        ")
print("made by github.com/things")
print("")
print("")

while x == "":
	requests.post("https://api.steampowered.com/IPlayerService/SetFavoriteBadge/v1?access_token=" + key)
	requests.post("https://api.steampowered.com/IPlayerService/SetProfileBackground/v1?access_token=" + key)
	requests.post("https://api.steampowered.com/IPlayerService/SetAvatarFrame/v1?access_token=" + key)
	requests.post("https://api.steampowered.com/IPlayerService/SetMiniProfileBackground/v1/?access_token=" + key)
	requests.post("https://api.steampowered.com/IPlayerService/SetProfileTheme/v1/?access_token=" + key)
	now = datetime.now().strftime("%H:%M:%S")
	print("Reset" + " (" + now + ")")
	print("__________________________________________")
	time.sleep(10) 