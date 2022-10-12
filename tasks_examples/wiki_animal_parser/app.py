"""
Component for parsing specific animals for specific collateral adjectives
"""

__author__ = 'Ivan Sushkov'
__maintainer__ = 'Ivan Sushkov'
__version__ = "1.00"

import logging
import requests
from typing import Union
from collections import defaultdict
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from concurrent.futures import ThreadPoolExecutor, as_completed


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class WikiAnimalParser:
    TMP_PATH = 'tmp/'
    WIKI_URL = 'https://en.wikipedia.org'
    ANIMAL_PAGE_PATH = '/wiki/List_of_animal_names'


    def __call__(self):
        if result := self.parse_wiki_page_content(self.WIKI_URL + self.ANIMAL_PAGE_PATH):
            self.generate_html_page(result)

            return result


    @staticmethod
    def get_wiki_page_content(url: str) -> bytes:
        """
        Request to wiki page and return response content if response status code is 200
        """

        # This headers helps o fix issue with getting some images from wikipedia
        headers = {
            'User-Agent':                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                         'Chrome/56.0.2924.76 Safari/537.36',
            "Upgrade-Insecure-Requests": "1",
            "DNT":                       "1",
            "Accept":                    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":           "en-US,en;q=0.5",
            "Accept-Encoding":           "gzip, deflate"
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.content
        else:
            logger.error("Request to Wiki Page %s failed with response status code %s", url, response.status_code)


    def parse_page_tables(self, url: str) -> ResultSet:
        """
        Parse page tables with class 'wikitable'
        """

        if page_content := self.get_wiki_page_content(url):
            wiki_page_soup = BeautifulSoup(page_content, 'html.parser')
            return wiki_page_soup.find_all('table', attrs={'class': 'wikitable'})


    @staticmethod
    def parse_table_rows(table: Union[Tag, ResultSet]) -> ResultSet:
        """
        Parse all table tows.
        """

        table_body = table.find('tbody')

        return table_body.find_all('tr')


    @staticmethod
    def parse_generic_terms_column(table_rows: ResultSet) -> list:
        """
        Parse Generic terms table and return list of Collateral adjective values. Example:
        ['viverrine', 'procyonine', 'nasuine', 'others']
        """

        table_data = []

        for row in table_rows:
            table_data.append([ele.text.strip() for ele in row.find_all('td')])

        return [col_adj for row_data in table_data if row_data for col_adj in row_data[5].split(', ')]


    @staticmethod
    def write_file(path: str, mode: str, content: Union[str, bytes]):
        """
        Write files according to specified path, mode and content.
        """

        with open(path, mode) as f:
            f.write(content)
            f.close()


    def parse_animal_image(self, page_path: str) -> str:
        """
        Get Wiki page content, parse this page. If page contains infobox table with image in the second table row -
        download this image in tmp folder and return path to this image.
        """

        try:
            wiki_page_soup = BeautifulSoup(self.get_wiki_page_content(self.WIKI_URL + page_path),
                                           'html.parser')
            infobox_table = wiki_page_soup.find('table', attrs={'class': 'infobox'})
            table_rows = self.parse_table_rows(infobox_table)

            if image_url := table_rows[1].find('img')['src']:
                file_format = '.' + image_url.split('.')[-1]
                image_path = self.TMP_PATH + page_path.split('/')[2].replace(' ', '_') + file_format

                if image_bytes := self.get_wiki_page_content('https:' + image_url):
                    self.write_file(image_path, "wb", image_bytes)
                    logger.debug("Image saved to %s", image_path)

                    return image_path

        except Exception as e:
            logger.error("Failed to parse and download image from %s, error: %s", page_path, e)


    @staticmethod
    def clean_animal_name(text: str) -> str:
        """
        Clean animal name, example:
        Cat (list) -> Cat
        Cattle[c] (list) -> Cattle
        """

        return text.split('(')[0].split('[')[0]


    def parse_terms_by_species_table(self, table_rows: ResultSet, collateral_adjectives: list) -> dict:
        """
        Parse Terms by species table data based on Collateral Adjectives list and return a dictionary in format:

        {
            'nasuine': [{'name': 'Coati', 'image_path': 'tmp/Coati.jpg'}],
            'canine':  [{'name': 'Coyote', 'image_path': 'tmp/Coyote.jpg'},
                        {'name': 'Dingo', 'image_path': 'tmp/Dingo.jpg'},
                        {'name': 'Dog (list)', 'image_path': 'tmp/Dog.jpg'},
                        {'name': 'Pelican', 'image_path': 'tmp/Pelican.jpg'},
                        {'name': 'Wolf', 'image_path': 'tmp/Wolf.jpg'}],
        }

        """

        def animal_parser(row, col_adjs):
            # here we assume that collateral adjective appears only once in 6 column of the table
            for col_adj in col_adjs:
                if col_adj in str(row):
                    all_td = row.find_all('td')

                    return col_adj, {
                        'name':       self.clean_animal_name(all_td[0].text.strip()),
                        'image_path': self.parse_animal_image(all_td[0].find('a')['href'])
                    }

        table_data = defaultdict(list)

        # We can use a with statement to ensure threads are cleaned up promptly
        with ThreadPoolExecutor(max_workers=60) as executor:
            # Start the load operations and mark each future with its row
            row_to_dict = {executor.submit(animal_parser, row, collateral_adjectives): row for row in table_rows}
            for future in as_completed(row_to_dict):
                if result := future.result():
                    table_data[result[0]].append(result[1])

        return dict(table_data)


    def generate_html_page(self, table_data: dict):
        """
        Generate html page with table based on animals data. Example:

        <html>
        <body>
        <table style=font-size:20px;font-weight: bold;>
        <tr>
        <td style=vertical-align:top; rowspan=7>musteline</td>
        <td style=vertical-align:top;>Badger</td>
        <td><img width=200 src=tmp/Badger.jpg></td>
        </tr>
        <tr>
        <td style=vertical-align:top;>Ferret</td>
        <td><img width=200 src=tmp/Ferret.png></td>
        </tr>
        </table>
        </body>
        </html>

        """

        def build_img_tag(image_path):
            return f"<img width=200 src={image_path}>" if image_path else ""

        table = "<html>\n<body>\n<table style=font-size:20px;font-weight: bold;>\n"

        for col_adj, animals in table_data.items():
            table += f"<tr>\n" \
                     f"<td style=vertical-align:top; rowspan={len(animals)}>{col_adj}</td>\n" \
                     f"<td style=vertical-align:top;>{animals[0]['name']}</td>\n" \
                     f"<td>{build_img_tag(animals[0]['image_path'])}</td>\n" \
                     f"</tr>\n"

            for animal in animals[1:]:
                table += f"<tr>\n" \
                         f"<td style=vertical-align:top;>{animal['name']}</td>\n" \
                         f"<td>{build_img_tag(animal['image_path'])}</td>\n" \
                         f"</tr>\n"

        table += "</table>\n</body>\n</html>"

        self.write_file("index.html", "w", table)


    def parse_wiki_page_content(self, url: str) -> dict:
        """
        Main method to parse the page content. If we got tables:
        1. Parse Generic terms table
        2. Parse Terms by species or taxon table
        """

        if tables := self.parse_page_tables(url):
            logger.debug("Got from the %s page %s", url, len(tables))

            collateral_adjectives = self.parse_generic_terms_column(self.parse_table_rows(tables[0]))
            logger.debug("Got collateral adjectives %s from Generic Terms table", collateral_adjectives)

            return self.parse_terms_by_species_table(self.parse_table_rows(tables[1]), collateral_adjectives)


if __name__ == "__main__":
    wiki_animal_parser = WikiAnimalParser()
    print(wiki_animal_parser())
