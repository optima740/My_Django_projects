from django import forms
# формы.

class LoginForm(forms.Form):
    # форма для аутентификации пользователей через базу данных
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # PasswordInput используется для отрисовки HTML-элемента
    # input, включая атрибут type="password"
