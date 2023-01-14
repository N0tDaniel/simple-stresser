import requests
import random

# list of proxies
proxies = [
    "http://proxy1:port",
    "http://proxy2:port",
    "http://proxy3:port",
    # ...
]

# target server
target_url = "http://example.com"

# number of requests to send
num_requests = 1000

# send requests
for i in range(num_requests):
    # select a random proxy
    proxy = random.choice(proxies)
    # send the request
    response = requests.get(target_url, proxies={"http": proxy, "https": proxy})
    # check the response status
    if response.status_code != 200:
        print(f"[ERROR] Request {i} failed with status code {response.status_code}")
    else:
        print(f"[SUCCESS] Request {i} sent successfully")
