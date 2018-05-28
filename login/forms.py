from django import forms
# from captcha.fields import CaptchaField

# 自定义类必须继承forms.Form类
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))   # .CharField：表示字符串类；label=：表示转义字段；widget=forms.TextInput：表示文本小部件；attrs={'class': 'form-control'})：用于美化小部件
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # widget=forms.PasswordInput：表示密码小部件

    # captcha = CaptchaField(label='验证码')


# class RegisterForm(forms.Form):
#     gender = (
#         ('male', '男'),
#         ('female', '女'),
#     )
#     username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='邮箱', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     sex = forms.ChoiceField(label='性别', choices=gender)
#     captcha = CaptchaField(label='验证码')
