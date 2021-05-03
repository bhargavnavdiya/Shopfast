from django import forms
from .models import contactUs,feedbackForm

class contactUs(forms.ModelForm):
    firstName= forms.CharField(error_messages={'required':'Please enter your First name'})
    lastName= forms.CharField(error_messages={'required':'Please enter your Last name'})
    emailId= forms.CharField(error_messages={'required':'Please enter your Email ID'})
    commentUser= forms.CharField(error_messages={'required':'Please enter your Comment'})

    class Meta:
        model=contactUs
        fields=('firstName','lastName','emailId','commentUser',)


class feedbackForm(forms.ModelForm):
    ratings=forms.CharField(error_messages={'required':'Rate us'})
    experience=forms.CharField(error_messages={'required':'Please tell your experience with us'})
    suggestion=forms.CharField(error_messages={'required':'Please give your suggestion to us'})

    class Meta: 
        model=feedbackForm
        fields=('ratings','experience','suggestion')