from App.Queues.Jobs.Daily.update import Update
from App.Data.Helpers.job_queue_helper \
    import append_today_tasks, delete_expired_schedules


class SetJobs(Update):

    def handle(self):
        jobs = list()
        self.append_delete_expired_schedule()
        self.append_add_tasks_job(jobs)
        self.set_jobs(jobs)
        return super().handle()

    def append_delete_expired_schedule(self, jobs: list):
        jobs.append({
            'name': 'Delete Expired Schedules',
            'when': '05:00',
            'callback': delete_expired_schedules
        })

    def append_add_tasks_job(self, jobs: list):
        jobs.append({
            'name': 'Add Today Tasks',
            'when': '05:01',
            'callback': append_today_tasks
        })
