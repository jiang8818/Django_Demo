# *_* coding: utf-8 *_*
# time:2021-04-0813:54
# tools:PyCharm
# file_name：form_tags.py.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django import template
register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__
@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)