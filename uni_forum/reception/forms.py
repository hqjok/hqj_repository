#!/usr/bin/python
# -*-  coding:utf-8  -*-
# @Time   : 2019/2/28  22:16
# @Author : 黄猿
# @File   : forms.py
from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="账号", max_length=64, widget=forms.TextInput(attrs={'class': 'required input-xlarge', 'title': '请输入账号'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'required input-xlarge','title': '请输入密码'}))
    captcha = CaptchaField(label="验证码", error_messages={"invalid": "验证码错误"}, )


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    occupation = (
        ('stu', "学生"),
        ('tea', "教师"),
    )
    reg_username = forms.CharField(label="用户名", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    reg_sex = forms.ChoiceField(label="性别", choices=gender)
    reg_occupation = forms.ChoiceField(label="职业", choices=occupation)
    reg_userId = forms.CharField(label="账号", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    reg_passwd1 = forms.CharField(label="密码", max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control required'}))
    reg_passwd2 = forms.CharField(label="确认密码", max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control required'}))
    reg_email = forms.EmailField(label="email", max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control required'}))
    