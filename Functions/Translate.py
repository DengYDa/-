import requests
from Functions.Func_base import Func
from Config.Config import CFG, ROOT_PATH
import os
"""Used for translation languages"""

class Translate(Func):
    def __init__(self,):
        self.google_translate_url = 'https://google-translate1.p.rapidapi.com/language/translate/v2'
        self.google_translate_headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'application/gzip',
            'X-RapidAPI-Key': 'a3d1047aa2msh747ac8f00f55939p15a0ecjsn17c0854b8e01',
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
        }
        self.translate_q = '你好'
        self.translate_target = 'en'
        self.translate_source = 'zh'
        self.translate_google_data = {
            'q': self.translate_q,
            'target': self.translate_target,
            'source': self.translate_source
        }

        self.supported_languages_url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/languages'
        self.supported_languages_headers = {
            'Accept-Encoding': 'application/gzip',
            'X-RapidAPI-Key': 'a3d1047aa2msh747ac8f00f55939p15a0ecjsn17c0854b8e01',
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
        }


    def get_env(self):
        """测试网络条件，VPN是否正常，Google翻译API是否正常，网络是否正常，如果都正常，则返回可支持的翻译语言
        :return: str"""
        try:
            resp2 = requests.get('https://www.baidu.com')
        except:
            return "网络连接错误，请检查网络问题"
        else:
            try:
                resp1 = requests.get('https://www.google.com',timeout=3)
            except:
                return "VPN连接错误，请检查VPN问题"

        response = requests.get(self.supported_languages_url, headers=self.supported_languages_headers)
        if response.status_code != 200:
            return "Google翻译API连接错误，请检查API问题"
        else:
            supported_languages = response.json()['data']['languages']
            supported_languages = [i['language'] for i in supported_languages]
            print("可支持翻译有:",supported_languages)

        return """环境检查完毕，可以正常使用翻译功能"""

    def auto_execute(self,q,target = 'zh',source = 'en'):
        """默认翻译为英转中，如果需要其他语言，请指定target和source，例如：auto_execute('hello world','zh','en')
         :param q: 需要翻译的内容  str
         :param target: 目标语言  str
         :param source: 源语言  str
         :return: 翻译结果  str
        """
        self.translate_q = q
        self.translate_target = target
        self.translate_source = source
        self.translate_google_data = {
            'q': self.translate_q,
            'target': self.translate_target,
            'source': self.translate_source
        }
        response = requests.post(self.google_translate_url, headers=self.google_translate_headers, data=self.translate_google_data)
        result = response.json()['data']['translations'][0]['translatedText']
        return result

    def get_return(self):
        pass


if __name__ == '__main__':
    translate = Translate()
    print(translate.get_env())
    print(translate.auto_execute('hello world'))
    print(translate.auto_execute('你好','en','zh'))