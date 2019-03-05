from django.shortcuts import render, HttpResponse, redirect
import json
from forum import models
from forum.forms import UserForm,RegisterForm
# Create your views here.


def forum(req):

    return render(req, "test.html")


def login(req):
    if req.session.get('is_login', None):
        redirect('/index/')
    if req.method == "POST":
        login_form = UserForm(req.POST)
        msg = ""
        if login_form.is_valid():
            userId = login_form.cleaned_data['username']
            userPsd = login_form.cleaned_data['password']
            try:
                user = models.UserInfo.objects.get(user_Id=userId)
                if user.user_passwd == userPsd:
                    req.session['is_login'] = True
                    req.session['user_id'] = user.user_Id
                    req.session['user_name'] = user.user_name
                    return redirect('/index/')
                else:
                    msg = "密码不正确！"
            except Exception as e:
                msg = '用户不存在！'
        return render(req, "login.html", locals())
    login_form = UserForm()
    return render(req, "login.html", locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def register(req):
    # if req.session.get('is_register', None):
    #     del req.session['is_register']

    if req.session.get('is_login', None):
        return redirect("/index")
    if req.method == "POST":
        register_form = RegisterForm(req.POST)
        msg = ''
        if register_form.is_valid():
            reg_username = register_form.cleaned_data['reg_username']
            reg_sex = register_form.cleaned_data['reg_sex']
            reg_occ = register_form.cleaned_data['reg_occupation']
            reg_userId = register_form.cleaned_data['reg_userId']
            reg_passwd1 = register_form.cleaned_data['reg_passwd1']
            reg_passwd2 = register_form.cleaned_data['reg_passwd2']
            reg_userEmail = register_form.cleaned_data['reg_email']
            if reg_passwd1 != reg_passwd2:
                msg = '两次密码不一致，请重新输入！'
                return render(req, 'register.html', locals())
            else:
                sameuserid = models.UserInfo.objects.filter(user_Id=reg_userId)
                if sameuserid:
                    msg = '用户名已存在！'
                    return render(req, 'register.html', locals())
                sameusername = models.UserInfo.objects.filter(user_name=reg_username)
                if sameusername:
                    msg = '账号已存在！'
                    return render(req, 'register.html', locals())
                try:
                    status = models.UserInfo.objects.create(
                     user_name=reg_username, user_sex=reg_sex, user_occupation=reg_occ,
                        user_Id=reg_userId, user_passwd=reg_passwd1, user_email=reg_userEmail
                    )
                    msg = '注册成功!请登录!'
                    login_form = UserForm()
                    return render(req, "login.html", locals())
                except :
                    msg = '注册失败'
                    return render(req, 'register.html', locals())
    register_form = RegisterForm()
    return render(req, 'register.html', locals())


def index(req):
    # username = req.COOKIES.get("username")
    # if username:
    #     return render(req, 'index.html', {"username": username})
    # else:
    #     return redirect('/login')

    return render(req, "index.html")


def login_test(req):
    if req.method == "POST":
        userId = req.POST.get("log_user")
        userPsd = req.POST.get("log_passwd")
        print(req.POST)
        status = models.UserInfo.objects.filter(user_Id=userId, user_passwd=userPsd)
        print(userId)
        print(userPsd)
        if status:
            rep = render(req, 'index.html')
            return rep
        else:
            return HttpResponse(json.dumps("failed"))
    return render(req, "test.html")


def check_user(req):
    check_id = req.POST.get('test_id')
    status = models.UserInfo.objects.filter(user_Id=check_id)
    if status:
        return HttpResponse(1)
    return HttpResponse(0)