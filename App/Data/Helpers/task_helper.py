from App.Data.Helpers.message_helper import alarm_clock
from App.Lib.Treat.date_treat import (treat_datetime_to_pt_date,
                                      treat_iso_string_to_datetime,
                                      add_time_to_date,
                                      treat_datetime_to_iso_string,
                                      is_valid_pt_date,
                                      treat_date_string_to_datetime)
from App.Lib.Treat.time_treat import (treat_datetime_to_string_hour,
                                      treat_string_hour_to_time)


def treat_string_to_task(new_task: str):
    task_props = new_task.split(',')
    if len(task_props) < 4:
        task_props.insert(1, task_props[0])
    
    return {
        'name': task_props[0],
        'description': task_props[1],
        'deadline': get_deadline_from_message(task_props[2], task_props[3])
    }


def get_deadline_from_message(date: str, hour: str):
    date_to_treat = get_deadline_date(date)
    hour_deadline = treat_string_hour_to_time(hour)
    datetime_deadline = add_time_to_date(date_to_treat, hour_deadline)
    
    return treat_datetime_to_iso_string(datetime_deadline)


def get_deadline_date(day: str):
    if is_valid_pt_date(day):
        return treat_date_string_to_datetime(day)
    # return WeekDay.get_date_from_week_day(day)
