from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Grade.Listing.GradeOptions.list_grades_options import \
    ListGradesOptions


class GradeHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.list_options]

    def list_options(self):
        self.grade = self.get_callback_data()
        ListGradesOptions().init()
