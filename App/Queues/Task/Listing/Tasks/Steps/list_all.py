from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import category_icon
from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Handlers.task_handler import TaskHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Listing.Tasks.list_tasks import ListTasks


class ListAll(ListTasks):

    def handle(self):
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = TaskHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma opção {category_icon()}'

    def get_menu(self):
        menu_name = 'current_tasks'
        options = treat_keyboard(self.get_tasks(), menu_name) 
        append_exit_button(options, menu_name)
        return treat_menu(options)

    def get_tasks(self):
        schedules = MarinaAPI.instance().list_today_tasks()
        tasks = get_tasks_from_schedules(schedules)
        return list(map(self.treat_task, tasks))

    def treat_task(task: dict):
        return {
            'id': task.get('id'),
            'name': task.get('name')
        }
