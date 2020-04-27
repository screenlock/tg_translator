import requests as r
def translate(text):
    Req = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190911T200326Z.6c0980e17bfe689c.8726e5ecba09e515e96dda3f65c73e7e116c5886&text="+text+"&lang=en-ru"
    Answ = r.get(Req)
    return Answ.text[36:-3]
