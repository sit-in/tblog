#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()

@register.filter
def add_one(num):
    try:
        num = int(num)
    except:
        num = 0
    return  num+1

@register.filter
def sub_one(num):
    try:
        num = int(num)
    except:
        num = 0
    return  num-1
