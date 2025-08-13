import telebot
import requests
from io import BytesIO

bot = telebot.TeleBot("8013031612:AAFFxVA2Papk0g_nYjSnQezec2vlj7NJ4xI")

@bot.message_handler(commands=['sex'])
def send_video(message):
    try:
        response = requests.get("https://api.sumiproject.net/video/videosex")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                video_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                video_data = requests.get(video_url, headers=headers)

                if video_data.status_code == 200 and video_data.content:
                    video_file = BytesIO(video_data.content)
                    video_file.name = "video.mp4"  
                    bot.send_video(message.chat.id, video_file)
                else:
                    bot.reply_to(message, "Không thể tải video.")
            else:
                bot.reply_to(message, "Không gửi được Video")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")

bot.polling()