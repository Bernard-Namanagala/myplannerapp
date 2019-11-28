from django import forms


class LoginForm(forms.Form):
    Email_or_Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'id': 'sign-in-email'
                                                                                                       '-username'}),
                                        max_length=125)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'sign-in-password'}))


class SignupForm(forms.Form):
    Email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'id': 'sign-up-email'}),
                            max_length=125)
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'id': 'username'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id': 'sign-up-password'}))


class TaskToAddForm(forms.Form):
    task_to_add = forms.CharField(widget=forms.TextInput(attrs={'name': 'task_to_add', 'placeholder':
                                  'type the task you want to add'}), max_length=255)
