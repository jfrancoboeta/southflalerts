from django import forms
from southflalerts.models import EmpInsert
from southflalerts.models import EmpDelete
from captcha.fields import ReCaptchaField
from django.core.exceptions import NON_FIELD_ERRORS

# create a ModelForm
class EmpInsertForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = EmpInsert
        fields = "__all__"
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "These %(field_labels)s are already subscribed.",
            }
        }

class EmpDeleteForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = EmpDelete
        fields = "__all__"

class Contact(forms.Form):
    email = forms.CharField(max_length = 50)
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(max_length = 1000)
    captcha = ReCaptchaField()