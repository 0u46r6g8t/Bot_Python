from conf import WhatsappBot

bot = WhatsappBot()

print("""

	Para que possa ativar o bot é preciso ativar o QRcode na tela principal

	Responda com:

		- y or Y, para 'Sim';
		- n or N, para 'Não';

	""")

QRcode = input("O QRcode foi ativado? ")

if QRcode == "y" or QRcode == "Y":
	while 1:
		try:
			bot.webServer()
		except KeyboardInterrupt:
			print("Obrigado por utilizar o bot feito em python")
			break
		except:
			bot.listening()
