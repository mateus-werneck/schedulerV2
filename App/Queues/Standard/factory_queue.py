from importlib import import_module
from App.Lib.Standard.abstract_singleton import AbstractSingleton


class FactoryQueue(AbstractSingleton):
    
    @staticmethod
    def create(namespace: str):
        module = FactoryQueue.get_module(namespace)
        class_name = FactoryQueue.get_class_name(namespace)
        queue_class = getattr(module, class_name)
        return queue_class()

    @staticmethod
    def get_module(namespace: str):
        module_namespace = f'{FactoryQueue.get_base_namespace()}.{namespace}'
        return import_module(module_namespace)

    @staticmethod
    def get_base_namespace():
        return 'App.Queues'
    
    @staticmethod
    def get_class_name(namespace: str):
        module_name = namespace.split('.').pop()
        name_parts = module_name.split('_')
        return ''.join([name.capitalize() for name in name_parts])