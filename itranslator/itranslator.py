import urllib.parse, requests, json, html, re
import user_agent as _user_agent

from .exceptions import *


class translator:

    def __init__(self, user_agent: str = None):
        self.user_agent = user_agent if user_agent is not None else _user_agent.generate_user_agent()

    async def translate(self, query: str, to_lang: str = 'auto', from_lang: str = 'auto') -> str:
        '''
        Translates a text from one language to another using the Google Translate API.
        :param query:
            The text to translate.
        :param to_lang:
            The language to translate the text to. Defaults to "auto".
        :param from_lang:
            The language of the text to translate. Defaults to "auto".
        :return:
            The translated
        '''
        if len(query) > 3900:
            raise LimitCharacterExceeds('Text exceeds 3900 character limit')

        url: str = f'https://translate.google.com/m?tl=%s&sl=%s&q=%s'
        request = requests.request(
            method='GET', url=url % (to_lang, from_lang, urllib.parse.quote(query)),
            headers={
                'User-Agent': self.user_agent
            }
        )
        try:
            if request.status_code != requests.codes.ok:
                raise ConnectionError(f'A connection problem occurred\nstatus code: {request.status_code}')
            else:
                translated_text = re.findall(r'(?s)class="(?:t0|result-container)">(.*?)<', request.text)
                return html.unescape(translated_text[0])
        except:
            raise TranslatorException('An unknown problem has occurred')

    @property
    def languages(self):
        '''Show all translatable languages.
        More detailed and complete viewing of languages in https://en.wikipedia.org/wiki/ISO_639-1'''
        languages = open('itranslator/languages.json', 'r')
        return json.load(languages)

    @property
    def lang_codes(self):
        return dict(map(reversed, self.languages.items()))
