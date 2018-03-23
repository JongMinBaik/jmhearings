#account/forms.py

from django import forms
from .models import Profile
from model_utils import Choices
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras


class profileForm(ModelForm):
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


    check_disability = forms.ChoiceField(
        choices=[
                (D_CHECK_TRUE, '청각 장애 있음'),
                (D_CHECK_FALSE, '청각 장애 없음'),
            ],
        )
    job = forms.ChoiceField(
        choices=[
                (JOB1, '중등 미만'),
                (JOB2, '중학생'),
                (JOB3, '고등학생'),
                (JOB4, '대학생'),
                (JOB5, '기타'),
        ]
    )
    birth_date = forms.DateField(widget=extras.SelectDateWidget)

    class Meta:
        model = Profile
        fields = ('check_disability', 'job', 'birth_date')


class addUserMultiForm(MultiModelForm):
    form_classes = {
        'user':UserCreationForm,
        'profile':profileForm,
    }
