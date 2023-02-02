# simple-stresser
simple stresser that connects to a list of proxies and sends requests to a target 

The function creates an aiohttp ClientSession, and then creates a list of tasks that each call the send_request function with a random proxy from the proxy list. The tasks are then run in parallel using asyncio.gather.
