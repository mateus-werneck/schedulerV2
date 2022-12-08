from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_string,
                                      treat_node_string,
                                      treat_string_to_datetime)
from App.Queues.Schedule.Search.search import Search


class CreateSchedule(Search):
    
    def handle(self) -> bool:
        if not self.has_active_schedule():
            return super().handle()
        
        schedule = self.create_schedule()
        self.set_schedule(schedule)
        return super().handle()
    
    
    def create_schedule(self):
        grade = self.get_grade()
        deadline = self.get_deadline()

        queue = FactoryQueue.create('Schedule.Create.create')
        queue.set_grade(grade)
        queue.set_deadline(deadline)
        queue.init()

        return queue.get_schedule()

    