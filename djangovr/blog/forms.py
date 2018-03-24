from django import forms
from .models import Request, Join, Helpdesk
from model_utils import Choices

class PostForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'ex. 홍길동'}))
    phone_num = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. 0101234xxxx'}))
    lec = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. 구석기 시대와 신석기 시대'}))
    lec_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. www.exampleurl.com'}))
    lec_teacher = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. 설민석'}))
    lec_company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. 메가스터디'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ex. hearings.info@gmail.com'}))
    class Meta:
        model = Request
        fields = ('username', 'phone_num', 'email', 'lec', 'lec_teacher', 'lec_url', 'lec_company', 'description',)


class JoinForm(forms.ModelForm):
    j_username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'ex. 홍길동'}))
    j_phone_num = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex. 0101234xxxx'}))
    j_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ex. hearings.info@gmail.com'}))
    class Meta:
        model = Join
        fields = ('j_username', 'j_phone_num', 'j_email')


class StatusForm(forms.ModelForm):
    STEP1 = '모집중'
    STEP2 = '준비중'
    STEP3 = '제작중'
    STEP4 = '배포완료'
    STEP_STOPPED = '제작중단'

    status = forms.ChoiceField(
        choices=[
            (STEP1, '모집중'),
            (STEP2, '준비중'),
            (STEP3, '제작중'),
            (STEP4, '배포완료'),
            (STEP_STOPPED, '제작중단'),
        ],
    )
    class Meta:
        model = Request
        fields = ('status',)


class HelpdeskPostForm(forms.ModelForm):
    LOCK = '잠금'
    UNLOCK = '전체공개'

    LOCK_CHECK = [
        (LOCK, '잠금'),
        (UNLOCK, '전체공개'),
    ]

    h_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    h_lock_checked = forms.ChoiceField(
        choices=[
            (LOCK, '잠금'),
            (UNLOCK, '전체공개'),
        ],
    )
    h_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Helpdesk
        fields = ('h_title', 'h_lock_checked', 'h_description',)
