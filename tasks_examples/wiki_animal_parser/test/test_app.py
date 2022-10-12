import unittest
from unittest.mock import Mock
from tasks_examples.wiki_animal_parser.app import WikiAnimalParser
from bs4 import BeautifulSoup


class wiki_animal_parser_TestCase(unittest.TestCase):

    def setUp(self):
        """
        setUp TestCase.
        """

        self.wiki_animal_parser = WikiAnimalParser()


    def test_clean_animal_name(self):
        expected_result = 'Cattle'
        text = 'Cattle[c] (list)'
        result = self.wiki_animal_parser.clean_animal_name(text)

        self.assertEqual(expected_result, result)


    def test_generate_html_page(self):
        expected_result = '<html>\n<body>\n<table style=font-size:20px;font-weight: bold;>\n<tr>\n<td ' \
                          'style=vertical-align:top; rowspan=2>musteline</td>\n<td ' \
                          'style=vertical-align:top;>Badger</td>\n<td><img width=200 ' \
                          'src=tmp/Badger.jpg></td>\n</tr>\n<tr>\n<td style=vertical-align:top;>Ferret</td>\n<td><img ' \
                          'width=200 src=tmp/Ferret.png></td>\n</tr>\n</table>\n</body>\n</html>'

        table_data = {
            'musteline': [{'name': 'Badger', 'image_path': 'tmp/Badger.jpg'},
                          {'name': 'Ferret', 'image_path': 'tmp/Ferret.png'}],
        }

        self.wiki_animal_parser.write_file = Mock()
        self.wiki_animal_parser.generate_html_page(table_data)
        self.wiki_animal_parser.write_file.assert_called_once_with("index.html", "w", expected_result)


    def test_parse_terms_by_species_table(self):
        expected_result = {'musteline': [{'image_path': 'tmp/Badger.jpg', 'name': 'Badger'}]}

        collateral_adjectives = ['musteline']
        html = '''<table><tbody><tr><th colspan="7"><span class="anchor" id="B"></span><b>B</b></th></tr>, <tr><td><a 
        href="/wiki/Baboon" title="Baboon">Baboon</a></td><td>infant</td><td>babuina<sup class="reference" 
        id="cite_ref-18"><a href="#cite_note-18">[18]</a></sup></td><td class="unknown table-unknown" 
        style="background: #EEE; font-size: smaller; vertical-align: middle; text-align: 
        center;">?</td><td>flange<sup class="reference" id="cite_ref-askoxford-b_19-0"><a 
        href="#cite_note-askoxford-b-19">[19]</a></sup><sup class="reference" id="cite_ref-20"><a 
        href="#cite_note-20">[a]</a></sup><br/>troop, group<sup class="reference" id="cite_ref-oxfordfaq_2-2"><a 
        href="#cite_note-oxfordfaq-2">[2]</a></sup><sup class="reference" id="cite_ref-sdzoo_11-5"><a 
        href="#cite_note-sdzoo-11">[11]</a></sup><sup class="reference" id="cite_ref-askoxford-b_19-1"><a 
        href="#cite_note-askoxford-b-19">[19]</a></sup></td><td class="unknown table-unknown" style="background: 
        #EEE; font-size: smaller; vertical-align: middle; text-align: center;">?</td><td></td></tr>, <tr><td><a 
        href="/wiki/Badger" title="Badger">Badger</a></td><td>cub<br/>kit</td><td>sow</td><td>boar</td><td >cete<sup 
        class="reference" id="cite_ref-oxfordfaq_2-3"><a href="#cite_note-oxfordfaq-2">[2]</a></sup><sup 
        class="reference" id="cite_ref-sdzoo_11-6"><a href="#cite_note-sdzoo-11">[11]</a></sup><sup class="reference" 
        id="cite_ref-usgs_14-2"><a href="#cite_note-usgs-14">[14]</a></sup><sup class="reference" 
        id="cite_ref-askoxford-b_19-2"><a href="#cite_note-askoxford-b-19">[19]</a></sup><br/>colony<sup 
        class="reference" id="cite_ref-askoxford-b_19-3"><a href="#cite_note-askoxford-b-19">[ 
        19]</a></sup></td><td>musteline</td><td></td></tr></tbody></table> '''

        table = BeautifulSoup(html, 'html.parser')
        table_rows = table.find('tbody').find_all('tr')

        self.wiki_animal_parser.parse_animal_image = Mock(return_value='tmp/Badger.jpg')
        result = self.wiki_animal_parser.parse_terms_by_species_table(table_rows, collateral_adjectives)
        self.assertEqual(expected_result, result)


    def test_parse_generic_terms_column(self):
        expected_result = ['viverrine', 'procyonine', 'nasuine', 'others', 'porcine', 'piscine', 'ichthyic', 'musteline']

        html = '''<table><tbody> <tr> <td><a href="/wiki/Viverridae" title="Viverridae">Viverridae</a></td> <td>cub, 
        kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, committee</td> <td>viverrine</td> <td><a 
        href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans </td></tr><tr> <td><a 
        href="/wiki/Procyonidae" title="Procyonidae">Procyonidae</a></td> <td>cub, kit</td> <td>sow</td> 
        <td>boar</td> <td>gaze, smack, committee</td> <td>procyonine, nasuine, others</td> <td><a 
        href="/wiki/Raccoon" title="Raccoon">Raccoon</a> family of Carnivorans </td></tr><tr> <td><a 
        href="/wiki/Suidae" title="Suidae">Suidae</a></td> <td>piglet</td> <td>sow</td> <td>boar</td> <td>drift or 
        drove</td> <td>porcine</td> <td>pig </td></tr><tr> <td><a href="/wiki/Osteichthyes" 
        title="Osteichthyes">Osteichthyes</a></td> <td>fry, fingerling</td> <td style="background: #EEE; font-size: 
        smaller; vertical-align: middle; text-align: center;" class="unknown table-unknown">?</td> <td 
        style="background: #EEE; font-size: smaller; vertical-align: middle; text-align: center;" class="unknown 
        table-unknown">?</td> <td><a href="/wiki/Shoaling_and_schooling" title="Shoaling and schooling">school, 
        shoal</a></td> <td>piscine, ichthyic</td> <td><a href="/wiki/Bony_fish" class="mw-redirect" title="Bony 
        fish">bony fish</a> </td></tr><tr> <td><a href="/wiki/Mustelidae" title="Mustelidae">Mustelidae</a></td> 
        <td>kit</td> <td>sow (large) or jill (small)</td> <td>boar (large) or hob,<sup id="cite_ref-7" 
        class="reference"><a href="#cite_note-7">[7]</a></sup> jack (small)</td> <td>colony (large) or business (
        small)</td> <td>musteline</td> <td><a href="/wiki/Ferret" title="Ferret">Ferret</a> family of Carnivorans (
        large: badgers &amp; wolverines; small: weasels &amp; ferrets) </td></tr></tbody></table> '''

        table = BeautifulSoup(html, 'html.parser')
        table_rows = table.find('tbody').find_all('tr')

        result = self.wiki_animal_parser.parse_generic_terms_column(table_rows)
        self.assertEqual(expected_result, result)


    def test_parse_animal_image(self):
        expected_result = 'tmp/Taurotragus.jpg'

        html = '''<tbody><tr> <th colspan="2" style="text-align: center; background-color: rgb(235,235,210)">Eland 
        </th></tr> <tr> <td colspan="2" style="text-align: center"><a href="/wiki/File:Taurotragus_oryx_(
        captive).jpg" class="image"><img alt="Taurotragus oryx (captive).jpg" 
        src="//upload.wikimedia.org/wikipedia/commons/thumb/6/68/Taurotragus_oryx_%28captive%29.jpg/220px
        -Taurotragus_oryx_%28captive%29.jpg" decoding="async" width="220" height="165" 
        srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/68/Taurotragus_oryx_%28captive%29.jpg/330px
        -Taurotragus_oryx_%28captive%29.jpg 1.5x, 
        //upload.wikimedia.org/wikipedia/commons/thumb/6/68/Taurotragus_oryx_%28captive%29.jpg/440px
        -Taurotragus_oryx_%28captive%29.jpg 2x" data-file-width="640" data-file-height="480"></a> </td></tr> <tr> <td 
        colspan="2" style="text-align: center; font-size: 88%"><i><a href="/wiki/Common_eland" title="Common 
        eland">Taurotragus oryx</a></i> </td></tr> </tbody> '''

        self.wiki_animal_parser.write_file = Mock()
        self.wiki_animal_parser.BeautifulSoup = Mock(return_value=BeautifulSoup(html, 'html.parser'))
        result = self.wiki_animal_parser.parse_animal_image('/wiki/Taurotragus')

        self.assertEqual(expected_result, result)


    def test_parse_table_rows(self):
        expexted_result = '[<tr> <td><a href="/wiki/Viverridae" title="Viverridae">Viverridae</a></td> <td>cub, ' \
                          '\n        kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, committee</td> ' \
                          '<td>viverrine</td> <td><a href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans ' \
                          '</td></tr>]'
        html = '''<table><tbody> <tr> <td><a href="/wiki/Viverridae" title="Viverridae">Viverridae</a></td> <td>cub, 
        kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, committee</td> <td>viverrine</td> <td><a 
        href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans </td></tr></tbody></table> '''

        table = BeautifulSoup(html, 'html.parser')
        result = self.wiki_animal_parser.parse_table_rows(table)

        self.assertEqual(expexted_result, str(result))


    def test_parse_page_tables(self):
        expected_result = 2
        html = '''<table class=wikitable><tbody> <tr> <td><a href="/wiki/Viverridae" 
        title="Viverridae">Viverridae</a></td> <td>cub, kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, 
        committee</td> <td>viverrine</td> <td><a href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans 
        </td></tr></tbody></table> <table class=notwikitable><tbody> <tr> <td><a href="/wiki/Viverridae" 
        title="Viverridae">Viverridae</a></td> <td>cub, kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, 
        committee</td> <td>viverrine</td> <td><a href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans 
        </td></tr></tbody></table> <table class=wikitable><tbody> <tr> <td><a href="/wiki/Viverridae" 
        title="Viverridae">Viverridae</a></td> <td>cub, kit</td> <td>sow</td> <td>boar</td> <td>gaze, smack, 
        committee</td> <td>viverrine</td> <td><a href="/wiki/Civet" title="Civet">Civet</a> family of Carnivorans 
        </td></tr></tbody></table> '''

        self.wiki_animal_parser.get_wiki_page_content = Mock(return_value=html)
        result = self.wiki_animal_parser.parse_page_tables('https://en.wikipedia.org/wiki/List_of_animal_names')
        self.assertEqual(expected_result, len(result))
