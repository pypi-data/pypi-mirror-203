# async-rotating-proxy
Run an API on your local machine that reroutes traffic through rotating proxies.

- Useful with pyppeteer and selenium
- Built on FastAPI and aiohttp
- Switch proxies on every request

## Installation
`pip install async_rotating_proxy`

## Usage
Usage is simple. Just start the API, format the URL, and send requests.
```
# Instantiating ProxyAPI class launches the API on localhost
proxy_api = ProxyAPI([proxy1:port, proxy2:port, proxy3:port],
                      proxy_username='my_auth_cred',
                      proxy_password='my_auth_cred',
                      port=9001)

# Encode and format the URL to get
# This prepends the localhost address and encodes the URL
url = 'http://checkip.dyndns.org/' 
formatted_url = proxy_api.format_url(url)

# Visit the formatted URL using preferred method
# I use pyppeteer in this example
browser = await pyppeteer.launch()
page = await browser.newPage()
await page.goto(formatted_url)
```


## Purpose
The article referenced below sums it up pretty well:
"The chrome browser does not support fain-grained proxy configuration out of the box. Therefore, the following use cases are not possible when using puppeteer in combination with Google Chrome:

    Using different proxies for different tabs/windows
    Switching proxies without restarting the browser

This is a bit annoying, because restarting the entire browser is an expensive operation in terms of computational resources. The chrome restart takes up to two seconds (depending on the system). We ideally want to switch proxies whenever the need arises without restarting the entire chrome process. This is a common requirement when scraping websites in scale."

## Reference
https://incolumitas.com/2020/12/20/dynamically-changing-puppeteer-proxies/
