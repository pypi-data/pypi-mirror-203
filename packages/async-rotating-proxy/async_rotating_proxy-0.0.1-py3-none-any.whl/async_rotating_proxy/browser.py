"""
This module provides a subclass of pyppeteer.Browser which
stores proxy data, authentication, and has a proxy_get() method
for routing page requests through the proxy server.
"""

from pyppeteer import Browser


class ProxyBrowser(Browser):
    """Subclass of pyppeteer.Browser with proxy rotation.

    It works by running an API on localhost which routes traffic through a proxy.
    Each request is routed through a random proxy in the proxies attribute.

    Args:
        proxies (list[str]): List of proxies to rotate through in ip:port form
        proxy_username (str | None): Username for proxy authentication if applicable
        proxy_password (str | None): Password for proxy authentication if applicable
        proxy_api_port (int): The port on localhost where the proxy API is running
    """
    def __init__(
            self, 
            proxies: list[str], 
            proxy_username: str | None = None,
            proxy_password: str | None = None,
            proxy_api_port: int = 8000
        ):
        super.__init__(self)
        self.proxies = proxies
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.proxy_api_port = proxy_api_port


