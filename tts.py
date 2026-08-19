import os
import wave
from google import genai
from google.genai import types

# کلید API خود را دقیقاً به جای عبارت زیر داخل کوتیشن قرار دهید
os.environ["GEMINI_API_KEY"] = "api key"

client = genai.Client()

# بقیه کدهای درخواست...
prompt_text = "سلام! این یک تست با هوش مصنوعی جمینای است."

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
