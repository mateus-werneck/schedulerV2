from App.Queues.Schedule.Listing.Daily.list_daily import ListDaily
from App.Queues.Standard.factory_queue import FactoryQueue


class ListAll(ListDaily):

    def handle(self):
        queue = FactoryQueue.create('Schedule.Listing.Tasks.list_tasks')
        queue.set_tasks(self.get_tasks())
        queue.init()
        return super().handle()
