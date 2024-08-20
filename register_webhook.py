import json

import Config
from Config import TOKEN

import asyncio

import aiohttp

DOMAIN = Config.BASE_WEBHOOK_URL

url = {
    "url": "https://" + DOMAIN + Config.WEBHOOK_PATH
}

API_URL = 'https://api.telegram.org/bot%s/setWebhook' % TOKEN


async def register_webhook():
    headers = {
        'Content-Type': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL,
                                data=json.dumps(url),
                                headers=headers) as resp:
            try:
                assert resp.status == 200
            except Exception as e:
                return {'success':False, 'message':'Возникла ошибка'}
            result = await resp.json()
            return {'success': result['result'], 'message': result['description']}


if __name__ == '__main__':
    response = asyncio.run(register_webhook())
    print(response['message'])
    if response['success']:
        exit(0)
    else:
        exit(1)
