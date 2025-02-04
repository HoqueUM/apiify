from apiify.GetContent import GetContent
url = 'https://www.marketwatch.com/story/wall-street-braces-for-more-volatility-ahead-as-trumps-tariffs-rock-markets-bb0ee587?mod=home-page'
data = ['Title', 'Author', 'Date', 'Content']
gc = GetContent(data, url)
result = gc.extract()