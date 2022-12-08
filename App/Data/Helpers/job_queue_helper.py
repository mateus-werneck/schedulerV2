from telegram.ext.callbackcontext import CallbackContext

from App.Data.Helpers.task_helper import (get_tasks_from_schedules,
                                          treat_task_to_alert_message)
from App.Lib.Bot.job_queue import BotJobQueue
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Log.logger import Logger
from App.Lib.Treat.date_treat import get_minutes_before, treat_node_string


def append_today_tasks(context: CallbackContext):
    Logger.instance().info('Registering new tasks for today.')
    daily_schedules = MarinaAPI.instance().list_today_tasks()
    daily_jobs = get_schedule_to_jobs(daily_schedules)
    [BotJobQueue.instance().register_once(**job) for job in daily_jobs]


def get_schedule_to_jobs(daily_schedules: list):
    tasks = get_tasks_from_schedules(daily_schedules)
    return list(map(treat_task_to_job, tasks))


def treat_task_to_job(task: dict):
    deadline = treat_node_string(task.get('deadLine'))
    return {
        'callback': alert_task,
        'when': get_minutes_before(deadline, 185),
        'context': treat_task_to_alert_message(task),
        'name': task.get('name'),
    }


def alert_task(context: CallbackContext):
    message = context.job.context
    Logger.instance().info('Sending one-time automatic message.')
    context.bot.send_message(chat_id=460786067, text=message)


def delete_expired_schedules(context: CallbackContext):
    Logger.instance().info('Removing expired schedules from the database.')
    MarinaAPI.instance().delete_expired_schedules()
