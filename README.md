
![Logo UdeA](UdeA+simplificado-01.png)

# 🩺 Microcurriculum UdeA con IA

Bienvenido al proyecto **Microcurriculum UdeA con IA**. Esta aplicación utiliza inteligencia artificial para ayudar en la creación y mejora de microcurrículos para cursos de pregrado y posgrado en la Universidad de Antioquia.

## 🚀 Descripción

Este proyecto es una herramienta interactiva desarrollada con Streamlit que permite a los docentes:

- **Crear** microcurrículos completos ingresando información relevante sobre el curso.
- **Mejorar** secciones específicas del microcurrículo utilizando inteligencia artificial y fragmentos del PEI-UdeA.
- **Descargar** el microcurrículo generado en formato Word (`.docx`).

La aplicación utiliza modelos de lenguaje avanzados y bases de datos vectoriales para proporcionar sugerencias y mejoras en las diferentes secciones del microcurrículo.

## 🛠️ Tecnologías Utilizadas

- **Python**
- **Streamlit**: para la interfaz web.
- **LangChain**: para el manejo de modelos de lenguaje y embeddings.
- **ChromaDB**: como base de datos vectorial.
- **Groq**: para interactuar con modelos de lenguaje avanzados.
- **Python-docx**: para la generación de documentos Word.

## 📦 Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/microcurriculum-udea.git
   cd microcurriculum-udea
   ```

2. **Crear un entorno virtual e instalar dependencias:**

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configurar la clave API de Groq**

   Necesitarás una clave API de Groq para poder utilizar el modelo de IA. Puedes obtenerla registrándote en la plataforma de Groq.

   Agrega la clave API a tu archivo `secrets.toml` de Streamlit de la siguiente manera:

   ```toml
   [API]
   API_KEY = "tu_clave_api_de_groq"
   ```

4. **Ejecutar la aplicación:**

   ```bash
   streamlit run app.py
   ```

## ✨ Características

- **IA para Mejora Automática**: Utiliza la tecnología de inteligencia artificial de Groq para mejorar secciones del microcurrículo basadas en el PEI de la universidad.
- **Facilidad de Uso**: La interfaz de usuario simple e intuitiva está diseñada para que cualquier docente pueda usarla sin complicaciones técnicas.
- **Personalización Completa**: Ajusta y mejora el microcurrículo con facilidad, y descarga el resultado final.

## 📊 Estructura del Proyecto

- `app.py`: La aplicación principal de Streamlit.
- `create_vector_db.py`: Script para crear bases de datos vectoriales a partir de PDFs (PEI y guía).
- `requirements.txt`: Archivo con las dependencias necesarias para ejecutar la aplicación.
- `README.md`: Archivo de descripción del proyecto.

## ✍️ Autor

Este trabajo experimental ha sido desarrollado por:

**Alejandro Hernández-Arango, MD, MSc**  
Trabajo experimental para el diplomado de pedagogía, Universidad de Antioquia, 2024-2.  
Correo: [alejandro.hernandeza@udea.edu.co](mailto:alejandro.hernandeza@udea.edu.co)

## 🌐 Contacto y Redes
Alejandro Hernández-Arango MD Esp MSc
Internal Medicine, Digital Health and Telemedicine 
Professor and Researcher in Artificial Intelligence
University of Antioquia
Medellín, Colombia.
Google Scholar | Research Gate 


- **ResearchGate**: [Alejandro Hernández-Arango en ResearchGate](https://www.researchgate.net/profile/Alejandro-Hernandez-Arango)
- **Google Scholar**: [Alejandro Hernández-Arango en Google Scholar](https://scholar.google.com.pr/citations?user=IeUO9c8AAAAJ&hl=es&oi=ao)







