import random
import string
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_temp_password(length=8):
    characters = string.ascii_letters + string.digits
    temp_password = ''.join(random.choice(characters) for _ in range(length))
    return temp_password

def send_temp_password_email(user, temp_password):
    subject = 'Temporary Password'
    message = f'Your temporary password is: {temp_password}'
    from_email = 'noreply@example.com'  # 이메일 발신자 주소
    recipient_list = [user.email]  # 사용자의 이메일 주소

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)