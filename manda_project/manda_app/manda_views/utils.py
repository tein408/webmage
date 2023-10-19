import random
import string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

User = get_user_model()

def generate_temp_password(length=8):
    characters = string.ascii_letters + string.digits
    temp_password = ''.join(random.choice(characters) for _ in range(length))
    return temp_password

def send_temp_password_email(user, temp_password):
    title = '[웹법사와 함께 만드는 만다라트] 임시비밀번호 안내'
    content = {
        "message": temp_password,
    }
    receive_email = [user.email]
    from_email = 'Manda 웹법사 <webmage_manda@naver.com>'
    emailContent = render_to_string('email.html', content)

    emailObject = EmailMessage(subject=title, body=emailContent, to=receive_email, from_email=from_email)
    emailObject.content_subtype = "html"
    emailObject.send()