from bs4 import BeautifulSoup
from datetime import datetime
import re

def sredec_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#container > ul > li")
    result_list = []
    for item in items:
        date = item.find("em").text
        #TODO: find a better selector
        a_elem = item.find("a")
        link = a_elem['href']
        title = a_elem['title'].strip()
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def krasno_selo_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#right > div.cont > div.ctxt > div.fnt_siz > p")
    result_list = []
    for item in items:
        try:
            a_elem = item.find("a")
            if item.text.isspace() or not a_elem:
                continue
            start = item.text.find("публикувано на ")
            if start == -1:
                continue

            date = item.text[start + len("публикувано на "):]
            match = re.search(r'\d+(.|-)\d+(.|-)\d+', date)
            date = datetime.strptime(match.group(), "%d.%m.%Y").date()
            title = a_elem.text
            link = a_elem['href']
        except Exception as ex:
            print(ex)
            print(date)
            print(item)
            continue
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list


def sofia_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#p_p_id_101_INSTANCE_f7DDrCt6UHSA_ > div > div > table > tbody > tr")
    result_list = []
    for item in items:
        date = datetime.strptime(item.select("td")[1].text.strip(), "%d.%m.%Y")
        a_elem = item.find("a")
        title = a_elem.text
        link = a_elem['href']

        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def oborishte_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("article")
    result_list = []
    for item in items:
        # date = datetime.strptime(item.select("td")[1].text.strip(), "%d.%m.%Y")
        a_elem = item.select("h2 > a")[0]
        title = a_elem.text
        link = a_elem['href']
        date = datetime.strptime(item.select('.txt')[0].text.strip(), "%d.%m.%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def poduiane_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".articleTitle > a")
    result_list = []
    
    for item in items:
        title = item.text.strip()
        link = item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def slatina_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    print(soup)
    items = soup.select(".maincolor2hover")
    result_list = []
    
    for item in items:
        print(item)
        # title = item.text.strip()
        # link = item['href']
        # date = ""
        # #TODO: refactor this as a dataclass?
        # result_list.append({
        #     "Date": date,
        #     "Title": title,
        #     "Link": link
        # })

    return result_list

def izgrev_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#content > div.blogger.imgsmall > div")
    result_list = []
    
    for item in items:
        a_item = item.select(".link--forsure")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = datetime.strptime(item.select("p.p-border")[0].text.strip(), "%d.%m.%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list


def lozenets_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".blog-entry")
    result_list = []
    
    for item in items:
        a_item = item.find("a")
        title = a_item.text.strip()
        link = a_item['href']
        date = datetime.strptime(item.select(".updated")[0].text.strip(), "%d.%m.%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

parsers_dict = {
    # "Sredec": sredec_parser,
    # "Sofia": sofia_parser,
    # "KrasnoSelo": krasno_selo_parser,
    "Vazrajdane": None,
    # "Oborishte": oborishte_parser,
    "Serdika": None,
    # "Poduiane": poduiane_parser,
    # "Slatina": slatina_parser,
    # "Izgrev": izgrev_parser,
    "Lozenets": lozenets_parser,
    "Triaditsa": None,
    "KrasnaPolqna": None,
    "Ilinden": None,
    "Nadejda": None,
    "Iskar": None,
    "Mladost": None,
    "Studentski": None,
    "Vitosha": None,
    "OvchaKupel": None,
    "Lyulin": None,
    "Vrabnitsa": None,
    "NoviIskar": None,
    "Kremikovci": None,
    "Pancharevo": None,
    "Bankya": None,
}
