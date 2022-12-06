from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (category_icon,
                                             cross_mark_icon, edit_icon)
from App.Handlers.task_handler import TaskHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Task.Listing.TaskOptions.list_task_options \
    import ListTaskOptions


class ListCategories(ListTaskOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = TaskHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)
        TaskHandler.instance().set_task(self.get_task())

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma opção {category_icon()}'

    def get_menu(self):
        options = self.get_options()
        append_exit_button(options)
        return treat_menu(options, 'main_task')

    def get_options(self):
        return [
            {
                'id': 'edit_task',
                'name': f'{edit_icon()} Editar Tarefa'
            },
            {
                'id': 'delete_task',
                'name': f'{cross_mark_icon()} Deletar Tarefa'
            }
        ]
