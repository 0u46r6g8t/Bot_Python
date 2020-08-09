from config import WhatsappBot

bot = WhatsappBot()

nameFromGroup = input('Digite o nome do contato que deseja enviar msg: ')
msg = input("Mensagem: ")

bot.SendMessage(nameFromGroup, msg)