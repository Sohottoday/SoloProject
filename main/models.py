from django.db import models

# Create your models here.
class main(models.Model):
    upso_num = models.CharField(max_length=30)  # 업소일련번호
    upso_name = models.CharField(max_length=40) # 업소명
    dong_name = models.CharField(max_length=20) # 동명
    address = models.TextField()    # 주소
    area = models.FloatField()  # 면적
    tell_num = models.TextField(max_length=20)  # 전화번호
    upjong = models.CharField(max_length=20)    # 업종
    code = models.CharField(max_length=30)  # 품목코드
    item = models.CharField(max_length=30)  # 품 목
    price = models.IntegerField()   # 가격
    check_date = models.CharField(max_length=20)    # 점검일자
    gu_name = models.CharField(max_length=10)
