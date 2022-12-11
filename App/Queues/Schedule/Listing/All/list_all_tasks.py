from App.Queues.Standard.abstract_handler import AbstractHandler


class ListAllTasks(AbstractHandler):
    _tasks = None

    def __init__(self):
        if self.__class__ is ListAllTasks:
            ListAllTasks._tasks = None

    def get_steps(self) -> list:
        return [
            'find_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.All'

    @staticmethod
    def set_tasks(tasks: list):
        ListAllTasks._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListAllTasks._tasks
