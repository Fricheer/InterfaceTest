from django import template # 导入template

register = template.Library() # 实例化Library

@register.filter(name='cut') # filter 修饰
def cut(value, arg):
    return value.replace(arg, '')