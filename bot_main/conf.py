from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WhatsappBot():

	def __init__(self):
		self.drive = webdriver.Chrome(executable_path="./chromedriver")
		self.drive.get("https://web.whatsapp.com")

	global list_command

	list_command = {
		"help": "Bot funcionado com sucesso! Por favor espere um momento que já já responderei...",
		"Man": "Dae jovem!",
		"exit":"Obrigado por utilizar o bot."
	}

	def webServer(self):
		
		for command in list_command:

			time.sleep(20)
			try:
				group = self.drive.find_element(By.XPATH, '//span[text()="\{}"]'.format(command))
				time.sleep(5)
				print(" [ + ] Achou o elemento \{}!".format(command))
				group.click()

				checkbox = self.drive.find_element_by_class_name('_3uMse')

				time.sleep(5)
				print(" [ + ] Clicando no elemento!")
				checkbox.click()
				
				checkbox.send_keys("{}".format(list_command[command]))

				buttonSend = self.drive.find_element_by_xpath('//span[@data-icon="send"]')
				
				print(" [ + ] Enviando Mensagem!")
				buttonSend.click()
				time.sleep(20)
				self.drive.get("https://web.whatsapp.com")
			except:
				self.drive.get("https://web.whatsapp.com")
				pass

	def listening(self):

		self.drive.get("https://web.whatsapp.com")
		
		time.sleep(5)
