from django.shortcuts import render, HttpResponse, redirect
from reception.forms import UserForm, RegisterForm
from reception import models
from my_way import RenderWrite
import json
# Create your views here.


def index(req):
    live_obj = models.Article.objects.filter(articleType__from_type__type="生活区")[:6]
    stu_obj = models.Article.objects.filter(articleType__from_type__type="学术区")[:6]
    req_id = req.session.get("user_uid", None)
    if req_id:
        lift_obj = models.Article.objects.filter(art_author_lift__uid=req_id).values("aid")
    return RenderWrite.render_template( req, "reception/index.html", locals())


def login(req):
    if req.session.get('is_login', None):
        redirect('/reception/index/')
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
                    req.session['user_uid'] = user.uid
                    return redirect('/reception/index/')
                else:
                    msg = "密码不正确！"
            except Exception as e:
                print(e)
                msg = '用户不存在！'

        return RenderWrite.render_template(req, "reception/login.html", locals())
    login_form = UserForm()
    return RenderWrite.render_template(req, "reception/login.html", locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/reception/index/")
    request.session.flush()
    return redirect('/reception/index/')


def register(req):
    if req.session.get('is_login', None):
        return redirect("reception/index")
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
                return RenderWrite.render_template(req, 'reception/register.html', locals())
            else:
                sameuserid = models.UserInfo.objects.filter(user_Id=reg_userId)
                if sameuserid:
                    msg = '账号已存在！'
                    return RenderWrite.render_template(req, 'reception/register.html', locals())
                sameusername = models.UserInfo.objects.filter(user_name=reg_username)
                if sameusername:
                    msg = '用户名已存在！'
                    return RenderWrite.render_template(req, 'reception/register.html', locals())
                try:
                    status = models.UserInfo.objects.create(
                     user_name=reg_username, user_sex=reg_sex, user_occupation=reg_occ,
                        user_Id=reg_userId, user_passwd=reg_passwd1, user_email=reg_userEmail
                    )
                    msg = '注册成功!请登录!'
                    login_form = UserForm()
                    return RenderWrite.render_template(req, "reception/login.html", locals())
                except Exception as e:
                    print(e)
                    msg = '注册失败'
                    return RenderWrite.render_template(req, 'reception/register.html', locals())
    register_form = RegisterForm()
    return RenderWrite.render_template(req, 'reception/register.html', locals())


def base(req):
    sss = "22"
    return render(req, "reception/index1.html", locals())


def article_msg(req):
    artid = req.GET.get("id")
    article_msg = models.Article.objects.get(aid=artid)
    comments_count = len(json.loads(article_msg.art_comment))
    # is_lifted = models.Article.objects.get(art_author_lift__uid=artid)
    # print(is_lifted)
    req_id = req.session.get("user_uid", None)
    print(req_id)
    if req_id:
        is_lifted = models.Article.objects.filter(art_author_lift__uid=req_id, aid=artid)
    return RenderWrite.render_template(req, "reception/article_msg.html", locals())


def check_lift(req):
    lift_count = req.GET.get("lift")
    aid = req.GET.get("art_id")
    symbol = req.GET.get("symbol")
    uid = req.session.get("user_uid")
    # 更新点赞数
    models.Article.objects.filter(aid=aid).update(art_lift=lift_count)
    # 以下更新个人点赞的帖子
    article_obj = models.Article.objects.get(aid=aid)
    user_obj = models.UserInfo.objects.get(uid=uid)
    if symbol == "+":
        article_obj.art_author_lift.add(user_obj)
    else:
        user_obj.article_set.remove(article_obj)
    return HttpResponse("add")


def msg_list(req):
    return render(req, "reception/msg_list.html")