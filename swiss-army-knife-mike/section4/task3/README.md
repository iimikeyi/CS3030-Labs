Task 3 - Site Checker 

The current script checks sites one at a time. Each requests.get() call waits for a reposnse before moving to the next URL> WIth 3 sites this is fine, but with 1000 sites it could take minutes if any sites are slow or timing out. 

This fix is asynchronous execution using Pythons asyncio library and aiohttp instead of requests. Async lets the script send all 1000 requests at nearly the same time and collect responses as they arrive rather than wating one by one. 

The difference: 
Synchronous: check site 1, wait, check site 2 wait, check site 3 
Asynchronous: send all requests at once, collect results as they come back. 

For 1000 sites this could reduce runtime several minutes down to a few seconds. 
