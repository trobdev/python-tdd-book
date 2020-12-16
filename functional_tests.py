from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Sam has heard about a cool new online to-do app, she goes to check out the browser homepage
		self.browser.get('http://localhost:8000')

		#Sam notices the page title and header mentioning to-do lists
		self.assertIn('To-Do', self.browser.title)
		# header_text = self.browser.find_element_by_tag_name('h1').text
		# self.assertIn('To-Do', header_text)
		
		#she is invited to enter a to-do item right away
		# inputbox = self.browser.find_element_by_id('id_new_item')
		# self.assertEqual(
		# 	inputbox.get_attribute('placeholder'),
		# 	'Enter a to-do item'
		# )
		#she types "Buy peacock feathers" into a text box (her hobby is tying fly-fishing lures)
		# inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, the page updates, and now the page lists 1: Buy peacock feathers
		# inputbox.send_keys(Keys.ENTER)
		# time.sleep(1)
		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_eleements_by_tag_name('tr')
		# self.assertTrue(
		# 	any(row.text == '1: Buy peacock feathers' for row in rows)
		# )
		#There is still a text box inviting her to add another item, she enters "Use peacock feathers to make a fly"
		self.fail('Finish the test!')
		#The page update again with both items on the list

		#She wonders whetherthe site will remember her list, she sees it generates a unique URL for her and there is some explanatory text

		#She visits the URL and her to-do list is still there

		#Satisfied, Sam goes to sleep
if __name__ == '__main__':
	unittest.main(warnings='ignore')
