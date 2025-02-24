from django import forms

from mailing.models import Receiver, Message, Mailing


class ReceiverForm(forms.ModelForm):
    """Form for Receiver Model  """
    class Meta:
        model = Receiver
        fields = ['name', 'email', 'description']

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-input'}),
            'email':forms.TextInput(attrs={'class': 'form-input'}),
            'description':forms.Textarea(attrs={'cols':50, 'rows' :5}),
        }

class MessageForm(forms.ModelForm):
    """Form for Message Model """
    class Meta:
        model = Message
        fields = ['title', 'message']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-input'}),
            'message':forms.Textarea(attrs={'cols':50, 'rows' :5}),
        }

class MailingForm(forms.ModelForm):
    """Form for Mailing Model """
    class Meta:
        model = Mailing
        fields = ['first_sending', 'end_sending', 'status',  'message', 'receivers']

        widgets = {
            'receivers': forms.TextInput(attrs={'class': 'form-input'}),
            'status':forms.TextInput(attrs={'class': 'form-input'}),
            'message':forms.Textarea(attrs={'cols':50, 'rows' :5}),
        }