from datetime import datetime, time, timedelta
from time import strptime

from pytz import timezone

node_format = '%Y-%m-%dT%H:%M:%S.%fZ'
iso_format = '%Y-%m-%d %H:%M:%S'
pt_br_format = '%d/%m/%Y'


def is_valid_pt_date(date: str):
    try:
        return strptime(date, pt_br_format) is not None
    except Exception:
        return False


def treat_node_string(node_date: str):
    time_obj = strptime(node_date, node_format)

    return datetime(
        year=time_obj.tm_year,
        month=time_obj.tm_mon,
        day=time_obj.tm_mday,
        hour=time_obj.tm_hour,
        minute=time_obj.tm_min,
        second=0,
        microsecond=0,
        tzinfo=timezone('America/Sao_Paulo')
    )


def treat_string_to_datetime(date: str):
    local_zone = timezone('America/Sao_Paulo')
    return datetime.strptime(date, iso_format)\
        .replace(tzinfo=local_zone)
        
def treat_pt_string_to_datetime(date: str):
    local_zone = timezone('America/Sao_Paulo')
    return datetime.strptime(date, pt_br_format)\
        .replace(tzinfo=local_zone)


def treat_datetime_to_string(date: datetime):
    return datetime.strftime(date, iso_format)


def treat_datetime_to_pt_date(date: datetime):
    return datetime.strftime(date, pt_br_format)


def get_minutes_before(date: datetime, minutes: float):
    return date - timedelta(minutes=minutes)


def get_minutes_after(date: datetime, minutes: float):
    return date + timedelta(minutes=minutes)


def add_time_to_date(date: datetime, time_obj: time):
    return date + timedelta(hours=time_obj.hour, minutes=time_obj.minute)
