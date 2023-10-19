from claude_api import Client


cookie = 'intercom-device-id-lupk8zyo=bfbbe24e-28c1-408b-9e58-4958f5969f1f; sessionKey=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; __ssid=1c689d613573fae2cc17c4739a4272f; activitySessionId=3537f2a0-65d6-4c84-9717-ea589e08f5de; cf_clearance=EuKw3QlJ3vVehmRL9cducF.o8RzIjHLaeCIRvOAiZ1M-1696855940-0-1-839f5b0e.df8f7bd3.d49e04ee-0.2.1696855940; intercom-session-lupk8zyo=L2M0d2JYR2huZG5zaWlXWDJ0SXlOMUZlSXNETTZDSjh1d2pGd0ovTlNPQXV3aVZaYmh6NXJTbFRMZTB4OVJHSi0tSXBSSkh2dmtIU2tNYWtpVUY3Tkh2QT09--b30b9ef091a4d45741766a220f83191aaddac3eb; __cf_bm=pXFwCOfbNDpUUkKT5y3rzi2m_yBQ09SKD0ACceacQKg-1696856857-0-AUi2uu4rWKW6nvqI4SIp5D3s1GIun7z9GOhxY2swC9TJ8qvxyuwKoqmoj43dVQTjl81I/rzmPahpElfsE7575oA='
claude_copilot = Client(cookie)

#conversations = claude_copilot.list_all_conversations()
#for conversation in conversations:
#    conversation_id = conversation['uuid']
#    print(conversation_id)

def test():
    url = "https://claude.ai/api/organizations"

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://claude.ai/chats',
        'Content-Type': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
        'Cookie': f'{self.cookie}'
    }

    response = self.send_request("GET", url, headers=headers)
