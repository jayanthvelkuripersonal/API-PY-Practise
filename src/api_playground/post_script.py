import requests
def get_posts():
   url = 'https://jsonplaceholder.typicode.com/posts' 
   # data = {
   #     'key1': 'value1',
   #     'key2': 'value2'
   # }
   response = requests.get(url)
   if response.status_code == 200:
      print(f'Status Code: {response.status_code}')
      print(f'Response Body: {response.text}')
   else:
      print(f'Status Code: {response.status_code}')
      print(response.reason)
get_posts()