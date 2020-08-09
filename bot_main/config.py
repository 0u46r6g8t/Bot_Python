from selenium import webdriver
import time
import platform

class WhatsappBot():

	def setSystem(self):
		system = platform.system()
		if system == 'Windows':
			self.drive = webdriver.Chrome(executable_path="./windows/chromedriver.exe") 
		if system == 'Linux':
			self.drive = webdriver.Chrome(executable_path="./chromedriver")

	def __init__(self):

		options = webdriver.ChromeOptions()
		options.add_argument("lang=pt-br")
		self.setSystem()


	def SendMessage(self, name, msg):
		# <span dir="auto" title="Arthur UTF" class="_3ko75 _5h6Y_ _3Whw5">Arthur UTF</span>
		# <div tabindex="-1" class="_3uMse"><div tabindex="-1" class="_2FVVk _2UL8j"><div class="_2FbwG" style="visibility: visible;">Digite uma mensagem</div><div class="_3FRCZ copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div></div></div>
		# <span data-testid="send" data-icon="send" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>

		try:
			self.drive.get("https://web.whatsapp.com")
			time.sleep(40)
			
			group = self.drive.find_element_by_xpath(f"//span[@title='{name}']")

			time.sleep(4)

			group.click()

			checkbox = self.drive.find_element_by_class_name('_3uMse')
			time.sleep(4)
			
			checkbox.click()

			checkbox.send_keys(msg)
			buttonSend = self.drive.find_element_by_xpath('//span[@data-icon="send"]')

			time.sleep(4)
			buttonSend.click()
		except Exception as e:
			return('Error: {}'.format(e))
		except KeyboardInterrupt:
			return("Tchau")