import os

from App.Lib.Standard.abstract_connection import Connection
from App.Lib.Treat.date_treat import today
from App.Lib.Treat.week_day_treat import WeekDay


class MarinaAPI(Connection):

    def get_base_url(self):
        return os.environ['MARINA_API']

    def list_grades(self):
        grades = self.get('grades')
        if not grades:
            return []
        return grades

    def find_grade(self, id: str):
        return self.get(f'grades/id/{id}')

    def create_grade(self, name: str):
        return self.post('grades', {'name': name})

    def update_grade(self, id: str, name: str):
        return self.patch(f'grades/{id}', {'name': name})

    def delete_grade(self, id: str):
        return self.delete(f'grades/{id}')

    def list_grade_tasks(self, grade_id: str):
        grade = self.get(f'grades/id/{grade_id}')
        if not grade or not grade['schedules']:
            return []
        tasks = list()
        for schedule in grade['schedules']:
            tasks += schedule['tasks']
        return tasks

    def find_task(self, id: str):
        return self.get(f'tasks/{id}')

    def create_task(self, data: dict):
        return self.post('tasks', data)

    def edit_task(self, id: str, data: dict):
        return self.patch(f'tasks/{id}', data)

    def delete_task(self, id: str):
        return self.delete(f'tasks/{id}')

    def list_today_tasks(self):
        return self.get('schedules/today')

    def list_weekly_tasks(self):
        week_day = WeekDay()
        query_params = {
            'initialDate': today(),
            'finalDate': week_day.get_end_of_week_date()
        }
        
        return self.get('schedules', query_params)
    
    def list_monthly_tasks(self):
        week_day = WeekDay()
        query_params = {
            'initialDate': today(),
            'finalDate': week_day.get_end_of_week_date()
        }
        
        return self.get('schedules', query_params)

    def create_schedule(self, data: dict):
        return self.post('schedules', data)

    def delete_expired_schedules(self):
        self.delete('schedules/today')
