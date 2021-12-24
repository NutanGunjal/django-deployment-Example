from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This is cut out all values of "arg" fron the string!
    """
    return value.replace(arg, '')


#register.filter('cut', cut)
