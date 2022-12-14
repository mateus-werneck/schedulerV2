from App.Data.Helpers.job_queue_helper import (append_today_tasks,
                                               delete_expired_schedules)
from App.Lib.Treat.time_treat import treat_string_hour_to_time
from App.Queues.Jobs.Daily.update import Update


class SetJobs(Update):

    def handle(self):
        jobs = list()
        self.append_delete_expired_schedule(jobs)
        self.append_add_tasks_job(jobs)
        self.set_jobs(jobs)
        return super().handle()

    def append_delete_expired_schedule(self, jobs: list):
        jobs.append({
            'callback': delete_expired_schedules,
            'time': treat_string_hour_to_time('02:00'),
            'name': 'Delete Expired Schedules'
        })

    def append_add_tasks_job(self, jobs: list):
        jobs.append({
            'callback': append_today_tasks,
            'time': treat_string_hour_to_time('09:50'),
            'name': 'Add Today Tasks'
        })
