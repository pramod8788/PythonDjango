from django import template

register = template.Library()

@register.filter
def to_model_name(value):
    return value.__class__.__name__