import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage  # Importa clases para manejar mensajes de humano y bot.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Estas son las herramientas para definir plantillas de prompts y manejar historial.
from langchain_ollama import OllamaLLM  # Importa el modelo Ollama para generación de lenguaje.

# Instancia el modelo Llama 3.1 más reciente de Ollama.
llm = OllamaLLM(model="llama3.1:latest")

# # Alternativa comentada para otra inicialización del modelo.
# llm = Ollama(model="llama3.1:latest")


def main():
    # Título de la aplicación en la interfaz.
    st.title("ChatBot de servicio al cliente")
    
    # Entrada para definir el nombre del asistente virtual, con un valor por defecto.
    bot_name = st.text_input("Nombre del sasistente virtual:", value="Bot")
    
    # Esta es la plantilla para describir el propósito del bot en función del nombre proporcionado por el usuario.
    prompt = f"Eres un asistente virtual y te llamas {bot_name}"
    
    # Esta es la entrada para modificar la descripción del asistente.
    bot_description = st.text_area("Descripcion del asistente", value=prompt)

    # Inicializa el historial de conversación en el estado de la sesión si no existe.
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Define una plantilla para manejar los mensajes del sistema.
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", bot_description),  # Mensaje inicial que describe el rol del sistema/bot.
            MessagesPlaceholder(variable_name="chat_history"),  # Reservado para historial de la conversación.
            ("human", "{input}")  # Representa el lugar donde se coloca la entrada del usuario.
        ]
    )

    # Combina la plantilla con el modelo LLM seleccionado para generar una cadena de respuestas.
    chain = prompt_template | llm

    # Entrada para que el usuario escriba su mensaje.
    user_input = st.text_input("Escribe tu pregunta:", key="user_input")

    # Botón de enviar para procesar la entrada del usuario.
    if st.button("Enviar"):
        # Si el usuario escribe "adios", detiene la ejecución de la aplicación.
        if user_input.lower() == "adios":
            st.stop()
        else:
            # Genera una respuesta utilizando la cadena combinada (plantilla + modelo).
            response = chain.invoke({
                "input": user_input,  # Entrada del usuario.
                "chat_history": st.session_state["chat_history"]  # Contexto del historial.
            })

            # Agrega el mensaje del usuario al historial.
            st.session_state["chat_history"].append(HumanMessage(content=user_input))
            # Agrega la respuesta del asistente al historial.
            st.session_state["chat_history"].append(AIMessage(content=response))

    # Construye una cadena para mostrar la conversación de forma legible en la interfaz.
    chat_display = ""  

    for msg in st.session_state["chat_history"]:
        if isinstance(msg, HumanMessage):  # Si el mensaje es del usuario.
            chat_display += f"👩🏻‍💻 Humano : {msg.content}\n"
        elif isinstance(msg, AIMessage):  # Si el mensaje es del asistente virtual.
            chat_display += f"🤖 {bot_name} : {msg.content}\n"

    # Muestra el historial de la conversación en un área de texto.
    st.text_area("chat", value=chat_display, height=400, key="chat_area")



if __name__ == '__main__':
    main()
