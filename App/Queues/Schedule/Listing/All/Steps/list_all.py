from App.Queues.Schedule.Listing.All.list_all_tasks import ListAllTasks
from App.Queues.Standard.factory_queue import FactoryQueue


class ListAll(ListAllTasks):

    def handle(self):
        queue = FactoryQueue.create('Schedule.Listing.Tasks.list_tasks')
        queue.set_tasks(self.get_tasks())
        queue.init()
        return super().handle()
