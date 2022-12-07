from App.Queues.Task.Listing.Tasks.list_tasks import ListTasks
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Bot.client import BotClient
from App.Lib.Bot.chat import BotChat
from App.Handlers.task_handler import TaskHandler
from App.Data.Helpers.message_helper import category_icon
from App.Data.Helpers.inline_keyboard_helper import treat_menu, append_exit_button


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
        options = self.get_tasks()
        append_exit_button(options)
        return treat_menu(options, 'current_tasks')

    def get_tasks(self):
        schedules = MarinaAPI.instance().list_today_tasks()
        tasks = [task for task in [schedule.get(
            'tasks') for schedule in schedules]]
        return list(map(self.treat_task, tasks))

    def treat_task(task: dict):
        return {
            'id': task.get('id'),
            'name': task.get('name')
        }
