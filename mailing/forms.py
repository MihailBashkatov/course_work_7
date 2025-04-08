from django import forms

from mailing.models import Receiver, Message, Mailing, Attempt
from users.models import User


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

    def __init__(self, *args, user_id=None, path_info=None, **kwargs):
        super(ReceiverForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.path_info = path_info #getting path


        if 'receiver_update' in self.path_info : #if path is for update client, then email fields becomes inactive
            self.fields['email'].disabled = True # Make email field non-editable for editing client
            self.fields['email'].help_text = None # Remove help_text for editing client

    def clean(self):
        """ Logic for creating only unique receivers email per user """
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = User.objects.get(id=self.user_id)

        # Gives possibility to edit client info, but not client's email
        if user.adder.filter(email=email).exists() and 'receiver_update' not in self.path_info:
            self.add_error('email', 'You already have the client with inserted email. Please, either insert another email or edit client')



class MessageForm(forms.ModelForm):
    """Form for Message Model """
    class Meta:
        model = Message
        fields = ['title', 'message']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-input'}),
            'message':forms.Textarea(attrs={'cols':50, 'rows' :5}),
        }

    def __init__(self, *args, user_id=None, path_info=None, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.path_info = path_info  # getting path

        if 'message_update' in self.path_info:  # if path is for update message, then title field becomes inactive
            self.fields['title'].disabled = True  # Make email field non-editable for editing message
            self.fields['title'].help_text = None  # Remove help_text for editing message


    def clean(self):
        """ Logic for creating only unique Title per user for the message """
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        user = User.objects.get(id=self.user_id)

        # Gives possibility to edit message info, but not message's title
        if user.message_sender.filter(title=title).exists() and 'message_update' not in self.path_info:
            self.add_error('title', 'You already have such Title. Please, either insert another title or edit current message')





class MailingForm(forms.ModelForm):
    """Form for Mailing Model """
    class Meta:
        model = Mailing
        fields = ['status',  'message', 'receivers']

        widgets = {
            'status':forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, path_info=None, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        self.path_info = path_info
        print(self.path_info)
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['receivers'].widget = forms.CheckboxSelectMultiple()
        self.fields['receivers'].queryset = Receiver.objects.filter(receiver_adder = self.user_id)
        self.fields['message'].widget = forms.RadioSelect()
        self.fields['message'].queryset = Message.objects.filter(message_sender = self.user_id)


    def clean(self):
        """ Logic for creating only unique Mailing per user """
        cleaned_data = super().clean()
        title = cleaned_data.get('message')
        user = User.objects.get(id=self.user_id)

        #Gives possibility to edit mailing info, but not mailing's title
        if user.sender.filter(message__title=title).exists() and 'mailings_update' not in self.path_info:
            self.add_error('message', 'You already have Mailing with such title. Please, choose another mailing or edit current one')







class AttemptForm(forms.ModelForm):
    """Form for Attempt Model """
    class Meta:
        model = Attempt
        fields = ['mailing']
