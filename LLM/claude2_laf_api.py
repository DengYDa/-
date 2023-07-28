import pytest
import requests
import os
import json
from datetime import datetime
from Config.Config import CFG, ROOT_PATH


class LAF_claude2():

    def __init__(self):
        self._url = CFG.LAF_CLAUDE2
        self._parentId = None
        self._history = {"user":[],"claude2":[]}
        self._file_name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')


    #单轮对话测试使用
    def claude2(self,url: str, content: str, parentId: str = None):
        query = {"content": content, "parentID": parentId}
        response = requests.get(self._url, params=query)
        response = eval(response.text)  # 转换为字典格式
        restore = response['res']['completion']  # 回复的内容
        context = response['parentId']  # 保留上下文

        return restore,context  # 转换为字典格式

    #多轮对话使用
    def chat(self,input: str):
        query = {"content": input, "parentId": self._parentId}
        response = requests.get(self._url, params=query)
        response = eval(response.text)  # 转换为字典格式
        restore = response['res']['completion']  # 回复的内容
        self._parentId = response['parentId']  # 保留上下文
        #输出对话记录
        self._history['user'].append(input)
        self._history['claude2'].append(restore)
        for x,y in zip(self._history['user'],self._history['claude2']):
            print(f"User: {x}")
            print(f"Claude2: {y}")

    def close(self):
        """关闭旧的对话，并将记录保存起来"""
        history_path = os.path.join(ROOT_PATH, 'chat_history')
        # 判断目录是否存在,不存在则创建
        if not os.path.exists(history_path):
            os.makedirs(history_path)
        file_path = os.path.join(history_path, self._file_name)
        with open(file_path + ".txt",'w') as f:
            for x, y in zip(self._history['user'], self._history['claude2']):
                f.write(x)
                f.write('\n')
                f.write(y)
        #重置
        self._parentId = None
        self._history = {"user": [], "claude2": []}
        self._file_name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')


if __name__ == "__main__":
    pytest.main()
    Claude = LAF_claude2()
    Claude.chat("请你记住这句话,[今天天气不错]")
    Claude.chat("我需要你复述我刚才让你记住的话")
    Claude.close()


