import unittest
from city_functions import get_formatted_name

class Test_cities(unittest.TestCase):

    def test_city_country(self):
        formattedName = get_formatted_name("santiago", "chile")
        self.assertEqual(formattedName, "Santiago, Chile")

    def test_city_country_population(self):
        formattedName = get_formatted_name("santiago", "chile", 500000)
        self.assertEqual(formattedName, "Santiago, Chile - population 500000")
        
unittest.main()