import requests

url = 'https://httpbin.org/ip'
proxy = '5.161.202.98:10000'
# proxy = 'gate.smartproxy.com:15555'
username = '0a84b9db1cab2b518657'
password = '9d43141d1ed58228'
print(f'http://{username}:{password}@{proxy}')
proxies = {
    'http': f'http://{username}:{password}@{proxy}',
    'https': f'http://{username}:{password}@{proxy}'
}

response = requests.get(url, proxies=proxies)
print(response.json())

# url = 'https://httpbin.org/ip'
# proxy = 'geo.iproyal.com:12321'
# # proxy = 'gate.smartproxy.com:15555'
# username = 'ULdpEUe3yNcfojM5'
# password = '4u1NN4VkgnKp17Ja_streaming-1'
# print(f'http://{username}:{password}@{proxy}')
# proxies = {
#     'http': f'http://{username}:{password}@{proxy}',
#     'https': f'http://{username}:{password}@{proxy}'
# }

# response = requests.get(url, proxies=proxies)
# print(response.json())