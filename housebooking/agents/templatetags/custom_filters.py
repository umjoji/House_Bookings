from django import template

register = template.Library()

@register.filter
def is_agent(user):
    return user.groups.filter(name='agents').exists()

@register.filter
def is_landlord(user):
    return user.groups.filter(name='landlords').exists()

@register.filter
def is_tenant(user):
    return user.groups.filter(name='tenants').exists()