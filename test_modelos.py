import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Obtener la API Key desde el entorno
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Error: No se encontró GEMINI_API_KEY en el archivo .env")
else:
    genai.configure(api_key=API_KEY)
    print("🔎 Buscando modelos disponibles para tu cuenta...")
    
    try:
        modelos = genai.list_models()
        for m in modelos:
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Disponible: {m.name}")
    except Exception as e:
        print(f"❌ Error conectando: {e}")
