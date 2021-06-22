from newsapi import NewsApiClient

# クライアントを初期化
newsapi = NewsApiClient(api_key='c8ac3154f53c47cb992f106527e9cd51')

# categoryをbusiness、国をjpに指定してニュースを取得
headlines = newsapi.get_top_headlines(category='business')

if headlines['totalResults'] > 0:
    print(headlines['totalResults'])
    print(headlines['articles'][0]['description'])
else:
    print("条件に合致したトップニュースはありません。")
