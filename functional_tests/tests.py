from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Sam has heard about a cool new online to-do app, she goes to check out the browser homepage
		self.browser.get(self.live_server_url)

		#Sam notices the page title and header mentioning to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		#she is invited to enter a to-do item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		#she types "Buy peacock feathers" into a text box (her hobby is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, the page updates, and now the page lists 1: Buy peacock feathers
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		#There is still a text box inviting her to add another item, she enters "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		#The page update again with both items on the list
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		#She wonders whetherthe site will remember her list, she sees it generates a unique URL for her and there is some explanatory text
		self.fail('Finish the test!')
		#She visits the URL and her to-do list is still there

		#Satisfied, Sam goes to sleep

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
