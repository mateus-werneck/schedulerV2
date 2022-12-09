from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class SchedulesHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'cronograma'

    def get_steps(self) -> list:
        return [
            self.list_options
        ]

    def list_options(self):
        FactoryQueue.instance()\
            .create('Schedule.Listing.Schedules.list_schedules_options')\
            .init()
