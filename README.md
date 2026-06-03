# 🤖 ChatBot con IA - Ollama (Llama 3.1)

## Asistente Virtual Personalizable con Inteligencia Artificial Local

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-Framework-green" />
  <img src="https://img.shields.io/badge/Ollama-Llama_3.1-black?logo=meta" />
  <img src="https://img.shields.io/badge/100%25-Local-orange" />
</p>

---

## 📋 Descripción

Chatbot conversacional que corre **100% en local** usando el modelo Llama 3.1 a través de Ollama. Construido con Streamlit como interfaz web y LangChain para el manejo de prompts e historial de conversación.

El asistente es completamente personalizable: puedes definir su nombre, su rol y su comportamiento desde la propia interfaz, lo que lo hace adaptable a distintos contextos como soporte al cliente, asistencia educativa o consultas internas.

---

## ✨ Características

- **Ejecución 100% local** — No requiere API keys ni conexión a servicios externos. Tus datos nunca salen de tu máquina.
- **Personalizable en tiempo real** — Cambia el nombre y la descripción del asistente directamente desde la interfaz sin modificar código.
- **Historial de conversación** — El bot mantiene el contexto de la conversación usando `ChatPromptTemplate` y `MessagesPlaceholder` de LangChain.
- **Interfaz web simple** — Streamlit proporciona una UI limpia y funcional accesible desde el navegador.

---

## 🛠️ Stack Tecnológico

| Tecnología | Propósito |
|---|---|
| **Python 3.x** | Lenguaje base |
| **Streamlit** | Interfaz web interactiva |
| **LangChain** | Gestión de prompts, historial y cadenas de procesamiento |
| **Ollama** | Servidor local para ejecutar modelos LLM |
| **Llama 3.1** | Modelo de lenguaje (Meta) ejecutado localmente |

---

## 🚀 Instalación y Configuración

### 1. Instalar Ollama

Descarga e instala Ollama desde [ollama.com](https://ollama.com/download) según tu sistema operativo.

Luego descarga el modelo Llama 3.1:

```bash
ollama pull llama3.1:latest
```

Verifica que esté corriendo:

```bash
ollama list
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/Mateo-Rua/ChatBot-con-IA---Ollama-3.1.git
cd ChatBot-con-IA---Ollama-3.1
```

### 3. Instalar dependencias

```bash
pip install streamlit langchain langchain-core langchain-ollama
```

### 4. Ejecutar la aplicación

```bash
streamlit run ChatBot_LLama.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 💻 Uso

1. **Nombre del asistente** — Escribe el nombre que quieras darle al bot (por defecto: "Bot").
2. **Descripción del asistente** — Define el rol y comportamiento. Por ejemplo:
   - `"Eres un asistente experto en Python que responde de forma concisa"`
   - `"Eres un tutor de matemáticas para estudiantes de secundaria"`
   - `"Eres un agente de soporte técnico de una empresa de telecomunicaciones"`
3. **Escribe tu pregunta** y haz clic en **Enviar**.
4. El historial de la conversación se muestra en el área de chat inferior.
5. Escribe `adios` para finalizar la sesión.

---

## 📂 Estructura del Proyecto

```
ChatBot-con-IA---Ollama-3.1/
│
├── ChatBot_LLama.py        # Código principal de la aplicación
└── README.md                # Documentación del proyecto
```

---

## 🔧 ¿Cómo funciona?

El flujo de la aplicación sigue esta secuencia:

1. **Inicialización** — Se instancia el modelo Llama 3.1 a través de `OllamaLLM` de LangChain.
2. **Configuración del prompt** — Se crea un `ChatPromptTemplate` con tres componentes: el mensaje del sistema (rol del bot), el historial de conversación (`MessagesPlaceholder`) y la entrada del usuario.
3. **Cadena de procesamiento** — La plantilla se combina con el modelo (`prompt_template | llm`) creando una cadena que procesa cada mensaje con el contexto completo.
4. **Gestión del historial** — Cada mensaje (humano y bot) se almacena en `st.session_state` como objetos `HumanMessage` y `AIMessage`, permitiendo que el modelo mantenga coherencia entre turnos.

---

## 🔮 Mejoras Futuras

- Agregar soporte para múltiples modelos (Mistral, Gemma, CodeLlama) seleccionables desde la interfaz.
- Implementar streaming de respuestas para una experiencia más fluida.
- Agregar opción para exportar el historial de conversación.
- Incluir soporte para carga de documentos (RAG) para que el bot responda basándose en archivos del usuario.

---

## 👤 Autor

**Mateo Rua**

[![GitHub](https://img.shields.io/badge/GitHub-Mateo--Rua-181717?logo=github)](https://github.com/Mateo-Rua)

---

> *Chatbot conversacional con IA ejecutado localmente usando Ollama y Llama 3.1, personalizable para cualquier contexto de asistencia.*
