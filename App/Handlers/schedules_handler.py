from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class SchedulesHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'cronograma'

    def get_steps(self) -> list:
        return [
            self.list_options,
            self.answer_options,
            self.start_task_mode
        ]

    def list_options(self):
        FactoryQueue\
            .create('Schedule.Listing.Schedules.list_schedules_options')\
            .init()

    def answer_options(self):
        self.delete_message()

        if self.is_daily_mode():
            self.daily_mode()
        elif self.is_weekly_mode():
            self.weekly_mode()
        elif self.is_monthly_mode():
            self.monthly_mode()

    def is_daily_mode(self):
        return self.is_mode('schedule_list_daily')

    def daily_mode(self):
        FactoryQueue.create('Schedule.Listing.Daily.list_daily')\
            .init()

    def is_weekly_mode(self):
        return self.is_mode('schedule_list_weekly')

    def weekly_mode(self):
        FactoryQueue.create('Schedule.Listing.Weekly.list_weekly')\
            .init()

    def is_monthly_mode(self):
        return self.is_mode('schedule_list_monthly')

    def monthly_mode(self):
        FactoryQueue.create('Schedule.Listing.Monthly.list_monthly')\
            .init()

    def start_task_mode(self):
        queue = 'Task.Listing.TaskOptions.list_task_options'
        FactoryQueue.create(queue).init()
