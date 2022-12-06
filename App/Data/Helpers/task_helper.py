from App.Lib.Treat.date_treat import (add_time_to_date,
                                      treat_datetime_to_string,
                                      is_valid_pt_date,
                                      treat_string_to_datetime)
from App.Lib.Treat.time_treat import treat_string_hour_to_time
from App.Lib.Treat.week_day_treat import WeekDay

def treat_string_to_task(new_task: str):
    task_props = new_task.split(',')
    append_task_description(task_props)

    return {
        'name': task_props[0],
        'description': task_props[1],
        'deadLine': get_deadline_from_message(task_props[2], task_props[3])
    }

def append_task_description(task_props: list):
    if len(task_props) < 4:
        task_props.insert(1, task_props[0])

def get_deadline_from_message(date: str, hour: str):
    date_to_treat = get_deadline_date(date)
    hour_deadline = treat_string_hour_to_time(hour)
    datetime_deadline = add_time_to_date(date_to_treat, hour_deadline)
    return treat_datetime_to_string(datetime_deadline)


def get_deadline_date(day: str):
    if is_valid_pt_date(day):
        return treat_string_to_datetime(day)
    return WeekDay().get_date_from_week_day(day)
