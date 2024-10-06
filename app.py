import streamlit as st
import ollama

# Function to interact with the Ollama API
def chat_with_ollama(system_prompt, user_prompt):
    try:
        response = ollama.chat(
            model="llama3.2:1b",
            messages=[
                {"role": "system", "content": system_prompt},  # System prompt
                {"role": "user", "content": user_prompt}       # User query
            ],
            options={"temperature": 0.5, "max_length": 100}
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App UI
def main():
    st.set_page_config(page_title="Chat with Ollama", page_icon="🤖", layout="wide")
    
    st.title("Chat with Ollama (llama3.2:1b) with a System Prompt")
    
    # Input fields for system and user prompts
    system_prompt = st.text_input("Enter a system prompt (e.g., 'You are a helpful assistant')", 
                                  placeholder="You are a helpful assistant.")
    user_query = st.text_input("Enter your query:", placeholder="Ask something...")
    
    if user_query and system_prompt:
        st.write("Thinking...")
        # Get response from Ollama
        response = chat_with_ollama(system_prompt, user_query)
        st.write(response)

if __name__ == "__main__":
    main()
