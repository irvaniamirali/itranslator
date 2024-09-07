from itranslator.errors import *

import urllib.parse
import html

from user_agent import generate_user_agent
from re import findall
from httpx import Client, codes

from typing import Optional

client = Client()


class Translator:

    def __init__(self, user_agent: Optional[str] = None) -> None:
        self.user_agent = user_agent or generate_user_agent()

    def translate(
            self,
            query: str,
            to_lang: Optional[str] = 'auto',
            from_lang: Optional[str] = 'auto'
    ) -> str:
        """
        Translates a text from one language to another using the Google Translate API.
        :param query:
            The text to translate.
        :param to_lang:
            The language to translate the text to. Defaults to "auto".
        :param from_lang:
            The language of the text to translate. Defaults to "auto".
        :return:
            The translated
        """
        url = f'https://translate.google.com/m?tl=%s&sl=%s&q=%s'
        request = client.request(
            method='GET', url=url % (to_lang, from_lang, urllib.parse.quote(query)),
            headers={
                'User-Agent': self.user_agent
            }
        )
        try:
            if request.status_code != codes.OK:
                raise ConnectionError(f'A connection problem occurred\nstatus code: {request.status_code}')
            else:
                translated_text = findall(r'(?s)class="(?:t0|result-container)">(.*?)<', request.text)
                return html.unescape(translated_text[0])
        except Exception as error:
            raise TranslatorException(f'An unknown problem has occurred:\n{error}')
