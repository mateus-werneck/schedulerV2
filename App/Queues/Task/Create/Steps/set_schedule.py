
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_string,
                                      treat_node_string,
                                      treat_string_to_datetime)
from App.Queues.Standard.factory_queue import FactoryQueue
from App.Queues.Task.Create.create import Create


class SetSchedule(Create):
  
    def handle(self) -> bool:
        self.set_schedule_id()
        return super().handle()

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
