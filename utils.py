# -- GISMentors subroutines --------------------------------------
import datetime
    
def get_month_year(locale='cs_CZ.UTF-8'):
    from calendar import TimeEncoding, month_name
    
    date = datetime.datetime.now()
    with TimeEncoding(locale) as encoding:
        s = month_name[date.month]
        if encoding is not None:
            s = s.decode(encoding)
        return s, date.year

def get_year():
    date = datetime.datetime.now()
    return date.year
