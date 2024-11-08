import requests
url = 'https://httpbin.org/ip'
proxy = 'geo.iproyal.com:12321'
# proxy = 'gate.smartproxy.com:15555'
username = 'ULdpEUe3yNcfojM5'
password = '4u1NN4VkgnKp17Ja_streaming-1'
print(f'http://{username}:{password}@{proxy}')
proxies = {
    'http': f'http://{username}:{password}@{proxy}',
    'https': f'http://{username}:{password}@{proxy}'
}

response = requests.get(url, proxies=proxies)
print(response.json())