from django import forms

from mailing.models import Receiver


class ReceiverForm(forms.ModelForm):
    """Form  """
    class Meta:
        model = Receiver
        fields = ['name', 'email', 'description']

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-input'}),
            'email':forms.TextInput(attrs={'class': 'form-input'}),
            'description':forms.Textarea(attrs={'cols':50, 'rows' :5}),
        }