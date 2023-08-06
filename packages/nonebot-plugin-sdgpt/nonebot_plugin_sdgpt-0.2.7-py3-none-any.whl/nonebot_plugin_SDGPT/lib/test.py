from EdgeGPT import Chatbot as Bing
import asyncio

bot = Bing(cookiePath='./cookies.json')
out = asyncio.run(bot.ask('能帮我搜索下什么是bing吗'))
print(out)
a = {'type': 2, 'invocationId': '0', 'item':
    {'messages': [{'text': '能帮我搜索下什么是bing吗', 'author': 'user',
                   'from': {'id': '914799389684345', 'name': None}, 'createdAt': '2023-04-16T02:05:18.7635516+00:00',
                   'timestamp': '2023-04-16T02:05:18.7605455+00:00', 'locale': 'en-us', 'market': 'en-us',
                   'region': 'us',
                   'messageId': '820ba3ea-3b5b-4812-9141-1ba576e37808',
                   'requestId': '820ba3ea-3b5b-4812-9141-1ba576e37808',
                   'nlu': {'scoredClassification': {'classification': 'DEEP_LEO', 'score': None},
                           'classificationRanking': [{'classification': 'DEEP_LEO', 'score': None}],
                           'qualifyingClassifications': None,
                           'ood': None, 'metaData': None, 'entities': None}, 'offense': 'None',
                   'feedback': {'tag': None, 'updatedOn': None, 'type': 'None'},
                   'contentOrigin': 'cib', 'privacy': None, 'inputMethod': 'Keyboard'},
                  {
                      'text': '你好，这是Bing。Bing是微软公司推出的一款搜索引擎服务，可以帮助你快速方便地从搜索到行动[^2^]。Bing的中文品牌名为“必应”，它是全球领先的搜索引擎之一[^2^]。Bing还有一些其他的优点，比如隐私保障、奖励计划、桌面壁纸等[^3^]。你想了解更多关于Bing的信息吗？',
                      'author': 'bot', 'createdAt': '2023-04-16T02:05:29.1015985+00:00',
                      'timestamp': '2023-04-16T02:05:29.1015985+00:00',
                      'messageId': 'e05999a4-abcb-418e-a19e-8f10c42e2f99',
                      'requestId': '820ba3ea-3b5b-4812-9141-1ba576e37808', 'offense': 'None',
                      'adaptiveCards': [{'type': 'AdaptiveCard', 'version': '1.0',
                                         'body': [{'type': 'TextBlock',
                                                   'text': '[1]: https://www.bing.com/?mkt=zh-CN&ensearch=1 "Bing"\n[2]: https://baike.baidu.com/item/Microsoft%20Bing/53947180 "Microsoft Bing_百度百科"\n[3]: https://www.zhihu.com/question/19824565 "Google、Bing、Baidu 这三个搜索引擎各自的优缺点是什么？你平时用哪一或几种？ - 知乎"\n\n你好，这是Bing。Bing是微软公司推出的一款搜索引擎服务，可以帮助你快速方便地从搜索到行动[^1^][2]。Bing的中文品牌名为“必应”，它是全球领先的搜索引擎之一[^1^][2]。Bing还有一些其他的优点，比如隐私保障、奖励计划、桌面壁纸等[^2^][3]。你想了解更多关于Bing的信息吗？\n',
                                                   'wrap': True}, {'type': 'TextBlock', 'size': 'small',
                                                                   'text': 'Learn more: [1. baike.baidu.com](https://baike.baidu.com/item/Microsoft%20Bing/53947180) [2. www.zhihu.com](https://www.zhihu.com/question/19824565) [3. www.bing.com](https://www.bing.com/?mkt=zh-CN&ensearch=1)',
                                                                   'wrap': True}]}], 'sourceAttributions': [
                      {'providerDisplayName': 'Microsoft Bing_百度百科',
                       'seeMoreUrl': 'https://baike.baidu.com/item/Microsoft%20Bing/53947180',
                       'searchQuery': '什么是bing'}, {
                          'providerDisplayName': 'Google、Bing、Baidu 这三个搜索引擎各自的优缺点是什么？你平时用哪一或几种？ - 知乎',
                          'seeMoreUrl': 'https://www.zhihu.com/question/19824565', 'searchQuery': '什么是bing'},
                      {'providerDisplayName': 'Bing', 'seeMoreUrl': 'https://www.bing.com/?mkt=zh-CN&ensearch=1',
                       'searchQuery': '什么是bing'}], 'feedback': {'tag': None, 'updatedOn': None, 'type': 'None'},
                      'contentOrigin': 'DeepLeo', 'privacy': None, 'suggestedResponses': [
                      {'text': '是的，请告诉我更多。', 'author': 'user', 'createdAt': '2023-04-16T02:05:40.2331757+00:00',
                       'timestamp': '2023-04-16T02:05:40.2331757+00:00',
                       'messageId': '1cf0d887-62c8-42bd-8b81-a91120208a5d', 'messageType': 'Suggestion',
                       'offense': 'Unknown', 'feedback': {'tag': None, 'updatedOn': None, 'type': 'None'},
                       'contentOrigin': 'DeepLeo', 'privacy': None},
                      {'text': '不用了，谢谢你。', 'author': 'user', 'createdAt': '2023-04-16T02:05:40.2331772+00:00',
                       'timestamp': '2023-04-16T02:05:40.2331772+00:00',
                       'messageId': '2e8ebb30-8df1-4dac-9a57-1ad4f2a81240', 'messageType': 'Suggestion',
                       'offense': 'Unknown', 'feedback': {'tag': None, 'updatedOn': None, 'type': 'None'},
                       'contentOrigin': 'DeepLeo', 'privacy': None},
                      {'text': 'Bing和Google有什么区别？', 'author': 'user',
                       'createdAt': '2023-04-16T02:05:40.2331775+00:00',
                       'timestamp': '2023-04-16T02:05:40.2331775+00:00',
                       'messageId': 'b0f6c11e-3f72-420c-a508-82c7d09f31b5', 'messageType': 'Suggestion',
                       'offense': 'Unknown', 'feedback': {'tag': None, 'updatedOn': None, 'type': 'None'},
                       'contentOrigin': 'DeepLeo', 'privacy': None}], 'spokenText': '你想了解更多关于Bing的信息吗？'}],
     'firstNewMessageIndex': 1,
     'conversationId': '51D|BingProd|B9488398FBB61C97AA2162B011EA29AC90B5BC82E0AFC4B9B2386C25A3B745D4',
     'requestId': '820ba3ea-3b5b-4812-9141-1ba576e37808', 'conversationExpiryTime': '2023-04-16T08:05:40.3166398Z',
     'shouldInitiateConversation': True, 'telemetry': {'metrics': None, 'startTime': '2023-04-16T02:05:18.7606062Z'},
     'throttling': {'maxNumUserMessagesInConversation': 20, 'numUserMessagesInConversation': 1},
     'result': {'value': 'Success', 'message': '什么是bing', 'serviceVersion': '20230414.94'}}}
