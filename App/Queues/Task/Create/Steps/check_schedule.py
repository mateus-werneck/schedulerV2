
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Create.create import Create
from App.Lib.Treat.date_treat import treat_iso_string_to_datetime, treat_datetime_to_iso_string


class CheckSchedule(Create):

    def handle(self) -> bool:
        grade = MarinaAPI.instance().find_grade(self.get_grade())
        return super().handle()

    def has_active_schedule(self, grade: dict, task: dict):
        if not grade.get('schedules'):
            return False
        schedules = self.get_schedule_dates(grade)
        return task.get('deadLine') in schedules

    def get_schedule_dates(self, grade: dict):
        return [treat_datetime_to_iso_string(
            treat_iso_string_to_datetime(schedule.get('scheduleDate')))
            for schedule in grade.get('schedules')
        ]

    def create_schedule(self):
        pass