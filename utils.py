# -- GISMentors subroutines --------------------------------------
import datetime
import locale
import warnings

def get_month_year(force_locale='cs_CZ.UTF-8'):
    try:
        locale.setlocale(locale.LC_ALL, force_locale)
    except locale.Error as e:
        warnings.warn(f"{e}")
        locale.setlocale(locale.LC_ALL)
    from calendar import month_name
    
    date = datetime.datetime.now()
    s = month_name[date.month]
    return s, date.year

def get_year():
    date = datetime.datetime.now()
    return date.year
