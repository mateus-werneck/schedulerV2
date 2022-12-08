
from App.Data.Helpers.message_helper import down_face, floppy_disk
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Grade.Create.create import Create


class SaveGrade(Create):

    def handle(self) -> bool:
        self.save()
        return super().handle()

    def save(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma turma válida.')
            return

        new_grade = self.create_grade()
        self.notify(new_grade)

    def create_grade(self):
        grade = self.get_grade_name()
        return MarinaAPI.instance().create_grade(grade)

    def get_grade_name(self):
        return self.get_text_data()

    def notify(self, grade: dict):
        if grade.get('id'):
            message = f'{floppy_disk()} Turma <b>{grade.get("name")}</b>'\
                + ' criada com sucesso.'
        else:
            message = f'{down_face()} Não consegui criar a turma' \
                + f'<b>{grade.get("name")}</b> para você.'

        self.send_message(message)
