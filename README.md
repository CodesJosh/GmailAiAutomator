# Gmail AI Automator 🤖📧

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-AI-orange.svg?style=for-the-badge\&logo=google-gemini\&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

# 🇪🇸 Descripción

**Gmail AI Automator** es una herramienta de automatización avanzada que integra la **API de Google Gemini** con el protocolo **IMAP** para gestionar bandejas de entrada de forma inteligente.

Este proyecto automatiza la lectura de correos y la generación de respuestas, permitiendo reducir el tiempo dedicado a la gestión manual del email.

---

## 🚀 Descripción del Sistema

El bot realiza automáticamente las siguientes tareas:

* Detecta **correos no leídos** en la bandeja de entrada
* Filtra remitentes automáticos o spam mediante **listas negras de palabras clave**
* Analiza el contenido del correo usando **modelos de lenguaje (LLM)**
* Genera una **respuesta profesional y coherente**
* Guarda la respuesta automáticamente en la carpeta de **Borradores (Drafts)**

De esta forma el usuario puede **revisar y aprobar la respuesta antes de enviarla**.

---

## 🛠️ Tech Stack

* **Lenguaje:** Python 3.9+
* **IA:** Google Generative AI (`gemini-1.5-flash` por defecto)
* **Protocolos:** IMAP (acceso y gestión de correo)
* **Procesamiento de texto:** BeautifulSoup4 + Regex
* **Gestión de configuración:** `python-dotenv`

---

## 📋 Prerrequisitos

* **Python 3.9+**

* **Google App Password**
  Necesaria si tienes activada la verificación en dos pasos (2FA)

  https://myaccount.google.com/apppasswords

* **Gemini API Key**

  https://aistudio.google.com/

---

## 🔧 Instalación y Uso

### 1. Clonar el repositorio

```bash id="s1kq82"
git clone https://github.com/CodesJosh/GmailAiAutomator.git
cd GmailAiAutomator
```

### 2. Instalar dependencias

```bash id="s9d2la"
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` basado en el archivo de ejemplo.

```bash id="shf83k"
cp .env.example .env
```

Edita `.env` con tus credenciales.

---

### 4. Ejecutar el bot

```bash id="akl28s"
python bot_gmail.py
```

---

## 📂 Estructura del Proyecto

```id="sn3j8f"
.
├── bot_gmail.py       # Lógica principal del bot
├── test_modelos.py    # Script de diagnóstico para validar Gemini API
├── requirements.txt   # Dependencias del proyecto
├── .env.example       # Plantilla de configuración
└── .gitignore         # Protección de archivos sensibles
```

---

## 🔐 Variables de Entorno (.env)

```id="3h2a8f"
EMAIL_USER=tu-usuario@gmail.com
EMAIL_PASS=tu-contraseña-de-aplicacion
API_KEY=tu-gemini-api-key
```

---

## 👤 Autor

Desarrollado por **CodesJosh**

---

# 🇺🇸 English Version

## Gmail AI Automator 🤖📧

**Gmail AI Automator** is a software engineering solution designed to optimize email workflows by combining **Google Gemini AI** with **IMAP automation**.

The system reads incoming emails, filters automated messages, and generates professional reply drafts using large language models.

Instead of sending emails automatically, responses are saved into the **Drafts folder**, allowing the user to review and approve them before sending.

---

## 🚀 System Overview

The bot performs the following steps:

* Scans **unread emails**
* Filters automated senders and newsletters
* Analyzes email content using **LLMs**
* Generates a **context-aware professional reply**
* Saves the result into the **Drafts folder**

---

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **AI Engine:** Google Generative AI (`gemini-1.5-flash`)
* **Protocols:** IMAP for secure mailbox access
* **Parsing:** BeautifulSoup4 for HTML cleanup
* **Environment Management:** `python-dotenv`

---

## 📋 Prerequisites

* **Python 3.9+**
* **Google App Password**

https://myaccount.google.com/apppasswords

* **Gemini API Key**

https://aistudio.google.com/

---

## 🔧 Installation & Usage

### 1. Clone the repository

```bash id="82kdla"
git clone https://github.com/CodesJosh/GmailAiAutomator.git
cd GmailAiAutomator
```

### 2. Install dependencies

```bash id="sd28a1"
pip install -r requirements.txt
```

### 3. Environment configuration

```bash id="sk1a0d"
cp .env.example .env
```

Edit the `.env` file with your credentials.

---

### 4. Run the application

```bash id="sdf82l"
python bot_gmail.py
```

---

## 📂 Project Structure

```id="skf93k"
.
├── bot_gmail.py
├── test_modelos.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 👤 Author

Developed by **CodesJosh**
