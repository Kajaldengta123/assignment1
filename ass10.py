import requests
response=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&jsonp=?" )
print(response.status_code)
b'?({"quoteText":"fears are nothing more than a state of mind ","QuoteAuthor":"nepolion hill","senderName":"","senderLink":""})'
