from App.Queues.Jobs.Daily.update import Update
from App.Lib.Bot.job_queue import BotJobQueue


class RegisterJobs(Update):

    def handle(self):
        [self.register(job) for job in self.get_jobs()]
        return super().handle()

    def register(self, job: dict):
        BotJobQueue.instance().register_daily(**job)
