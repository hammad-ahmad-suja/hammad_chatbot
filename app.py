import streamlit as st
from ollama import Client

# ============================================================
# Ollama Configuration
# ============================================================

OLLAMA_HOST = "http://127.0.0.1:11434"

client = Client(host=OLLAMA_HOST)


# ============================================================
# Streamlit Page Configuration
# ============================================================

st.set_page_config(
    page_title="Ollama Local Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# Title
# ============================================================

st.title("🤖 Ollama Local Chatbot")
st.write("Chat with your local AI models using Ollama.")


# ============================================================
# Session State
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# Get Ollama Models
# ============================================================

def get_available_models():
    """
    Get installed models from the local Ollama server.
    """

    try:
        response = client.list()

        models = []

        # Current Ollama Python API
        if hasattr(response, "models"):
            for model in response.models:

                # Current API normally uses .model
                if hasattr(model, "model"):
                    models.append(model.model)

                # Fallback for older versions
                elif isinstance(model, dict):
                    if "model" in model:
                        models.append(model["model"])
                    elif "name" in model:
                        models.append(model["name"])

        return models, None

    except Exception as e:
        return [], str(e)


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("⚙️ Configuration")

    available_models, connection_error = get_available_models()

    # --------------------------------------------------------
    # Ollama Connection Status
    # --------------------------------------------------------

    if connection_error:

        st.error("❌ Ollama connection failed")

        st.write("Ollama host:")
        st.code(OLLAMA_HOST)

        st.write("Actual error:")
        st.code(connection_error)

        st.info(
            "Make sure the Ollama application/server is running."
        )

    else:

        st.success("✅ Ollama connected")

    # --------------------------------------------------------
    # Model Selection
    # --------------------------------------------------------

    if available_models:

        # Remove duplicates and sort
        available_models = sorted(set(available_models))

        # Prefer Gemma 3 4B
        default_model = "gemma3:4b"

        if default_model in available_models:
            default_index = available_models.index(default_model)
        else:
            default_index = 0

        selected_model = st.selectbox(
            "Select local model",
            available_models,
            index=default_index
        )

        st.write("Installed models:")

        for model in available_models:
            st.write(f"• {model}")

    else:

        st.warning("No models detected.")

        selected_model = st.text_input(
            "Enter model name",
            value="gemma3:4b"
        )

    # --------------------------------------------------------
    # Clear Chat
    # --------------------------------------------------------

    st.divider()

    if st.button(
        "🗑️ Clear Chat History",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# Display Previous Messages
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# Chat Input
# ============================================================

prompt = st.chat_input(
    "Ask your local AI anything..."
)


# ============================================================
# Send Message
# ============================================================

if prompt:

    # --------------------------------------------------------
    # Add user message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # --------------------------------------------------------
    # Display user message
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # --------------------------------------------------------
    # Generate AI response
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        try:

            # ------------------------------------------------
            # Send request to Ollama
            # ------------------------------------------------

            stream = client.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True
            )


            # ------------------------------------------------
            # Read streaming response
            # ------------------------------------------------

            full_response = ""

            for chunk in stream:

                content = ""

                # Current Ollama Python response
                try:
                    content = chunk.message.content
                except Exception:
                    pass

                # Fallback for dictionary response
                if not content and isinstance(chunk, dict):

                    try:
                        content = chunk["message"]["content"]
                    except Exception:
                        content = ""

                # Add text
                if content:

                    full_response += content

                    response_placeholder.markdown(
                        full_response
                    )


            # ------------------------------------------------
            # Save assistant response
            # ------------------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )


        except Exception as e:

            st.error("❌ Ollama returned an error")

            st.write("Model:")
            st.code(selected_model)

            st.write("Error details:")
            st.code(str(e))

            st.info(
                "Check that this model works with Ollama using "
                f"`ollama run {selected_model}`."
            )