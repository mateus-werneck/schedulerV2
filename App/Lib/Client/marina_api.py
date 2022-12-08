import os

from App.Lib.Standard.abstract_connection import Connection


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
        return [task for task in grade['schedules'][0]['tasks']]

    def create_task(self, data: dict):
        return self.post('tasks', data)

    def delete_task(self, id: str):
        return self.delete(f'tasks/{id}')
    
    def list_today_tasks(self):
        return self.get('schedules/today')

    def create_schedule(self, data: dict):
        return self.post('schedules', data)

    def delete_expired_schedules(self):
        self.delete('schedules/today')
