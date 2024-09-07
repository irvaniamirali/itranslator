from itranslator.errors import *

import urllib.parse
import json
import html

from user_agent import generate_user_agent
from re import findall
from httpx import AsyncClient, codes

from typing import Optional

client = AsyncClient()


class Translator:

    def __init__(self, user_agent: Optional[str] = None) -> None:
        self.user_agent = user_agent or generate_user_agent()

    async def translate(
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
        request = await client.request(
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

    @property
    def languages(self):
        """
        Show all translatable languages.
        More detailed and complete viewing of languages in https://en.wikipedia.org/wiki/ISO_639-1
        """
        languages = open('itranslator/languages.json', 'r')
        return json.load(languages)

    @property
    def lang_codes(self):
        return dict(map(reversed, self.languages.items()))
