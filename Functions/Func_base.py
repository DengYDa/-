from abc import ABC, abstractmethod



class Func(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_env(self):
        """用来获取执行环境"""
        pass


    @abstractmethod
    def auto_execute(self):
        """负责任务执行"""
        pass

    @abstractmethod
    def get_return(self):
        """负责返回任务执行的结果，以及结果的处理工作"""
        pass