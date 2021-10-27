from bs4 import BeautifulSoup
from datetime import datetime

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
            date = ""
            title = ""
            link = item.find("a")['href']
        except Exception as ex:
            print(item)
            exit()
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

parsers_dict = {
    # "Sredec": sredec_parser,
    "Sofia": sofia_parser,
    "KrasnoSelo": None,
    "Vazrajdane": None,
    "Oborishte": None,
    "Serdika": None,
    "Poduiane": None,
    "Slatina": None,
    "Izgrev": None,
    "Lozenets": None,
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
