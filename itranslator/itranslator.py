import requests
import urllib.parse
import user_agent
import html
import re


class translator:

    def __init__(self, action: str = 'google'):
        self.actions: list = [
            'google', 'bing'
        ]
        self.action: str = action

    async def translate(self, query: str, to_lang: str = 'auto', from_lang: str = 'auto') -> str:
        url: str = 'https://translate.google.com/m?tl=%s&sl=%s&q=%s'
        request = requests.request(
            method='POST', url=url % (to_lang, from_lang, urllib.parse.quote(query)),
            headers={
                'User-Agent': user_agent.generate_user_agent()
            }
        )
        if request.status_code != requests.codes.ok:
            raise ConnectionError('A connection problem occurred', __file__)
        else:
            translated_text = re.findall(r'(?s)class="(?:t0|result-container)">(.*?)<', request.text)
            return html.unescape(translated_text[0])

    @property
    def LANGUAGES(self):
        pass
