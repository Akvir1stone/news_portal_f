from django import template


register = template.Library()


@register.filter()
def text(value):
    v = str(value)
    for i in range(len(v)-3):
        t = v[i:i+3]
        if t == 'ajh':
            tv = v[0:i]
            tv = tv + '***'
            tv = tv + v[i+3:]
            v = tv
    return v
