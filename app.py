# Main module
# Imports
import time
import streamlit as st
from src.config import load_environment, FAV_ICON_URL
from src.llm.pipeline import brochure_pipeline, out_of_scope_response
from src.assets.ping_sound import play_ping_sound
from warnings import filterwarnings
filterwarnings("ignore")

def main():
    # Page configuration
    st.set_page_config(page_title="Brochure Creator AI App", page_icon=FAV_ICON_URL, layout="centered")

    # Load the API key
    api_key = load_environment()
    if not api_key:
        st.error("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
    elif not api_key.startswith("sk-proj-"):
        st.error("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
    elif api_key.strip() != api_key:
        st.error("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
    else:
        st.success("API key found and looks good so far!")

    st.title("Brochure Creator AI App")
    st.write("Welcome to the Brochure Creator App! Enter a URL below to get a brochure.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter website URL..."):
        # Play the ping sound (Messenger style)
        play_ping_sound()

        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            try:
                # Check if the input looks like a URL
                if prompt.strip().startswith("http://") or prompt.strip().startswith("https://"):
                    full_response = brochure_pipeline(prompt)
                else:
                    full_response = out_of_scope_response(prompt) + "\n\n(Note: For website summaries, please enter a valid URL starting with http:// or https://)"

                # Check if the response is a string
                if isinstance(full_response, str):
                    # Function to yield the string word by word to simulate streaming
                    def stream_string(text):
                        for word in text.split(" "):
                            yield word + " "
                            time.sleep(0.04)
                    full_response = st.write_stream(stream_string(full_response))
                else:
                    full_response = st.write_stream(full_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()