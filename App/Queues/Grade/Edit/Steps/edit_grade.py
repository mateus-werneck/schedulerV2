
from App.Data.Helpers.message_helper import down_face, edit_icon
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Grade.Edit.edit import Edit


class EditGrade(Edit):

    def handle(self) -> bool:
        updated = self.edit_grade()
        self.notify(updated)
        return super().handle()

    def edit_grade(self):
        grade = self.get_grade()
        name = self.get_text_data()
        return MarinaAPI.instance().update_grade(grade, name)

    def notify(self, grade: dict):
        if grade.get('id'):
            message = f'{edit_icon()} Turma <b>{grade.get("name")}</b>'\
                + ' alterada com sucesso.'
        else:
            message = f'{down_face()} Não consegui alterar a turma' \
                + f' <b>{grade.get("name")}</b> para você.'

        self.send_message(message)
