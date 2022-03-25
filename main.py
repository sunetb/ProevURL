import requests
from html.parser import HTMLParser
my_global_var = ""
link = "https://certificering.tbst.dk/?page=1&Fagdisciplin=0&Certificeringsniveau=0&SortTerm=postNr&AntalPrSide=2147483647"

f = requests.get(link)

html_text = f.text




class MyDataObject:
    current_tag = ""


mdo = MyDataObject()


class MyHTMLParser(HTMLParser):
    my_object_global_var = ""

    def handle_starttag(self, tag, attrs):
        # print("Start tag:", tag)
        mdo.current_tag = tag
        my_global_var = tag # Den er gal her
        self.my_object_global_var = tag


    def handle_data(self, data):
        if mdo.current_tag == 'tr': #virker
            print("Datobject has 'tr'")
        if my_global_var == 'tr':   #Virker ikke
            print("global var has 'tr'")
        if self.my_object_global_var == 'tr':    #Crasher uden 'self'
            print("Object global var has 'tr'")

print(html_text)
parser = MyHTMLParser()
parser.feed(html_text)


