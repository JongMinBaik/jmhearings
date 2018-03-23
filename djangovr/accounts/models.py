from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    JOB1 = '중등 미만'
    JOB2 = '중학생'
    JOB3 = '고등학생'
    JOB4 = '대학생'
    JOB5 = '기타'

    JOB_STATUS = [
        (JOB1, '중등 미만'),
        (JOB2, '중학생'),
        (JOB3, '고등학생'),
        (JOB4, '대학생'),
        (JOB5, '기타'),
    ]

    D_CHECK_TRUE = '청각 장애 있음'
    D_CHECK_FALSE = '청각 장애 없음'

    DISABILITY_CHECK = [
        (D_CHECK_TRUE, '청각 장애 있음'),
        (D_CHECK_FALSE, '청각 장애 없음'),
    ]

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    check_disability = models.CharField(choices=DISABILITY_CHECK, max_length=20,)
    job = models.CharField(choices=JOB_STATUS, max_length=20, default=JOB5, blank=False)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
