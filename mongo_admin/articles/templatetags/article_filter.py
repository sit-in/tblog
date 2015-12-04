#!/usr/bin/env python
# encoding: utf-8

from django import template
register = template.Library()


@register.filter
def obj2str(o_id):
    return str(o_id)
