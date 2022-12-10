from App.Queues.Standard.abstract_handler import AbstractHandler


class ListMonthly(AbstractHandler):
    _tasks = None

    def __init__(self):
        if self.__class__ is ListMonthly:
            ListMonthly._tasks = None

    def get_steps(self) -> list:
        return [
            'find_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.Monthly'

    @staticmethod
    def set_tasks(tasks: list):
        ListMonthly._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListMonthly._tasks
