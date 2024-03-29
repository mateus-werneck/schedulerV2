from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import add_icon, category_icon, down_face
from App.Handlers.tasks_handler import TasksHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Treat.date_treat import (treat_datetime_to_pt_date,
                                      treat_node_string)
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour
from App.Queues.Grade.Listing.Tasks.list_tasks import ListTasks


class ListAll(ListTasks):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        if not menu:
            return
        callback_function = TasksHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)
        TasksHandler.instance().set_grade(self.get_grade())

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()

        if not menu:
            self.send_message(f'{down_face()} Nenhuma tarefa foi encontrada.')
            return None

        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma tarefa {category_icon()}'

    def get_menu(self):
        options = self.get_options()

        if not options:
            return None

        menu_name = 'main_tasks'
        options = treat_keyboard(options, menu_name)
        append_exit_button(options, menu_name)
        return treat_menu(options)

    def get_options(self):
        grade = self.get_grade()
        tasks = MarinaAPI.instance().list_grade_tasks(grade)
        return [self.treat_task(task) for task in tasks]

    def treat_task(self, task: dict):
        deadline = treat_node_string(task.get('deadLine'))
        deadline_date = treat_datetime_to_pt_date(deadline)
        deadline_hour = treat_datetime_to_string_hour(deadline)

        return {
            'id': task.get('id'),
            'name': f'{task.get("name")} - {deadline_date} - {deadline_hour}'
        }
