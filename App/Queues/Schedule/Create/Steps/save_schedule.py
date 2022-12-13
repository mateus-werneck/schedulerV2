
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import treat_string_to_datetime
from App.Lib.Treat.week_day_treat import WeekDay
from App.Queues.Schedule.Create.create import Create


class SaveSchedule(Create):

    def handle(self) -> bool:
        self.save()
        return super().handle()

    def save(self):
        schedule = self.create_schedule()
        self.set_schedule(schedule)

    def create_schedule(self):
        data = self.get_schedule_by_deadline()
        return MarinaAPI.instance().create_schedule(data)

    def get_schedule_by_deadline(self):
        schedule_date = self.get_deadline()

        schedule = {
            'scheduleDate': schedule_date,
            'scheduleDay': self.get_schedule_day(schedule_date)
        }
        self.append_grade(schedule)
        return schedule

    def get_schedule_day(self, deadline: str):
        deadline_datetime = treat_string_to_datetime(deadline)
        return WeekDay().get_week_day_from_date(deadline_datetime)
    
    def append_grade(self, schedule:dict):
        if not self.get_grade():
            return
        schedule['gradeId'] = self.get_grade()
        
