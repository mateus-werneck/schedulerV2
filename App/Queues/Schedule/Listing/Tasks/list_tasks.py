from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTasks(AbstractHandler):
    _tasks = None

    def __init__(self):
        if self.__class__ is ListTasks:
            ListTasks._tasks = None

    def get_steps(self) -> list:
        return [
            'check_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.Tasks'

    @staticmethod
    def set_tasks(tasks: list):
        ListTasks._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListTasks._tasks
