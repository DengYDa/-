import baidu
from Config.Config import CFG
import json
import requests

#access_token = baidu.access_token(CFG.client_id,CFG.client_secret)



class LLM():
    def __init__(self,access_token,api_name = 'qianfan_chinese_llama_2_7b',history = []):
        self.access_token = access_token
        self.history = history
        self.api_name = api_name

    def chat(self,input):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/"+ \
               self.api_name +"?access_token=" + self.access_token

        inpt = {
                    "role": "user",
                    "content": input
                }
        self.history.append(inpt)

        payload = json.dumps({
            "messages": self.history
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        result = response.json().get("result")

        reback = {
            "role": "assistant",
            "content": result
        }
        self.history.append(reback)

        print(result)

        return result


if __name__ == '__main__':
    access_token = baidu.Access_token(CFG.client_id,CFG.client_secret)
    Copilot = LLM(access_token,api_name='llama_2_13b')
    _ = Copilot.chat("你会说中文吗？")
    #_ = Copilot.chat("我刚刚和你说了什么？")
