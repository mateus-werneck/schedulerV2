from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import treat_node_string
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour
from App.Queues.Schedule.Listing.Weekly.list_weekly import ListWeekly


class FindTasks(ListWeekly):

    def handle(self):
        daily_tasks = self.find_weekly()
        self.set_tasks(daily_tasks)
        return super().handle()

    def find_weekly(self):
        daily = MarinaAPI.instance().list_weekly_tasks()
        tasks = get_tasks_from_schedules(daily)
        return [self.treat_task(task) for task in tasks]

    def treat_task(self, task: dict):
        deadline = treat_node_string(task.get('deadLine'))
        deadline = treat_datetime_to_string_hour(deadline)
        
        return {
            'id': task.get('id'),
            'name': f'{task.get("name")} - {deadline}'
        }
