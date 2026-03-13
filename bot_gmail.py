import imaplib
import email
from email.header import decode_header
from email.message import EmailMessage
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup 

# --- 1. CARGA DE CONFIGURACIÓN SEGURA ---
load_dotenv()

# Estas variables se leerán de tu archivo .env local
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS") 
API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar la IA
if API_KEY:
    genai.configure(api_key=API_KEY)
    # Nota: He cambiado a 'gemini-1.5-flash' que es la versión estable actual
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    print("❌ Error: GEMINI_API_KEY no encontrada en el archivo .env")

# --- 2. CONFIGURACIÓN DE FILTROS ---
PALABRAS_IGNORADAS = [
    "no-reply", "noreply", "donotreply", 
    "linkedin", "newsletter", "notificaciones", 
    "banco", "info@", "alert", "security", "google"
]

def limpiar_texto(texto):
    if not texto: return ""
    return texto.strip()

def generar_respuesta_ia(cuerpo_del_correo):
    if not cuerpo_del_correo or len(cuerpo_del_correo) < 10:
        return "El correo era demasiado corto o solo contenía imágenes."

    print("🤖 Consultando a la IA...")
    prompt = f"""
    Actúa como mi asistente personal. He recibido este correo:
    "{cuerpo_del_correo[:2000]}"
    
    Escribe una respuesta amable, profesional y concisa (máximo 3 párrafos).
    Solo el cuerpo del mensaje.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ ERROR REAL DE LA IA: {e}") 
        return f"Error generando respuesta."

def crear_borrador(destinatario, asunto_original, respuesta_ia):
    print(f"📝 Intentando guardar borrador para: {destinatario}")
    
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_USER, EMAIL_PASS)
        
        msg = EmailMessage()
        msg["From"] = EMAIL_USER
        msg["To"] = destinatario
        msg["Subject"] = f"Re: {asunto_original}"
        msg.set_content(respuesta_ia)
        
        mensaje_bytes = msg.as_bytes()
        fecha_actual = imaplib.Time2Internaldate(time.time())

        # Intentar diferentes nombres de carpetas según el idioma de la cuenta
        carpetas_a_probar = ["[Gmail]/Borradores", "[Gmail]/Drafts", "Drafts", "Borradores"]
        
        guardado = False
        for carpeta in carpetas_a_probar:
            try:
                mail.append(carpeta, None, fecha_actual, mensaje_bytes)
                print(f"✅ ¡Éxito! Guardado en: '{carpeta}'")
                guardado = True
                break
            except:
                continue
                
        if not guardado:
            print("❌ No se pudo encontrar la carpeta de Borradores.")
            
        mail.logout()
    except Exception as e:
        print(f"❌ Error al conectar para crear borrador: {e}")

def obtener_cuerpo_mensaje(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
                except: pass
    else:
        try:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        except: pass
    return body

def revisar_correo():
    print("🔍 Conectando a Gmail...")
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")
        
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        
        if not email_ids:
            print("📭 No hay correos nuevos.")
            return

        print(f"📬 Procesando el último correo recibido...")
        ultimo_id = email_ids[-1] 
        
        _, msg_data = mail.fetch(ultimo_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Decodificar asunto
                subject_raw = msg["Subject"]
                subject = "Sin Asunto"
                if subject_raw:
                    decoded_list = decode_header(subject_raw)
                    subject_fragment, encoding = decoded_list[0]
                    if isinstance(subject_fragment, bytes):
                        subject = subject_fragment.decode(encoding if encoding else "utf-8", errors="ignore")
                    else:
                        subject = subject_fragment
                
                sender = msg.get("From")
                if any(palabra in sender.lower() for palabra in PALABRAS_IGNORADAS):
                    print(f"🚫 IGNORADO: {sender}")
                    continue

                body = obtener_cuerpo_mensaje(msg)
                print(f"📩 Procesando: {sender}\nAsunto: {subject}")
                
                respuesta = generar_respuesta_ia(body)
                crear_borrador(sender, subject, respuesta)

        mail.logout()
    except Exception as e:
        print(f"❌ Error en la revisión: {e}")

if __name__ == "__main__":
    revisar_correo()