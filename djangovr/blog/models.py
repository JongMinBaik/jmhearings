from django.db import models
from django.utils import timezone
from model_utils import Choices


class Request(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True)
    phone_num = models.CharField(max_length=50, blank=True)
    lec = models.CharField(max_length=100, blank=True)
    lec_url = models.CharField(max_length=100, blank=True)
    lec_teacher = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    email = models.EmailField()
    lec_company = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    view_cnt = models.IntegerField(default=0, blank=True)

    # 게시글 상태 모델링
    STEP1 = '모집중'
    STEP2 = '준비중'
    STEP3 = '제작중'
    STEP4 = '배포완료'
    STEP_STOPPED = '제작중단'

    STATUS = [
        (STEP1, '모집중'),
        (STEP2, '준비중'),
        (STEP3, '제작중'),
        (STEP4, '배포완료'),
        (STEP_STOPPED, '제작중단'),
    ]
    status = models.CharField(choices=STATUS, max_length=20, default=STEP1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.lec
