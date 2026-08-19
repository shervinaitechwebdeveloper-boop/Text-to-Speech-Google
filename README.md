# 🤖 Gemini TTS with Python

یک پروژه ساده و کاربردی برای تبدیل **متن به صوت (Text-to-Speech)** با استفاده از **Google Gemini API** و مدل `gemini-2.5-flash-preview-tts`.

در این پروژه، یک متن فارسی به Gemini ارسال می‌شود و صدای تولیدشده با Voice `Kore` به صورت فایل `WAV` ذخیره می‌شود.

---

## ✨ امکانات

- 🤖 استفاده از Google Gemini
- 🗣️ تبدیل متن به صدا (Text-to-Speech)
- 🇮🇷 پشتیبانی از متن فارسی
- 🎙️ استفاده از Voice `Kore`
- 🔊 دریافت خروجی صوتی با فرمت WAV
- 🐍 پیاده‌سازی با Python
- 💾 ذخیره خروجی به صورت `gemini_output.wav`

---

## 📦 نصب کتابخانه

ابتدا کتابخانه موردنیاز را نصب کنید:

```bash
pip install google-genai
```

---

## 🔑 دریافت Gemini API Key

برای اجرای پروژه به **Gemini API Key** نیاز دارید.

کلید API خود را از **Google AI Studio** دریافت کنید.

بعد از دریافت API Key، آن را در قسمت زیر کد قرار دهید:

```python
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"
```

مثلاً:

```python
os.environ["GEMINI_API_KEY"] = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXX"
```

> ⚠️ **توجه امنیتی بسیار مهم:**  
> API Key واقعی خود را مستقیماً در GitHub، ویدیو، README یا شبکه‌های اجتماعی منتشر نکنید.

بهتر است API Key را با **Environment Variable** یا فایل تنظیمات محلی که داخل `.gitignore` قرار دارد مدیریت کنید.

---

## 🚀 اجرای پروژه

فایل Python را مثلاً با نام زیر ذخیره کنید:

```text
gemini_tts.py
```

سپس اجرا کنید:

```bash
python gemini_tts.py
```

در صورت اجرای موفق، فایل زیر ساخته می‌شود:

```text
gemini_output.wav
```

---

## 🧠 نحوه عملکرد

```text
📝 متن فارسی
      ↓
🤖 Gemini API
      ↓
🗣️ Text-to-Speech
      ↓
🎙️ Voice: Kore
      ↓
🔊 PCM Audio
      ↓
💾 gemini_output.wav
```

---

## 💻 کد کامل

```python
import os
import wave
from google import genai
from google.genai import types


# 🔑 Gemini API Key خود را اینجا قرار دهید
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"

client = genai.Client()


# متنی که می‌خواهیم به صدا تبدیل شود
prompt_text = "سلام! این یک تست با هوش مصنوعی جمینای است."


# ارسال درخواست به Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=prompt_text,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Kore"
                )
            )
        ),
    ),
)


# دریافت فایل صوتی
for part in response.candidates[0].content.parts:

    if part.inline_data and part.inline_data.mime_type.startswith("audio/"):

        pcm_data = part.inline_data.data

        with wave.open("gemini_output.wav", "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(pcm_data)

        print("فایل صوتی با موفقیت ذخیره شد!")

        break
```

---

## 🎙️ تغییر متن

برای تغییر متن، مقدار `prompt_text` را تغییر دهید:

```python
prompt_text = "سلام دوستان! به کانال من خوش آمدید."
```

می‌توانید متن فارسی دلخواه خود را قرار دهید تا Gemini آن را به صوت تبدیل کند.

---

## 📁 ساختار پروژه

بعد از اجرای برنامه، ساختار پروژه به شکل زیر خواهد بود:

```text
project/
│
├── gemini_tts.py
└── gemini_output.wav
```

فایل `gemini_output.wav` خروجی صوتی تولیدشده توسط Gemini است.

---

## ⚠️ رفع خطاهای رایج

### خطای `ModuleNotFoundError: No module named 'google'`

اگر با خطای زیر مواجه شدید:

```text
ModuleNotFoundError: No module named 'google'
```

دستور زیر را اجرا کنید:

```bash
pip install google-genai
```

---

### مشکل API Key

اگر درخواست به Gemini ارسال نمی‌شود، موارد زیر را بررسی کنید:

- API Key را به درستی وارد کرده باشید.
- API Key فعال باشد.
- اتصال اینترنت برقرار باشد.
- سرویس Gemini API برای حساب شما در دسترس باشد.

---

## 🔐 امنیت API Key

**هیچ‌وقت API Key واقعی را در GitHub قرار ندهید.**

برای مثال، این کار را انجام ندهید:

```python
os.environ["GEMINI_API_KEY"] = "AIzaSyYourRealApiKey"
```

بهتر است از متغیر محیطی استفاده کنید.

در ویندوز PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

و سپس در Python:

```python
import os

api_key = os.environ["GEMINI_API_KEY"]
```

همچنین اگر فایل `.env` ایجاد می‌کنید، آن را در `.gitignore` قرار دهید.

---

## 🎯 کاربردهای پروژه

این پروژه می‌تواند پایه‌ای برای ساخت پروژه‌های بزرگ‌تر باشد، مانند:

- 🤖 دستیار هوش مصنوعی
- 🗣️ دستیار صوتی
- 🎙️ JARVIS
- 📚 تبدیل متن آموزشی به صوت
- 🎬 تولید Voice برای ویدیو
- 📖 کتاب صوتی
- 📰 خواندن اخبار با هوش مصنوعی
- 📧 خواندن ایمیل‌ها به صورت صوتی
- 🚀 پروژه‌های AI و Automation

---

## 👨‍💻 سازنده

ساخته شده توسط **شروین موسوی**

### 🎥 YouTube

**Shervin AI Tech**


[کانال YouTube Shervin AI Tech](https://www.youtube.com/@ShervinAITech?utm_source=chatgpt.com)

---

## ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود:

⭐ به پروژه Star بدهید  
📢 پروژه را با دوستان خود به اشتراک بگذارید  
🎥 کانال **Shervin AI Tech** را دنبال کنید

---

## 📄 License

این پروژه برای اهداف آموزشی و توسعه‌ای ارائه شده است.
