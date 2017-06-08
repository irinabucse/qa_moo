import unittest
from selenium import webdriver

class HomePage(unittest.TestCase):
    _base_url = "https://www.moo.com/uk/"
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(self):
        self.driver.maximize_window()

    def setUp(self):
        self.driver.get(self._base_url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_welcome(self):
        self.assertTrue(self.driver.find_element_by_tag_name("h1").text == "Welcome to MOO")

    def test_subtitle(self):
        self.assertTrue(self.driver.find_element_by_class_name("intro").text == "Premium Business Cards, Luxe Business Cards, Postcards, Stickers and more.")

    def test_shop_button(self):
        btn = self.driver.find_element_by_class_name("slideshow-content").find_element_by_link_text("Shop now >")
        #store `href` attribute in `link` variable
        link = btn.get_attribute("href")
        btn.click()
        # compare the new page url with stored one
        self.assertEqual(link, self.driver.current_url)

    def test_business_cards_link(self):
        business = self.driver.find_element_by_class_name("intro").find_element_by_link_text("Business Cards")
        link = business.get_attribute("href")
        business.click()
        self.assertEqual(link, self.driver.current_url)

    def test_luxe_business_cards(self):
        self.driver.find_element_by_class_name("intro").find_element_by_link_text("Luxe Business Cards").click()
        self.assertEqual("https://www.moo.com/uk/products/luxe/business-cards.html", self.driver.current_url)

    def test_postcards(self):
        self.driver.find_element_by_class_name("intro").find_element_by_link_text("Postcards").click()
        self.assertEqual("https://www.moo.com/uk/products/postcards.html", self.driver.current_url)

    def test_stickers(self):
        self.driver.find_element_by_class_name("intro").find_element_by_link_text("Stickers").click()
        self.assertEqual("https://www.moo.com/uk/products/stickers-range.html", self.driver.current_url)



    def test_business_cards(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("Business Cards").click()
        self.assertEqual("https://www.moo.com/uk/products/business-cards.html", self.driver.current_url)

    def test_postcards_link(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("Postcards").click()
        self.assertEqual("https://www.moo.com/uk/products/postcards.html", self.driver.current_url)

    def test_taillored_collection_link(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("Tailored Collection").click()
        self.assertEqual("https://www.moo.com/uk/products/tailored/business-cards.html", self.driver.current_url)

    def test_nfc(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("NFC Business Cards+").click()
        self.assertEqual("https://www.moo.com/uk/products/nfc/business-cards-plus.html", self.driver.current_url)

    def test_luxe_business(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("Luxe Business Cards").click()
        self.assertEqual("https://www.moo.com/uk/products/luxe/business-cards.html", self.driver.current_url)

    def test_stickers_link(self):
        self.driver.find_element_by_class_name("slideshow-nav").find_element_by_link_text("Stickers").click()
        self.assertEqual("https://www.moo.com/uk/products/stickers-range.html", self.driver.current_url)

    def test_next_day_business(self):
        self.driver.find_element_by_class_name("")
