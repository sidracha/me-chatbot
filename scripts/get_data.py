import requests
import json
import sys


limit = 100

params = {
    
    "limit": str(limit)

}

num_msg = 10000000

url = "https://discord.com/api/v9/channels/" + priv_id + "/" + "messages"

response = requests.get(url, params=params, cookies=cookies, headers=headers).json()

f = open("data3.txt", "w")


for i in range(0, len(response)):
    content = response[i]["content"]
    username = response[i]["author"]["username"]

    if username != my_username or content == "":
        continue
    
    temp = 1
    written = False
    while temp < 7 and i-temp >= 1:
        c = response[i-temp]["content"]
        if response[i-temp]["author"]["username"] == my_username or c == "":
            temp += 1
            continue
        f.write(content + " %%% " + c + "\n")
        written = True
        break
        

    if not written:
        if i == 0:
            f.write(content + " %%% " + " " + "\n")
        else:
            f.write(content + " %%% " + response[i-1]["content"] + "\n")



before = response[len(response)-1]["id"]


for i in range(0, int(num_msg/limit)):
    

    response = requests.get(url, params={"limit": str(limit), "before": before}, cookies=cookies, headers=headers).json() 

    for j in range(0, len(response)):

        content = response[j]["content"]
        username = response[j]["author"]["username"]

        if username != my_username or content == "":
            continue
    
        temp = 1
        written = False
        while temp < 7 and j-temp >= 1:
            c = response[j-temp]["content"]
            if response[j-temp]["author"]["username"] == my_username or c == "":
                temp += 1
                continue
            f.write(content + " %%% " + c + "\n")
            written = True
            break

        if not written:
            if j == 0:
                f.write(content + " %%% " + " " + "\n")
            else:
                f.write(content + " %%% " + response[j-1]["content"] + "\n")
    
    if len(response) < limit:
        break

    before = response[len(response)-1]["id"]
    print(i)







