import webbrowser  
import time  
with open("test.txt") as fp:  
    for url in fp:  
        url = url.strip()
        time.sleep(1) #打开间隔时间  
        webbrowser.open(url)