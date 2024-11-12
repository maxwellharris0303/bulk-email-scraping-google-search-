import requests
import re
from bs4 import BeautifulSoup
from time import sleep

def extract_email(content):
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    # Step 3: Use regular expression to find email addresses
    # email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com\b"
    emails = re.findall(email_pattern, text)

    # Step 4: Remove duplicates if needed
    unique_emails = list(set(emails))

    # print("Extracted emails:", unique_emails)
    for email in unique_emails:
        with open(f'emails-requests.txt', 'a', encoding='utf-8') as file:
            file.write(email + "\n")
    return len(unique_emails)

page_index= 0
flag = 0
while page_index < 2000:
    headers = {
        "Cookie": "MUID=3D063B4F42626EFC00A12E7D43CA6F4C; MUIDB=3D063B4F42626EFC00A12E7D43CA6F4C; _EDGE_S=F=1&SID=143FA5264EDE64F1265BB0144F7665D7&mkt=en-fi; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7FBEA4A5F4834D7DACBAC78868BF555D&dmnchg=1; SRCHUSR=DOB=20241109&T=1731290991000; SRCHHPGUSR=SRCHLANG=en&DM=0&BRW=NOTP&BRH=M&CW=780&CH=810&SCW=1164&SCH=1975&DPR=1.0&UTC=-480&WTS=63866887791&HV=1731291796&PRVCW=1280&PRVCH=810&EXLTT=31; _SS=SID=143FA5264EDE64F1265BB0144F7665D7&R=200&RB=0&GB=0&RG=200&RP=200; USRLOC=HS=1&ELOC=LAT=60.183685302734375^|LON=24.927433013916016^|N=Helsinki^%^2C^%^20Uusimaa^|ELT=4^|; _RwBf=r=0&ilt=95&ihpd=0&ispd=60&rc=200&rb=0&gb=0&rg=200&pc=200&mtu=0&rbb=0&g=0&cid=&clo=0&v=60&l=2024-11-10T08:00:00.0000000Z&lft=2024-11-09T00:00:00.0000000-08:00&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0&rwflt=0&rwaul2=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2024-11-11T02:23:15.6205167+00:00&rwred=0&wls=&wlb=&wle=&ccp=&cpt=&lka=0&lkt=0&aad=0&TH=; _Rwho=u=d&ts=2024-11-09; ipv6=hit=1731294593688&t=4; BCP=AD=1&AL=1&SM=1; BFPRResults=FirstPageUrls=B151B872F55B6424910AB1DFD3B24A9D^%^2C8407E7CBBB2C32E1831A9E3C38CEF4F8^%^2C25D686E8F6F4CD51BF3FE4923D81A8C6^%^2CD3D2DA9CC021864204D336B863EBF5A8^%^2C956E380FF1F3871C9EA23BE8C7C034B0^%^2C02975AC36473171FCD757D62D601ECFC^%^2C16EF85EB040E3F43E4F38B6369521B64^%^2C1D3ADEC9F5575FFF917074016D62DF17^%^2CD9A0B099DD41DD9FE6E5E60A652E047B^%^2C670F54ED11023F2BBF6553E73595098D&FPIG=803431927B5E4DC89C7BB1580D5A55A3; MSPTC=pF0FvWRN4VBQhfLEc9AmLC6Bh22NYGtKfuilQlCvP1A; ak_bmsc=399348E7C58B29E2500BF6D5B0D64153~000000000000000000000000000000~YAAQG9hUuFg+dReTAQAA+sACGRk5FiHlzs9hXc6ozAS4+u2XWs2rtdy3Zie/NUQwS9f+MnZTW4ciMBrKrI0aEi4iotXwuFoJqJYGcQSbiFPXtJQcfAqgr3Uw7ELryHkGzglNrGvxJleCJKgGsZxGRokZvACY+ZS9rlkmHLO2niBhRREvY0i6XPx/mUPw1CCgD55cXhv4dWXhtSe+9L+2TVy25kBoVUDbmxMEASdBrFIXz4krKfmzGCNScyXJH1m1aJujV4ekfiMbLBAg6PsIRh/UrskcNfZ7gRhlJISBdCMvUY7pCjPhB/WrC12zK3LW0WsRMMGAhtHs2snzOBQJYnKDVGHCcumLYzOIl5fpvdfzRJJl1mex8GyT/DPp3h+KclgzWZYJyg==; dsc=order=BingPages"
    }
    response = requests.get(f"https://www.bing.com/search?q=gloversville+influencer+%40outlook.com+site%3Afacebook.com&first={page_index}", headers=headers)
    # print(response.cookies)
    email_count = extract_email(response.content)
    print(email_count)
    if email_count != 0:
        flag = 0
    else:
        flag += 1
    if flag > 5:
        break

    page_index += 10