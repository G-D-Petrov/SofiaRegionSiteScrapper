from bs4 import BeautifulSoup

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
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

parsers_dict = {
    "Sredec": sredec_parser,
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
