import requests 
import json 
import pandas as pd 
from datetime import date 
import html_to_json

url = "https://www.scan.co.uk/todayonly"


##due to the nature of webscraping, if requests are to frequent they are blocked, replace the cookie if this is the case  


import requests

url = f"https://www.scan.co.uk/todayonly"

payload={}
headers = {
  'authority': 'www.scan.co.uk',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'S=IsH8jY1PjjgbqDsm08rNveicWRgcfIT9wnFEvFNuoYeNNI3sv7odRcfapy/bBE0NwlmE80Bg6amZjxqXZxzzUQ==; DS=rQM7pITbDJIt2Gq+KcfL3h8QSuJafE634FjJHU2jXVSvIelzfMo8LpbbOI89WTf7wJ8TFVKH+qXWBeC4jugNFA==; R=ZRhQHB5YWjW1EaTGSecimpcD705WXQsBC4CGIGe3JIbn8VsKrVUAos3ORQpOApS579M9z25UkW/BFbYJBwzfd5NWD3YcjR03A8N7/L8UMA88vrAR7za/sQc+xtqdDbFbINlCre/3PD9LXbAK54PwxIrw4+B3or4sXjGFFzrp1Hc=; US=7sQJRKUOyY/m+cJknOdUoBlV0MT1cJhNgG5M7S/S7M+sg3rCLRvZFWxO7rRYdYgelAZB3hw9ZucVVcbXxC9chv/5h0ZinFlKuMTYHu0YtfVQSMNqc7zwxPVFWGUR9Wgi0Rus4zsE2fOB/XBK4A+p5CsegcS3lBZ9rcKqCW7eVPzbsZ14QswC1RfW5KT1IPzvf1aCa+AiYybJXXDQvZGxnmSauXtfhJ2GHADjL4EFUzkRai9z3rrue1ljt4UQK1ASxX0Sp/jmZAfo0Sl4u42cCK+WDesh0eWCtvVOkeXTOUaHPe7xLFDgEboGRaOVTYOx; _wt.newReturning=Sat Jan 14 2023 22:46:34 GMT+0000 (Greenwich Mean Time); _wt.newVisitor=Sat Jan 14 2023 22:46:34 GMT+0000 (Greenwich Mean Time); ai_user=K7dsBJaKZp3tq4d3WPSEs/|2023-01-14T22:46:34.554Z; _gcl_au=1.1.959752496.1673736395; _ga=GA1.3.64301033.1673736395; _gid=GA1.3.1586472965.1673736395; _wt.mode-1668725=WT3OAo_B2Jr3hk~; _wt.control-1668725-ta_101SuperClickMenuTake2=WT3iE1XAvFPZE0qSacFdqNxBbdIV6jIqAWyU0HD54O_99UXFXA04lWFlX2BQr6BLEPHjbUmyOUfMQFyrUi4Lb4VlWrBrMURw7BouGmB46yjBve9wqioRVrEFoyMjvqZ4jREHLd5unvsOSBWqLvpdZv8oGkHurvbJsErrveAniCJNOxxjirZz-LfyjUq4DxTw92tOXUQRnzUPjTDdbLwXZD0TzxUH1Yzf6n-EIDh7rdsTikgYsHFrmjTuaqG8FMHOvM0uT-lBeHZ6wHiuiOy; __cf_bm=1W1VJUuFAgUhU3TgGZgZJi5mRpNzi0JzwFMbVjHys_w-1673736394-0-AbBLiEYpcWuNA+6eYZhBB1KN5U7C0bSYJ4ChfHrV58xkIKd+9m5pall40QGU3LyDEu2mkEpnBAs+nsWtN/xc3iby78j6l8I6Nt3Uss+IT7jiZRkz3ZY3U380OXPHyUgcovZKZicNocGmgRlCfC8kLjU=; cookpol=3; _fbp=fb.2.1673736397284.2065341474; _wt.user-1668725=WT3h9XZi-3sVANqUqDMqoBqSv6FHbvMIyi_l8fNSe1PmHuLSOJM0U8ipkGT1PoRhw4DgYE2AZdcOTBC-eEAZn_adnXpacroCcEJtHtHK1Q6tBIyvbMdUddKnQBWD-3wLpmgVhoDj16jdLzmFuMVc5JDgWLE4dfwp6FoYlByW1HfZhRF-0fce2LScO-8rZOegN-itlXLfo7n66Gsyq4KyRl4QxfLmRE~; ai_session=ePNVr/5Ria9hgWu26upfJv|1673736394609|1673736397394; DS=xKQjaV9QQiz2dVv93OgZYHF5qhSPltmEntQjJsLBI5EsYQQ3nz5JlAIqtLecSpx8W84BrVt6YhHZsmNn4yNWzQ==; S=a7QBx8aoqik3q2/xeWUMdu5jw4MQ5b1W3zhL/657qfZ145kvQGT3mTm79YZ43MYI8hkgfyBuAOM5oCeya24x5Q==; US=7sQJRKUOyY/m+cJknOdUoBlV0MT1cJhNgG5M7S/S7M+sg3rCLRvZFWxO7rRYdYge2x87lZv3PB+qmFzY+fKfJf/5h0ZinFlKuMTYHu0YtfVQSMNqc7zwxPVFWGUR9Wgi0Rus4zsE2fOB/XBK4A+p5CsegcS3lBZ9rcKqCW7eVPzbsZ14QswC1RfW5KT1IPzvf1aCa+AiYybJXXDQvZGxnmSauXtfhJ2GHADjL4EFUzkRai9z3rrue1ljt4UQK1ASb/2ftYmy/se0AXbwbpm14/1jqdxHYvuPtJvWXa/QC/p4/xKZCy7mJiprRUS5pQA9',
  'referer': 'https://www.scan.co.uk/',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

currentProducts = pd.DataFrame([])
response = requests.get(url, headers=headers)  
responseJson = html_to_json.convert(str(response))
data = response.json() 

currentProducts = currentProducts.append(pd.json_normalize(data['productColumns']))  
day = date.today()

currentProducts.to_csv(day + " scanProducts.csv")


"""
headers = { 
  'Accept': 'application/json',     
  'Content-Type': 'application/json',
  'authority': 'www.scan.co.uk',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'S=IsH8jY1PjjgbqDsm08rNveicWRgcfIT9wnFEvFNuoYeNNI3sv7odRcfapy/bBE0NwlmE80Bg6amZjxqXZxzzUQ==; DS=rQM7pITbDJIt2Gq+KcfL3h8QSuJafE634FjJHU2jXVSvIelzfMo8LpbbOI89WTf7wJ8TFVKH+qXWBeC4jugNFA==; R=ZRhQHB5YWjW1EaTGSecimpcD705WXQsBC4CGIGe3JIbn8VsKrVUAos3ORQpOApS579M9z25UkW/BFbYJBwzfd5NWD3YcjR03A8N7/L8UMA88vrAR7za/sQc+xtqdDbFbINlCre/3PD9LXbAK54PwxIrw4+B3or4sXjGFFzrp1Hc=; US=7sQJRKUOyY/m+cJknOdUoBlV0MT1cJhNgG5M7S/S7M+sg3rCLRvZFWxO7rRYdYgelAZB3hw9ZucVVcbXxC9chv/5h0ZinFlKuMTYHu0YtfVQSMNqc7zwxPVFWGUR9Wgi0Rus4zsE2fOB/XBK4A+p5CsegcS3lBZ9rcKqCW7eVPzbsZ14QswC1RfW5KT1IPzvf1aCa+AiYybJXXDQvZGxnmSauXtfhJ2GHADjL4EFUzkRai9z3rrue1ljt4UQK1ASxX0Sp/jmZAfo0Sl4u42cCK+WDesh0eWCtvVOkeXTOUaHPe7xLFDgEboGRaOVTYOx; _wt.newReturning=Sat Jan 14 2023 22:46:34 GMT+0000 (Greenwich Mean Time); _wt.newVisitor=Sat Jan 14 2023 22:46:34 GMT+0000 (Greenwich Mean Time); ai_user=K7dsBJaKZp3tq4d3WPSEs/|2023-01-14T22:46:34.554Z; _gcl_au=1.1.959752496.1673736395; _ga=GA1.3.64301033.1673736395; _gid=GA1.3.1586472965.1673736395; _wt.mode-1668725=WT3OAo_B2Jr3hk~; _wt.control-1668725-ta_101SuperClickMenuTake2=WT3iE1XAvFPZE0qSacFdqNxBbdIV6jIqAWyU0HD54O_99UXFXA04lWFlX2BQr6BLEPHjbUmyOUfMQFyrUi4Lb4VlWrBrMURw7BouGmB46yjBve9wqioRVrEFoyMjvqZ4jREHLd5unvsOSBWqLvpdZv8oGkHurvbJsErrveAniCJNOxxjirZz-LfyjUq4DxTw92tOXUQRnzUPjTDdbLwXZD0TzxUH1Yzf6n-EIDh7rdsTikgYsHFrmjTuaqG8FMHOvM0uT-lBeHZ6wHiuiOy; __cf_bm=1W1VJUuFAgUhU3TgGZgZJi5mRpNzi0JzwFMbVjHys_w-1673736394-0-AbBLiEYpcWuNA+6eYZhBB1KN5U7C0bSYJ4ChfHrV58xkIKd+9m5pall40QGU3LyDEu2mkEpnBAs+nsWtN/xc3iby78j6l8I6Nt3Uss+IT7jiZRkz3ZY3U380OXPHyUgcovZKZicNocGmgRlCfC8kLjU=; cookpol=3; _fbp=fb.2.1673736397284.2065341474; _wt.user-1668725=WT3h9XZi-3sVANqUqDMqoBqSv6FHbvMIyi_l8fNSe1PmHuLSOJM0U8ipkGT1PoRhw4DgYE2AZdcOTBC-eEAZn_adnXpacroCcEJtHtHK1Q6tBIyvbMdUddKnQBWD-3wLpmgVhoDj16jdLzmFuMVc5JDgWLE4dfwp6FoYlByW1HfZhRF-0fce2LScO-8rZOegN-itlXLfo7n66Gsyq4KyRl4QxfLmRE~; ai_session=ePNVr/5Ria9hgWu26upfJv|1673736394609|1673736397394; DS=xKQjaV9QQiz2dVv93OgZYHF5qhSPltmEntQjJsLBI5EsYQQ3nz5JlAIqtLecSpx8W84BrVt6YhHZsmNn4yNWzQ==; S=a7QBx8aoqik3q2/xeWUMdu5jw4MQ5b1W3zhL/657qfZ145kvQGT3mTm79YZ43MYI8hkgfyBuAOM5oCeya24x5Q==; US=7sQJRKUOyY/m+cJknOdUoBlV0MT1cJhNgG5M7S/S7M+sg3rCLRvZFWxO7rRYdYge2x87lZv3PB+qmFzY+fKfJf/5h0ZinFlKuMTYHu0YtfVQSMNqc7zwxPVFWGUR9Wgi0Rus4zsE2fOB/XBK4A+p5CsegcS3lBZ9rcKqCW7eVPzbsZ14QswC1RfW5KT1IPzvf1aCa+AiYybJXXDQvZGxnmSauXtfhJ2GHADjL4EFUzkRai9z3rrue1ljt4UQK1ASb/2ftYmy/se0AXbwbpm14/1jqdxHYvuPtJvWXa/QC/p4/xKZCy7mJiprRUS5pQA9',
  'referer': 'https://www.scan.co.uk/',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

currentProducts = pd.DataFrame([])
url = f"https://www.scan.co.uk/" 
r = requests.get(url, headers=headers)  
data = r.json() 
currentProducts = currentProducts.append(pd.json_normalize(data['productColumns']))  
day = date.today()

currentProducts.to_csv(day + " scanProducts.csv")





"""