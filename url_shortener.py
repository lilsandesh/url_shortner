# url_shortener.py

class URLShortener:
    def __init__(self, base_url="http://127.0.0.1:6000/"):
        self.base_url = base_url
        self.url_dict = {}
        self.custom_aliases = {}

    def shorten_url(self, original_url, custom_alias=None):
        if custom_alias:
            if custom_alias in self.custom_aliases:
                raise ValueError("Custom alias already in use.")
            self.custom_aliases[custom_alias] = original_url
            return self.base_url + custom_alias
        else:
            short_key = self._generate_short_key()
            self.url_dict[short_key] = original_url
            return self.base_url + short_key

    def _generate_short_key(self):
        short_key = str(len(self.url_dict) + 1)
        while short_key in self.url_dict or short_key in self.custom_aliases:
            short_key = str(int(short_key) + 1)
        return short_key

    def get_original_url(self, short_key):
        if short_key in self.custom_aliases:
            return self.custom_aliases[short_key]
        return self.url_dict.get(short_key, None)
