from App.Queues.Standard.abstract_handler import AbstractHandler


class ListSchedulesOptions(AbstractHandler):
    
    def get_steps(self) -> list:
        return [
            'list_categories'
        ]
    
    def get_namespace(self) -> str:
        return 'Schedule.Listing.Schedules'
