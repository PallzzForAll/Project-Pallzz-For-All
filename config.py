
---

## 📄 FILE 1: `config.py` (Konfigurasi)

Simpan kode ini sebagai `config.py`:

```python
# config.py
# Ganti BOT_TOKEN dengan token dari @BotFather
BOT_TOKEN = "8815600729:AAFFlObLTLVVsywfTNrl8KrP1poOvUVxPEw"

# Daftar layanan OTP (endpoint API)
SERVICES = {
    "bca": "https://api.bca.co.id/otp/send",
    "mandiri": "https://api.mandiri.co.id/otp",
    "tokopedia": "https://api.tokopedia.com/v1/otp",
    "shopee": "https://api.shopee.com/otp",
    "gopay": "https://api.gojek.com/otp",
    "dana": "https://api.dana.id/otp",
    "ovo": "https://api.ovo.id/otp",
    "bni": "https://api.bni.co.id/otp",
    "bri": "https://api.bri.co.id/otp",
    "btpn": "https://api.btpn.com/otp",
    "linkaja": "https://api.linkaja.com/otp",
    "kredivo": "https://api.kredivo.com/otp",
    "akulaku": "https://api.akulaku.com/otp",
    "payfazz": "https://api.payfazz.com/otp"
}