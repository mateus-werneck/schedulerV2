
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_string_to_datetime,
                                      treat_datetime_to_string,
                                      treat_node_string)
from App.Queues.Schedule.Create.create import Create as CreateSchedule
from App.Queues.Task.Create.create import Create


class CheckSchedule(Create):
    schedule_dates = []
    current_grade = {}

    def handle(self) -> bool:
        self.set_current_grade()
        self.set_task_schedule_id()
        return super().handle()

    def set_current_grade(self):
        self.current_grade = MarinaAPI.instance().find_grade(self.get_grade())

    def set_task_schedule_id(self):
        task = self.get_task()
        task['scheduleId'] = self.get_schedule_id()

    def get_schedule_id(self):
        schedule = self.find_or_create_schedule()
        return schedule.get('id')

    def find_or_create_schedule(self):
        if self.has_active_schedule():
            return self.find_schedule()
        return self.create_schedule()

    def has_active_schedule(self):
        if not self.current_grade.get('schedules'):
            return False

        self.schedule_dates = self.get_schedule_dates()
        return self.get_deadline() in self.schedule_dates

    def get_schedule_dates(self):
        schedule_dates = [schedule.get('scheduleDate')
                          for schedule in self.current_grade.get('schedules')]
        return [treat_node_string(date) for date in schedule_dates]

    def get_deadline(self):
        task = self.get_task()
        deadline = treat_string_to_datetime(task.get('deadLine'))
        return deadline.replace(hour=0, minute=0)

    def find_schedule(self):
        schedule_date = self.get_deadline()
        schedule_index = self.schedule_dates.index(schedule_date)
        return self.current_grade.get('schedules')[schedule_index]

    def create_schedule(self):
        grade = self.get_grade()
        deadline = treat_datetime_to_string(self.get_deadline())

        queue = CreateSchedule()
        queue.set_grade(grade)
        queue.set_deadline(deadline)
        queue.init()

        return queue.get_schedule()
