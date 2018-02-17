import urllib.request

page = urllib.request.urlopen("http://ww1.beans-r-us.biz/caf/?ses=Y3JlPTE1MTgzNDEzMTYmdGNpZD13dzEuYmVhbnMtci11cy5iaXo1YTgwMGNjNDQ4Y2FhOC42NDY3NTcxNCZma2k9MCZ0YXNrPXNlYXJjaCZkb21haW49YmVhbnMtci11cy5iaXombGFuZ3VhZ2U9ZW4mYV9pZD0zJnNlc3Npb249SVBkeTZiRWFtMDBHc2NZSG1ZTl8=&query=Coffee%20Beans&afdToken=3B1g-zXTOfithH6-wvTMPkazgrc57WkU8sEwrX-Udjj_-_jszNlzH5TcncFscfAeY3I0n13PXir82JoX6_hyPQqCxnJsVPaYDPll30vFEg")
text = page.read().decode("utf-8")

print(text)
