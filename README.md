# ai-chatbot-with-nlp
 AI Chatbot (Streamlit + NLTK)
 
This is a simple AI Chatbot built with NLTK and a modern Streamlit interface, styled with a dark theme.

It uses pattern–response pairs to answer basic user queries and maintains chat history in the browser session.

 1. Install Requirements

Make sure you have Python 3.8+ installed, then run:


    pip install streamlit nltk

 2. NLTK Setup
    
  Download the required tokenizer data for NLTK:

    import nltk

    nltk.download('punkt')

 3. Run the Chatbot
Save the script as ai_chatbot.py and run:

        streamlit run ai_chatbot.py
 Your default browser will open with the chatbot interface.

Usage
Type your message in the chat input at the bottom and press Enter.

The chatbot responds based on pre‑defined regex patterns.

Click 🔄 Reset Chat anytime to clear the conversation.
