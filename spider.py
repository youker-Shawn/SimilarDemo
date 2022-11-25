# -*- coding: utf-8 -*-
'''
@Time    :   2022-11-23 19:30:22
@File    :   spider.py
@author  :   youker-Shawn
@Desc    :   抓取各国人口数据
数据来源：https://www.geonames.org/countries/
'''
import json
import time
from typing import List
import requests
from lxml import etree
from geopy.geocoders import Nominatim

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
geolocator = Nominatim(user_agent=UA)


def extract(html_text: str) -> List[dict]:
    result = []
    with open("webpage.html", "r") as f:
        html_text = "".join(f.readlines())

    html = etree.HTML(html_text)
    countries = html.xpath('//table[@id="countries"]//tr[position()>1]')
    for country in countries:
        country_name = country.xpath('td[5]//text()')[0]
        country_continent = country.xpath('td[last()]//text()')[0]
        country_population = country.xpath('td[last()-1]//text()')[0]
        # print(country_name, country_population, country_continent)
        if country_name in ("Taiwan", "Hong Kong", "Macao"):
            continue

        country_population = int(''.join(country_population.split(',')))
        # key name is the same as CountryPopulation model's field
        result.append(
            {
                "name": country_name,
                "population": country_population,
                "continent": country_continent,
            }
        )

    return result


def main():
    # resp = requests.get("https://www.geonames.org/countries/")
    # with open("webpage.html", 'w') as f:
    #     f.write(resp.text)

    # extract_result = extract(resp.text)
    extract_result = extract("")
    # print(extract_result)

    source_data = []
    idx = 1
    for country in extract_result:
        try:
            location = geolocator.geocode(country["name"])
            country["latitude"] = location.latitude
            country["longitude"] = location.longitude
        except Exception as e:
            print(f'{country["name"]}, error:{e}')
            continue

        # print(country)
        source_data.append(
            {
                "pk": idx,
                "model": "demo.CountryPopulation",
                "fields": country,
            }
        )
        idx += 1

    with open('demo/fixtures/population.json', 'w') as f:
        json.dump(source_data, f, indent=4)


if __name__ == '__main__':
    main()
