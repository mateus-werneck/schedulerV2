from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class ScheduleHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'cronograma'

    def get_steps(self) -> list:
        return [self.list_options]

    def get_parent_handler_name(self) -> str:
        return 'agenda_handler'

    def list_options(self):
        FactoryQueue\
            .create('Schedule.Listing.Schedules.list_schedules_options')\
            .init()
