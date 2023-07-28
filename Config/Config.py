import os

import pytest

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGDIR = os.path.join(ROOT_PATH, "logs")

class Config():

    def __init__(self):
        #传统数据库相关配置
        self.LOCAL_DB_HOST = os.getenv("LOCAL_DB_HOST", None)
        self.LOCAL_DB_PORT = int(os.getenv("LOCAL_DB_PORT", 3306))
        self.LOCAL_DB_USER = os.getenv("LOCAL_DB_USER", None)
        self.LOCAL_DB_PASSWORD = os.getenv("LOCAL_DB_PASSWORD", None)
        self.LOCAL_DB_DATABASES = os.getenv("LOCAL_DB_DATABASES", None)

        #向量数据库相关配置
        self.LOCAL_VC_HOST = os.getenv("LOCAL_VC_HOST", None)
        self.LOCAL_VC_PORT = int(os.getenv("LOCAL_VC_PORT", 3306))
        self.LOCAL_VC_USER = os.getenv("LOCAL_VC_USER", None)
        self.LOCAL_VC_PASSWORD = os.getenv("LOCAL_VC_PASSWORD", None)
        self.LOCAL_VC_DATABASES = os.getenv("LOCAL_VC_DATABASES", None)

        #claude2的接口
        self.LAF_CLAUDE2 = os.getenv("LAF_CLAUDE2", None)





CFG = Config()

if __name__  == "__main__":
    pytest.main()
    print(ROOT_PATH)
