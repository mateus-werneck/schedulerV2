from App.Queues.Standard.abstract_handler import AbstractHandler


class ListDaily(AbstractHandler):
    _tasks = None

    def __init__(self):
        if self.__class__ is ListDaily:
            ListDaily._tasks = None

    def get_steps(self) -> list:
        return [
            'find_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.Daily'

    @staticmethod
    def set_tasks(tasks: list):
        ListDaily._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListDaily._tasks
