from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Schedule.Listing.list_schedule_options import \
    ListScheduleOptions


class ScheduleHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'agenda'

    def get_steps(self) -> list:
        return [self.list_options]

    def list_options(self):
        ListScheduleOptions().init()
