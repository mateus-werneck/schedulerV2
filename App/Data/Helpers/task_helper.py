from App.Lib.Treat.date_treat import (add_time_to_date, is_valid_pt_date,
                                      treat_datetime_to_string,
                                      treat_string_to_datetime)
from App.Lib.Treat.time_treat import treat_string_hour_to_time
from App.Lib.Treat.week_day_treat import WeekDay
from App.Data.Helpers.message_helper import alarm_clock
from App.Lib.Treat.date_treat \
    import treat_node_string, treat_datetime_to_pt_date, get_minutes_before
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour


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


def get_tasks_from_schedules(schedules: list):
    [treat_schedule_tasks(schedule) for schedule in schedules]
    tasks = list()
    for schedule in schedules:
        tasks += schedule.get('tasks')
    return tasks


def treat_schedule_tasks(schedule: dict):
    tasks = schedule.get('tasks')
    for task in tasks:
        task['grade'] = schedule.get('grade')['name']


def treat_task_to_message(task: dict):
    deadline = get_minutes_before(treat_node_string(task.get('deadLine')), 180)
    
    task_message = {
        'grade': task.get('grade'),
        'name': task.get('name'),
        'description': task.get('description'),
        'due_date': treat_datetime_to_pt_date(deadline),
        'delivery_date': treat_datetime_to_string_hour(deadline),
    }
    
    return f'{alarm_clock()} Alerta de Tarefa.' \
        + get_base_task_message().format(**task_message)


def get_base_task_message():
    return ('\
        \n<b>Turma:</b> {grade}\
        \n<b>Tarefa:</b> {name}\
        \n<b>Descrição:</b> {description}\
        \n<b>Data Limite:</b> {due_date}\
        \n<b>Horário de entrega:</b> {hour}\
    ')
