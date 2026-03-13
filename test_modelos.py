import google.generativeai as genai

# PON TU API KEY AQUI
API_KEY = "AIzaSyDMPk2xZRMnxhe4VSv5mTVcDLzle3SWgNA"
genai.configure(api_key=API_KEY)

print("🔎 Buscando modelos disponibles para tu cuenta...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Disponible: {m.name}")
except Exception as e:
    print(f"❌ Error conectando: {e}")