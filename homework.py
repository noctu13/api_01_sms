import requests, os, time
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': '5.92',
        'fields': 'online',
        'access_token': os.getenv('ACCESS_TOKEN')
    }
    status = requests.post('https://api.vk.com/method/users.get', params=params).json()['response'][0]['online']
    return status


def sms_sender(sms_text):
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.getenv('NUMBER_TO'),
        from_=os.getenv('NUMBER_FROM'),
        body=sms_text
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
