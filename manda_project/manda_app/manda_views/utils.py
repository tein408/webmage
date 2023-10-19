import random
import string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_temp_password(length=8):
    characters = string.ascii_letters + string.digits
    temp_password = ''.join(random.choice(characters) for _ in range(length))
    return temp_password

def send_temp_password_email(user, temp_password):
    subject = '[웹법사와 함께 만드는 만다라트] 임시비밀번호 안내'
    message = f'입력하신 비밀번호는 암호화 되어있어 임시로 생성된 비밀번호를 안내해 드립니다.\n\n임시비밀번호: {temp_password}\n\n안내해 드리는 비밀번호로 로그인 하시기 바랍니다.'
    from_email = 'webmage_manda@naver.com'
    recipient_list = [user.email]
    print(recipient_list)

    EmailMessage(subject=subject, body=message, to=recipient_list, from_email=from_email).send()