from django import template

from petstagram.main.models import Profile

register = template.Library()
""" Променливата register ни дава декоратори от Джанго библиотеката"""

""" декорато който връща някаква стойност "стринг" """


@register.simple_tag()
def has_profile():
    """ връщаме дали броя на профилите е повече от 0"""
    return Profile.objects.count() > 0



