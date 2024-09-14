from telethon.sync import TelegramClient

api_id = 23262291
api_hash = '77c460c8142ca13f32c27ac389db2e35'
phone_number = '+972556683729'

client = TelegramClient('+972556683729', api_id, api_hash)
async def main():
    await client.connect()
    
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        code = input('📲 Enter the code you received: ')
        try:
            await client.sign_in(phone_number, code)
        except telethon.errors.SessionPasswordNeededError:
            password = input('🔐 2FA enabled, enter your password: ')
            await client.sign_in(password=password)

    print("✅ Logged in successfully!")

with client:
    client.loop.run_until_complete(main())
