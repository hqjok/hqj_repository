#!/usr/bin/python
# -*-  coding:utf-8  -*-
# @Time   : 2019/3/3  14:46
# @Author : 黄猿
# @File   : my_way.py

from django.shortcuts import render
from reception import models


# 新建一个工具类  用来将base.html动态加载的数据传递到继承页面
class RenderWrite(object):

    def render_template(request, template_name, context=None, content_type=None, status=None, using=None):
        c_list = []
        cate = models.Alltype.objects.all().distinct()
        for c in cate:
            data = {
                'type': c.type,
                'id': c.atid,
                "ArticleType": []
            }
            c_list.append(data)
            pro = models.ArticleType.objects.filter(from_type_id=c.atid)
            for p in pro:
                data["ArticleType"].append(p)
                # print(c.type, p.type_name)
        # print(c_list)
        if isinstance(context, dict):
            context["c_list"] = c_list
        else:
            context = {
                'c_list': c_list,
            }
        return render(
            request=request,
            template_name=template_name,
            context=context,
            content_type=content_type,
            status=status,
            using=using
        )