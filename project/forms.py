from django import forms


class ContactForm(forms.Form):
    you = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'feedback-input', 'placeholder': 'ФИО'}), label='')
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
            attrs={'class': 'feedback-input', 'placeholder': 'E-mail'}), label='')
    message = forms.CharField(widget=forms.Textarea(
            attrs={'class': 'feedback-input', 'placeholoder': 'Message'}), required=True, label='')
