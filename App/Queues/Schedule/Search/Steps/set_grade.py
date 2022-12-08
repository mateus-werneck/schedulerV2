from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Schedule.Search.search import Search


class SetGrade(Search):

    def handle(self) -> bool:
        grade = MarinaAPI.instance().find_grade(self.get_grade())

        if not grade:
            grade = {}

        self.set_grade(grade)
        return super().handle()
