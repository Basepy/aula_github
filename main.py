import asyncio
from telegram import Bot

# Token do seu bot Telegram
TOKEN = '6209907953:AAEpLdG7lZce5cAG9V1D82sogvhiGR38cYY' 

# Função assíncrona para enviar mensagem
async def enviar_mensagem(user_id, mensagem):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=user_id, text=mensagem)

# Função principal para rodar o envio da mensagem
def main():
    user_id = 5533806118  # Substitua pelo ID do usuário para quem deseja enviar a mensagem
    mensagem = "Olá! Esta é uma mensagem do seu bot Telegram."
    asyncio.run(enviar_mensagem(user_id, mensagem))

if __name__ == '__main__':
    main()
