from django import template
from datetime import datetime, timezone, timedelta

register = template.Library()

@register.filter
def zip_lists(a, b):
    return zip(a, b)


@register.filter
def time_since_expired(expiration_date):
    now = datetime.now(timezone.utc)
    if isinstance(expiration_date, datetime):
        expiration_date = expiration_date.date()
    expiration_date = datetime.combine(expiration_date, datetime.min.time(), tzinfo=timezone.utc)
    if expiration_date < now:
        time_difference = now - expiration_date
        days = time_difference.days
        if days == 0:
            seconds = time_difference.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            if hours == 0 and minutes == 0:
                return "Just expired"
            elif hours == 0:
                return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            else:
                return f"{hours} hour{'s' if hours > 1 else ''} and {minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return "Not yet expired"
# def time_since_expired(expiration_date):
#     now = datetime.now(timezone.utc)
#     if expiration_date < now:
#         time_difference = now - expiration_date
#         days = time_difference.days
#         if days == 0:
#             seconds = time_difference.seconds
#             hours = seconds // 3600
#             minutes = (seconds % 3600) // 60
#             if hours == 0 and minutes == 0:
#                 return "Just expired"
#             elif hours == 0:
#                 return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
#             else:
#                 return f"{hours} hour{'s' if hours > 1 else ''} and {minutes} minute{'s' if minutes > 1 else ''} ago"
#         else:
#             return f"{days} day{'s' if days > 1 else ''} ago"
#     else:
#         return "Not yet expired"