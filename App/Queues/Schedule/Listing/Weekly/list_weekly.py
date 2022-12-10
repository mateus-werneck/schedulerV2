from App.Queues.Standard.abstract_handler import AbstractHandler


class ListWeekly(AbstractHandler):
    _tasks = None

    def __init__(self):
        if self.__class__ is ListWeekly:
            ListWeekly._tasks = None

    def get_steps(self) -> list:
        return [
            'find_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.Weekly'

    @staticmethod
    def set_tasks(tasks: list):
        ListWeekly._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListWeekly._tasks
