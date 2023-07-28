import  logging

from typing import Any




class Log():
    Main_Logger:Any
    User_logger: Any
    Func_logger: Any
    LLM_logger: Any
    Memory_logger: Any

    def __init__(self):
        self.Main_Logger = None
        self.User_Logger = None
        self.Func_logger = None
        self.Memory_Logger = None
        self.LLM_Logger = None

    @staticmethod
    def Main_logger(self):
        self.Main_Logger = logging.getLogger("main")
        self.Main_Logger.setLevel(logging.INFO)

        return self.Main_Logger

    @staticmethod
    def User_logger(self):
        self.User_Logger = logging.getLogger("User")
        self.User_Logger.setLevel(logging.INFO)

        return self.User_Logger

    @staticmethod
    def Func_logger(self):
        self.Func_Logger = logging.getLogger("Func")
        self.Func_Logger.setLevel(logging.INFO)

        return self.Func_Logger

    @staticmethod
    def LLM_logger(self):
        self.LLM_Logger = logging.getLogger("LLM")
        self.LLM_Logger.setLevel(logging.INFO)

        return self.LLM_Logger

    @staticmethod
    def Memory_logger(self):
        self.Memory_Logger = logging.getLogger("Memory")
        self.Memory_Logger.setLevel(logging.INFO)

        return self.Memory_Logger

if __name__ =="__main__":
    pass