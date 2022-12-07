from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Log.logger import Logger
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Bot.job_queue import BotJobQueue
from App.Data.Helpers.task_helper import treat_task_to_message


def append_today_tasks():
    Logger.instance().info('Registering new tasks for today.', context=self)
    daily_schedule = MarinaAPI.instance().list_today_tasks()
    daily_jobs = get_schedule_to_jobs(daily_schedule)
    map(BotJobQueue.instance().register_once, daily_jobs)


def get_schedule_to_jobs(daily_schedules: list):
    tasks = get_tasks_from_schedules(daily_schedules)
    return list(map(treat_task_to_job, tasks))


def treat_task_to_job(task: dict):
    return {
        'callback': alert_task,
        'name': task.get('name'),
        'context': treat_task_to_message(task)
    }


def alert_task(context: CallbackContext):
    message = context.job.context
    Logger.instance().info('Sending one-time automatic message.')
    context.bot.send_message(chat_id=460786067, text=message)


def delete_expired_schedules(context: CallbackContext):
    Logger.instance().info('Removing expired schedules from the database.')
    MarinaAPI.instance().delete_expired_schedules()
