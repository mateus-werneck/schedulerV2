from App.Queues.Schedule.Listing.Monthly.list_monthly import ListMonthly
from App.Queues.Standard.factory_queue import FactoryQueue


class ListAll(ListMonthly):

    def handle(self):
        queue = FactoryQueue.create('Schedule.Listing.Tasks.list_tasks')
        queue.set_tasks(self.get_tasks())
        queue.init()
        return super().handle()
