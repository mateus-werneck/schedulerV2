
from App.Data.Helpers.job_queue_helper import append_today_tasks
from App.Lib.Treat.date_treat import today, treat_date_to_string
from App.Queues.Task.Create.create import Create


class AlertTask(Create):

    def handle(self) -> bool:
        if self.is_deadline_today():
            append_today_tasks()
        return super().handle()

    def is_deadline_today(self):
        task = self.get_task()
        deadline = treat_string_to_datetime(task['deadLine'])
        return today() == treat_date_to_string(deadline)
