from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, error_messages={'required': 'This field is required'})
    last_name = forms.CharField(required=True, error_messages={'required': 'This field is required'})
    email = forms.EmailField(required=True, error_messages={'required': 'This field is required'})
    phone = forms.CharField(required=True, error_messages={'required': 'This field is required'})
    country = forms.CharField(required=True, error_messages={'required': 'This field is required'})
    message = forms.CharField(required=True, error_messages={'required': 'This field is required'})

    class Meta:
        fields = '__all__.'
