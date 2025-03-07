from django import forms

from mailing.models import Receiver, Message, Mailing, Attempt


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
        fields = ['status',  'message', 'receivers']

        widgets = {
            'status':forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['receivers'].widget = forms.CheckboxSelectMultiple()
        self.fields['receivers'].queryset = Receiver.objects.filter(receiver_adder = user)
        self.fields['message'].widget = forms.RadioSelect()
        self.fields['message'].queryset = Message.objects.filter(message_sender = user)

class AttemptForm(forms.ModelForm):
    """Form for Attempt Model """
    class Meta:
        model = Attempt
        fields = ['mailing']
