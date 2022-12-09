from App.Queues.Schedule.Listing.Daily.list_daily import ListDaily
from App.Lib.Client.marina_api import MarinaAPI
from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour


class FindTasks(ListDaily):

    def handle(self):
        daily_tasks = self.find_daily()
        self.set_tasks(daily_tasks)
        return super().handle()

    def find_daily(self):
        daily = MarinaAPI.instance().list_today_tasks()
        tasks = get_tasks_from_schedules(daily)
        return [treat_task(task) for task in tasks]

    def treat_task(task: dict):
        deadline = treat_datetime_to_string_hour(task.get('deadLine'))
        return {
            'id': task.get('id'),
            'name': f'{task.get("name")} - {deadline}'
        }
