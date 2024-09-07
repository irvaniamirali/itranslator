from itranslator.asyncio import Translator
from asyncio import run

translator = Translator()


async def main():
    result = await translator.translate("Hello", "fa")
    print(result)

run(main())
