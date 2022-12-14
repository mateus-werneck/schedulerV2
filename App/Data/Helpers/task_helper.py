from App.Data.Helpers.message_helper import alarm_clock
from App.Lib.Treat.date_treat import (add_time_to_date, get_minutes_before,
                                      is_valid_pt_date,
                                      treat_datetime_to_pt_date,
                                      treat_datetime_to_string,
                                      treat_node_string,
                                      treat_pt_string_to_datetime)
from App.Lib.Treat.time_treat import (treat_datetime_to_string_hour,
                                      treat_string_hour_to_time)
from App.Lib.Treat.week_day_treat import WeekDay


def treat_string_to_task(new_task: str):
    task_props = [task.split(':', 1).pop().strip()
                  for task in new_task.split('\n')]
    
    if len(task_props) != 4:
        return {}
    
    return {
        'name': task_props.pop(0),
        'description': task_props.pop(0),
        'deadLine': get_deadline_from_message(
            task_props.pop(0), task_props.pop(0))
    }

def get_deadline_from_message(date: str, hour: str):
    date_to_treat = get_deadline_date(date)
    hour_deadline = treat_string_hour_to_time(hour)
    datetime_deadline = add_time_to_date(date_to_treat, hour_deadline)
    return treat_datetime_to_string(datetime_deadline)


def get_deadline_date(day: str):
    if is_valid_pt_date(day):
        return treat_pt_string_to_datetime(day)
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
        if not task.get('grade'):
            continue
        task['grade'] = schedule.get('grade')['name']


def get_base_task_message():
    return (
        '<b>Tarefa:</b> {name}\
        \n<b>Descrição:</b> {description}\
        \n<b>Data Limite:</b> {due_date}\
        \n<b>Horário de entrega:</b> {delivery_date}\
    ')


def treat_task_to_alert_message(task: dict):
    deadline = get_minutes_before(treat_node_string(task.get('deadLine')), 180)

    task_message = {
        'name': task.get('name'),
        'description': task.get('description'),
        'due_date': treat_datetime_to_pt_date(deadline),
        'delivery_date': treat_datetime_to_string_hour(deadline),
    }
    
    message = f'{alarm_clock()} Alerta de Tarefa.\n' 
    
    if task.get('grade'):
        task_message['grade'] = task.get('grade')
        message += '<b>Turma:</b> {grade}\n' 

    message += get_base_task_message()
    return message.format(**task_message)


def treat_task_to_message(task: dict):
    deadline = get_minutes_before(treat_node_string(task.get('deadLine')), 180)

    task_message = {
        'name': task.get('name'),
        'description': task.get('description'),
        'due_date': treat_datetime_to_pt_date(deadline),
        'delivery_date': treat_datetime_to_string_hour(deadline),
    }

    return get_base_task_message().format(**task_message)
