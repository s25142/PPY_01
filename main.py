import webbrowser
import requests
if __name__ == '__main__':
    website = input("Podaj stronę internetową: ")


    url1 = "http://archive.org/wayback/available?url=" + website + "&timestamp=" + "20000712"
    url2 = "http://archive.org/wayback/available?url=" + website + "&timestamp=" + "20050218"
    url3 = "http://archive.org/wayback/available?url=" + website + "&timestamp=" + "20120621"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    d1 = response1.json()
    d2 = response2.json()
    d3 = response3.json()
    page1 = d1["archived_snapshots"]["closest"]["url"]
    page2 = d2["archived_snapshots"]["closest"]["url"]
    page3 = d3["archived_snapshots"]["closest"]["url"]

    webbrowser.open(page1)
    webbrowser.open(page2)
    webbrowser.open(page3)

