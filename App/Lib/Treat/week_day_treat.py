from datetime import datetime, timedelta

from App.Lib.Errors.WeekDay.week_day_limit_exception import \
    WeekDayExceededException
from App.Lib.Errors.WeekDay.week_day_utc_exception import \
    WeekDayUtcNotFoundException
from App.Lib.Treat.date_treat import get_minutes_after, treat_date_to_string


class WeekDay:
    
    def __init__(self):
        self.recursion_limit = 6
        self.current_recursion = 0
    
    def get_week_days(self):
        return {
            'Monday': ['segunda'],
            'Tuesday': ['terca', 'terça'],
            'Wednesday': ['quarta'],
            'Thursday': ['quinta'],
            'Friday': ['sexta'],
            'Saturday': ['sábado', 'sabado'],
            'Sunday': ['domingo']
        }

    def get_date_from_week_day(self, day: str):
        day = self.treat_week_day(day)
        utc_day = self.__convert_utc_day(day)
        return self.__get_date_from_utc_day(utc_day)
    
    def get_week_day_from_date(self, date: datetime):
        return self.__get_utc_day_from_datetime(date)
    
    def treat_week_day(self, day: str):
        day = day.lower().replace(' ', '', 1)
        day = day.split('-')[0]
        day = day.split(' ')[0]
        return day

    def __convert_utc_day(self, day: str):
        week_days = self.get_week_days()
        for utc_day, day_list in week_days.items():
            if day in day_list:
                return utc_day
        raise WeekDayUtcNotFoundException()

    def __get_date_from_utc_day(self, utc_day: str, today: datetime = None):
        if today is None:
            today = datetime.today()
        
        current_utc_day = self.__get_utc_day_from_datetime(today)

        if current_utc_day == utc_day.lower():
            self.current_recursion = 0
            return today.replace(hour=0, minute=0, second=0, microsecond=0)

        self.__check_recursion_limit()
        return self.__get_date_from_utc_day(utc_day, today + timedelta(days=1))

    def __get_utc_day_from_datetime(self, date: datetime):
        return date.strftime('%A').lower()
    
    def __check_recursion_limit(self):
        self.current_recursion += self.current_recursion
        if self.current_recursion > self.recursion_limit:
            raise WeekDayExceededException()
        
    def get_end_of_week_date(self):
        today = datetime.today()
        
        if self.is_last_day_week(today):
            return treat_date_to_string(today)
        
        current_day = self.get_week_day_from_date(today)
        days_after = self.get_days_before_week_last_day(current_day)
        return self.get_date_after_some_days(today, days_after)
        
    def is_last_day_week(self, date: datetime):    
        current_day = self.get_week_day_from_date(date)
        return current_day == 'sunday'
    
    def get_days_before_week_last_day(self, day: str):
        week_days = list(self.get_week_days().keys())
        day_index = week_days.index(day.capitalize())
        last_day_index = week_days.index('Sunday')
        return last_day_index - day_index
            
    def get_date_after_some_days(self, date: datetime, days: int):
        days_minutes = days * 1440
        next_date = get_minutes_after(date, days_minutes)
        return treat_date_to_string(next_date)
