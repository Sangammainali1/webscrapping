import requests
import os
url = "https://timesofindia.indiatimes.com/city/delhi"

# os.makedirs(os.path.dirname("data/times.html"), exist_ok=True)

def fetchAndSaveToFile(url,path):
    r=requests.get(url)


    #   # Ensure the directory exists before saving the file
    # directory = os.path.dirname(path)
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
        
    with open(path,"wb") as f:
        f.write(r.content)



fetchAndSaveToFile(url,"data/times.html")