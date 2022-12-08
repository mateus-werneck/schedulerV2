from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_string,
                                      treat_node_string,
                                      treat_string_to_datetime)
from App.Queues.Schedule.Search.search import Search


class CheckScheduleExists(Search):
    schedule_dates = []
    
    def handle(self) -> bool:
        if not self.has_active_schedule():
            return super().handle()
        
        schedule = self.find_schedule()
        self.set_schedule(schedule)
        return super().handle(True)
    
    def has_active_schedule(self):        
        if not self.get_grade().get('schedules'):
            return False

        self.schedule_dates = self.get_schedule_dates()
        return self.get_deadline_to_compare() in self.schedule_dates

    def get_schedule_dates(self):
        schedule_dates = [schedule.get('scheduleDate')
                          for schedule in self.get_grade().get('schedules')]
        return [treat_node_string(date) for date in schedule_dates]

    def get_deadline_to_compare(self):
        deadline = treat_string_to_datetime(self.get_deadline())
        return deadline.replace(hour=0, minute=0)

    def find_schedule(self):
        schedule_date = self.get_deadline_to_compare()
        schedule_index = self.schedule_dates.index(schedule_date)
        return self.get_grade().get('schedules')[schedule_index]

    