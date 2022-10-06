import requests

def download(fileName):
    f = open(fileName,'wb')
    f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    f.close()


with open("names.txt", "r+",encoding="utf-8") as f:
    data = f.readlines()
    for i in range(len(data)):
        print(data[i].split("\n")[0])