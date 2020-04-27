import requests as r
def translate(text):
    Req = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=*REPLACE WITH YOUR API KEY*&text="+text+"&lang=en-ru"
    Answ = r.get(Req)
    return Answ.text[36:-3]
