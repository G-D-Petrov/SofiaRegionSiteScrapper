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

def triaditsa_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".entry-content > p > a")
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

def ilinden_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".span9")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        p_item = item.select("p")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = datetime.strptime(p_item.text.split()[-1].strip(), "%d/%m/%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list


def nadejda_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".card-body")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        p_item = item.select("small")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = datetime.strptime(p_item.text.strip(), "%d/%m/%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def iskar_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".article")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        # p_item = item.select("small")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = datetime.strptime(item.select(".date-and-category")[0].text.strip(), "%d.%m.%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def mladost_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".news-content")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        # p_item = item.select("small")[0]
        title = item.select(".news-title")[0].text.strip()
        link = a_item['href']
        date = datetime.strptime(item.select(".date")[0].text.strip(), "%d.%m.%y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })

    return result_list

def studentski_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("article")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        # p_item = item.select("small")[0]
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

#TODO
def vitosha_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#tab3 > article > p")
    result_list = []
    
    for item in items: 
        try:
            span = item.select("span > span")[0]
            title = span.select('strong')[0].text
            link = "https://www.raionvitosha.eu/bg/service/obavlienia-ustroistvo-kadastar-regulacia"
            date = span.select('span')[0].text
            if title == date:
                continue
        except Exception as ex:
            continue
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def ovcha_kupel_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".entry-info")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        # p_item = item.select("small")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
    return result_list

def lyulin_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".jet-listing-dynamic-link__link")
    # items = soup.select(".a")
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

def novi_iskar_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("#tab3 > ul > li")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        title = a_item.text.strip()
        link = a_item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def pancharevo_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".entry-header")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        title = a_item.text.strip()
        link = "http://www.pancharevo.org/" + a_item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def bankya_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".post")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        title = a_item.text.strip()
        link = "http://www.bankya.bg/" + a_item['href']
        date = datetime.strptime(item.select(".date")[0].text.strip(), "%d.%m.%Y")
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def vazrajdane_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".messages")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        title = a_item.text.strip()
        link = "http://www.bankya.bg/" + a_item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def krasna_polqna_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select(".jd_content_file")
    result_list = []
    
    for item in items: 
        a_item = item.select("a")[0]
        title = item.text.strip()
        link = "https://www.krasnapoliana.com/" + a_item['href']
        date = ""
        #TODO: refactor this as a dataclass?
        result_list.append({
            "Date": date,
            "Title": title,
            "Link": link
        })
        
    return result_list

def obshtina_parser(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    items = soup.select("tr")
    result_list = []
    for item in items:
        try:
            a_elem = item.select("a")[0]
        except Exception as ex:
            continue
        title = a_elem.text
        link = a_elem['href']
        date = ""

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
    # "Vazrajdane": vazrajdane_parser,
    # "Oborishte": oborishte_parser,
    "Serdika": None,
    # "Poduiane": poduiane_parser,
    # "Slatina": slatina_parser,
    # "Izgrev": izgrev_parser,
    # "Lozenets": lozenets_parser,
    # "Triaditsa": triaditsa_parser,
    # "KrasnaPolqna": krasna_polqna_parser,
    # "Ilinden": ilinden_parser,
    # "Nadejda": nadejda_parser,
    # "Iskar": iskar_parser,
    # "Mladost": mladost_parser,
    # "Studentski": studentski_parser,
    "Vitosha": None,
    # "OvchaKupel": ovcha_kupel_parser,
    # "Lyulin": lyulin_parser,
    "Vrabnitsa": None,
    # "NoviIskar": novi_iskar_parser,
    "Kremikovci": None,
    # "Pancharevo": pancharevo_parser,
    # "Bankya": bankya_parser,
    "Obshtina": obshtina_parser,
}
