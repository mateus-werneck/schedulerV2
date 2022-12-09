
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_string,
                                      treat_node_string,
                                      treat_string_to_datetime)
from App.Queues.Standard.factory_queue import FactoryQueue
from App.Queues.Task.Edit.edit import Edit


class CheckSchedule(Edit):
    schedule_dates = []
    grade = None

    def handle(self) -> bool:
        if not self.should_check_schedule():
            return super().handle()
        
        self.set_schedule_id()
        return super().handle()

    def should_check_schedule(self):
        task_data = self.get_task()
        task = MarinaAPI.instance().find_task(self.get_task_id())
        self.grade = task.get('schedule').get('gradeId')
        
        current_deadline = treat_string_to_datetime(task_data.get('deadLine'))
        old_deadline = treat_node_string(task.get('deadLine'))
        return current_deadline != old_deadline
    
    def set_schedule_id(self):
        task = self.get_task()
        schedule = self.find_schedule()
        task['scheduleId'] = schedule.get('id')
    
    def find_schedule(self):
        grade = self.get_grade()
        deadline = self.get_task().get('deadLine')

        queue = FactoryQueue.create('Schedule.Search.search')
        queue.set_grade(grade)
        queue.set_deadline(deadline)
        queue.init()

        return queue.get_schedule()
