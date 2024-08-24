import asyncio
from sys import stdout
from logging import basicConfig, INFO

from handlers.MessageHandler import main

if __name__ == '__main__':
    basicConfig(level=INFO, stream=stdout)
    asyncio.run(main())
