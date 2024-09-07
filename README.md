# ITranslator
Text translation package based on Google Translate API

### Sync Example
```python
from itranslator import Translator

translator = Translator()

translated_text = translator.translate(query='hi there', to_lang='fa')
print(translated_text)
```

### Async Example
```python
from itranslator.asyncio import Translator
from asyncio import run

translator = Translator()


async def main():
    translated_text = await translator.translate("Hello", "fa")
    print(translated_text)

run(main())
```

### Install & Update
```bash
pip install itranslator -U
```
### License
ITranslator is released under the GPL-3.0 License. See the bundled [LICENSE](https://github.com/irvaniamirali/itranslator/blob/main/LICENSE) file for details.
