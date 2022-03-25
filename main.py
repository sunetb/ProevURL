import requests
from html.parser import HTMLParser

link = "https://certificering.tbst.dk/?page=1&Fagdisciplin=0&Certificeringsniveau=0&SortTerm=postNr&AntalPrSide=2147483647"

f = requests.get(link)

html_text = f.text

my_global_var = ""


class MyDataObject:
    current_tag = ""


mdo = MyDataObject()


class MyHTMLParser(HTMLParser):
    my_object_global_var = ""

    def handle_starttag(self, tag, attrs):
        # print("Start tag:", tag)
        mdo.current_tag = tag
        my_global_var = tag # Den er gal her
        my_object_global_var = tag


    def handle_data(self, data):
        if mdo.current_tag == 'tr': #virker
            print("Datobject has 'tr'")
        if my_global_var == 'tr':   #Virker ikke
            print("global var has 'tr'")
       # if my_object_global_var == 'tr':    #Crasher?
       #     print("Object global var has 'tr'")

print(html_text)
parser = MyHTMLParser()
parser.feed(html_text)


