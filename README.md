# ITranslator
A Python package to use in translating texts based on api

## Simpale Example
```python
import itranslator, asyncio

translator = itranslator.translator()
async def main():
    translated_text = await translator.translate(query='hi there', to_lang='fa')
    print(translated_text)

asyncio.run(main())
```

### License
ITranslator is released under the GPL-3.0 License. See the bundled [LICENSE](https://github.com/metect/itranslator/blob/main/LICENSE) file for details.
