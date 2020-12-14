from selenium import webdriver 
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
		
		self.fail('Finish the test!')
		#she is invited to enter a to-do item right away

		#she types "Buy peacock feathers" into a text box (her hobby is tying fly-fishing lures)

		#When she hits enter, the page updates, and now the page lists 1: Buy peacock feathers

		#There is still a text box inviting her to add another item, she enters "Use peacock feathers to make a fly"

		#The page update again with both items on the list

		#She wonders whetherthe site will remember her list, she sees it generates a unique URL for her and there is some explanatory text

		#She visits the URL and her to-do list is still there

		#Satisfied, Sam goes to sleep
if __name__ == '__main__':
	unittest.main(warnings='ignore')
