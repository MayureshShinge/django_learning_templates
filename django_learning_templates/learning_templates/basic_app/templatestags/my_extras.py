from django import template

register = template.Library()

#creating a custom template filter
@register.filter(name='cut')
def cut(value,arg):
    # This cuts out or removes all the values of "arg" from the string.

    return value.replace(arg,'')

#We will pass a string 'cut' and in second one we will call the function
# register.filter('cut',cut)