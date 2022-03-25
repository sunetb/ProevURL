import requests
from html.parser import HTMLParser

link = "https://certificering.tbst.dk/?page=1&Fagdisciplin=0&Certificeringsniveau=0&SortTerm=postNr&AntalPrSide=2147483647"

f = requests.get(link)

html_text = f.text
my_global_var = ""


class MyDataObject:
    current_tag = ""


mdo = MyDataObject()



the_data = []


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # print("Start tag:", tag)
        mdo.current_tag = tag
        my_global_var = tag # Den er gal her



    def handle_endtag(self, tag):
        pass
        #print("End tag  :", tag) ##TODO: /tr

    def handle_data(self, data):
        if mdo.current_tag == 'tr':
            print("Datobject has 'tr'")
        if my_global_var == 'tr':
            print("global var has 'tr'")

print(html_text)
parser = MyHTMLParser()
parser.feed(html_text)
print("===============tjek data================")
print(len(the_data))

