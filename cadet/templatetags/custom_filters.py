from django import template

register = template.Library()

@register.filter
def get_mark(param):
    print(param)
    return __self__.filter(lesson_id=param.lid, cadet_id=param.cid)