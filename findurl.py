import re
import csv
import pandas as pd

def find_sources(string):
    url_https = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    if len(url_https) != 0:
        return url_https
    url_www = re.findall('www?.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    if len(url_www):
        return url_www
    return 0

def find_domain(test_str):
	print("Dostałem: ", test_str)
	test_str = test_str.replace("https://www.", "")
	test_str = test_str.replace("http://www.", "")
	test_str = test_str.replace("https://", "")
	test_str = test_str.replace("http://", "")
	domena = test_str.split("/")[0]
	return domena

def get_url(text):
	return text.split(",")[1]

def check(text):
    fake_source_found = 0
    # zaladuj pliki .csv do dataframe
    df_1 = pd.read_csv('politifact_fake.csv')
    df_2 = pd.read_csv('gossipcop_fake.csv')
    # ekstrakcja URL źródeł do sprawdzenia
    sources_list = find_sources(text)
    print("Zrodla ktore znalazlem: ", sources_list)
    no_of_elements = len(sources_list)
    print("Liczba elementow w liscie to: ", no_of_elements)
    for i in range(0, no_of_elements):
        # "gola" domena z listy zrodel
        checked_domain = find_domain(sources_list[i])
        print("Sprawdzana domena to: ", checked_domain)
        # sprawdz czy adres znajduje sie w ktorejs z dfow
        # RAMKA 1: INDEKSY 0-431
        for x in range(0 - 432):
            fake_domain = find_domain(df_1.loc[x, 'news_url'])
            print("Falszywa domena do ktorej sprawdzam: ",fake_domain)
            if checked_domain == fake_domain:
                fake_source_found = 1
                print("Znaleziono falszywa domene. Sprawdzana domena: ", checked_domain, "fake z bazy: ", fake_domain)
                break
        # RAMKA 2: INDEKSY 0 - 5322
        for y in range(0 - 5323):
            fake_domain = find_domain(df_2.loc[y, 'news_url'])
            print("falszywa domena do ktorej sprawdzam: ", fake_domain)
            if checked_domain == fake_domain:
                fake_source_found = 1
                print("Znaleziono falszywa domene. Sprawdzana domena: ", checked_domain, "fake z bazy: ", fake_domain)
                break
    #print(df_1.loc[:, 'news_url'])
    #print(df_2.loc[:, 'news_url'])
    return fake_source_found




def main():
    #tekst artykułu
    text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples https://theglobalheadlines.net/kutas</a>'
    if(check(text)):
        print("Domene znaleziono w bazie danych")
    else:
        print("Domeny nie znaleziono w bazie danych")

if __name__ == "__main__":
    main()