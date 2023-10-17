from django.db import models
from .models import MandaMain  # MandaMain 모델을 가져오기
from .models import MandaSub
from django.contrib.auth.models import User  # User 모델을 가져오기

# Create your models here.

#Feed 테이블
class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True)  # feed_id를 기본 키로 설정
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user_id 외래 키
    cont_id = models.ForeignKey(MandaContent, on_delete=models.CASCADE)  # cont_id 외래 키
    main_id = models.ForeignKey(MandaMain, on_delete=models.CASCADE)  # main_id 외래 키
    sub_id = models.ForeignKey(MandaSub, on_delete=models.CASCADE)  # sub_id 외래 키
    feed_contents = models.TextField()  # 피드 내용
    feed_image = models.ImageField(upload_to='feed_images/')  # 이미지를 저장할 경로
    created_at = models.DateTimeField(auto_now_add=True)  # 피드 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 피드 업데이트일
    feed_hash = models.CharField(max_length=255)  # 피드 해시값, 필요에 따라 길이 조절 가능

    def __str__(self):
        return self.feed_contents

#핵심목표
class MandaMain(models.Model):
    main_id = models.AutoField(primary_key=True)  # 기본 키
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # 외래키로 User 모델 연결
    success = models.BooleanField()  # 성공 여부 (True/False)
    main_title = models.CharField(max_length=255)  # 메인 타이틀, 필요에 따라 길이 조절 가능

    def __str__(self):
        return self.main_title

#세부목표
class MandaSub(models.Model):
    sub_id = models.AutoField(primary_key=True)  #기본 키
    main_id = models.ForeignKey(MandaMain, on_delete=models.CASCADE)  # MandaMain 모델과 외래키로 연결
    success = models.BooleanField()  # 성공 여부 (True/False)
    sub_title = models.CharField(max_length=20)  # 서브 타이틀, 최대 길이 20

    def __str__(self):
        return self.sub_title

#실천목표
class MandaContent(models.Model):
    cont_id = models.AutoField(primary_key=True)  # 기본 키
    sub_id = models.ForeignKey(MandaSub, on_delete=models.CASCADE)  # 외래키로 MandaSub와 연결
    success = models.BigIntegerField()  # 성공 여부, bigint 타입
    content = models.CharField(max_length=20)  # 콘텐츠, 최대 길이 20

    def __str__(self):
        return self.content
