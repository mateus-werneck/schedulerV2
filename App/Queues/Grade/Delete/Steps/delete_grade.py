
from App.Data.Helpers.message_helper import delete_icon, down_face
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Grade.Delete.delete import Delete


class DeleteGrade(Delete):

    def handle(self) -> bool:
        deleted = self.delete_grade()
        self.notify(deleted)
        return super().handle()

    def delete_grade(self):
        grade = self.get_grade()
        return MarinaAPI.instance().delete_grade(grade)

    def notify(self, grade: dict):
        if grade.get('id'):
            message = f'{delete_icon()} Turma deletada com sucesso.'
        else:
            message = f'{down_face()} Não consegui deletar a turma para você.'

        self.send_message(message)
