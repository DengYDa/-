from Functions.Func_base import Func
from pathlib import Path
from Config.Config import CFG, ROOT_PATH
import os
class Auto_Code(Func):
    """Auto coding and fitting bug"""
    def __init__(self,path:str):
        """羡慕路径不能为空"""
        if not path:
            raise ValueError('The path can not be None')
        if not isinstance(path,str):
            raise ValueError('The path must be str')
        self.path = path

    def get_env(self):
        #获取项目列表
        trees = self.get_dir_tree(self.path)

        return trees


    def get_dir_tree(self,path):
        tree = {os.path.basename(path): {'subdirs': [], 'files': []}}

        for dirpath, dirnames, filenames in os.walk(path):
            key = os.path.basename(dirpath)

            # 过滤掉以.开头的文件夹名
            dirnames = [d for d in dirnames if not d.startswith('.')]
            # 过滤名字中包含cache的目录
            dirnames = [d for d in dirnames if 'cache' not in d]


            # 只保留py文件
            filenames = [f for f in filenames if  f.endswith('.py')]


            tree[key] = {'subdirs': dirnames, 'files': filenames}

            for dirname in dirnames:
                subtree = self.get_dir_tree(os.path.join(dirpath, dirname))
                tree[key][dirname] = subtree

        return tree
    def auto_execute(self):
        """负责任务执行"""
        return 0


    def get_return(self):
        """负责返回任务执行的结果，以及结果的处理工作"""
        return 0


if __name__ == '__main__':
    auto_code = Auto_Code(ROOT_PATH)
    trees = auto_code.get_env()
    print(trees['nvwa-assistant'])
    print(trees['Functions'])
