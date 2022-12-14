from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_pt_date,
                                      treat_node_string)
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour
from App.Queues.Schedule.Listing.All.list_all_tasks import ListAllTasks


class FindTasks(ListAllTasks):

    def handle(self):
        tasks = self.find_tasks()
        self.set_tasks(tasks)
        return super().handle()

    def find_tasks(self):
        tasks = MarinaAPI.instance().list_tasks_no_grade()
        tasks = get_tasks_from_schedules(tasks)
        return [self.treat_task(task) for task in tasks]

    def treat_task(self, task: dict):
        deadline = treat_node_string(task.get('deadLine'))
        deadline_date = treat_datetime_to_pt_date(deadline)
        deadline_hour = treat_datetime_to_string_hour(deadline)
        
        return {
            'id': task.get('id'),
            'name': f'{task.get("name")} - {deadline_date} - {deadline_hour}'
        }
