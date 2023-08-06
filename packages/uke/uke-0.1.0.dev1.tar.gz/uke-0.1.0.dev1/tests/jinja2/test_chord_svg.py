#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Template

# from uke.tmpl import chord_svg


# 打开模板
with open('./uke/tmpl/base.jinja2', 'r', encoding='utf-8') as f:
    templ_file = f.read()
templ = Template(templ_file)
# 设置参数
element = {
    "width": 84,  # "100%"
    "height": 124,  # "100%"
    "style": "font-family: sans-serif; font-size: 11px;",
    "content": "content",
}
ret = templ.render(element)
print(ret)
