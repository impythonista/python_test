from django import template
from ..models import Client


register = template.Library()

@register.filter(name='count_filter')
def count_filter(val, page):
  value = ((page - 1) * 10) + val if val and page else val
  return value
