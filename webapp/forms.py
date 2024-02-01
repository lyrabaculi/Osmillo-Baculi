from django import forms
from .models import Donation
from .models import UserAccount



class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'gender', 'address', 'image', 'password1', 'password2']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['email', 'password1']
        widgets = {
            'password1': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')

        if email and password1:
            user = authenticate(email=email, password=password1)
            if user is None or not user.is_active:
                raise forms.ValidationError("Invalid email or password")
        return cleaned_data
