from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_pt_date,
                                      treat_node_string)
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour
from App.Queues.Schedule.Listing.Monthly.list_monthly import ListMonthly


class FindTasks(ListMonthly):

    def handle(self):
        monthly_tasks = self.find_monthly()
        self.set_tasks(monthly_tasks)
        return super().handle()

    def find_monthly(self):
        monthly = MarinaAPI.instance().list_monthly_tasks()
        tasks = get_tasks_from_schedules(monthly)
        return [self.treat_task(task) for task in tasks]

    def treat_task(self, task: dict):
        deadline = treat_node_string(task.get('deadLine'))
        deadline_date = treat_datetime_to_pt_date(deadline)
        deadline_hour = treat_datetime_to_string_hour(deadline)
        
        return {
            'id': task.get('id'),
            'name': f'{task.get("name")} - {deadline_date} - {deadline_hour}'
        }
