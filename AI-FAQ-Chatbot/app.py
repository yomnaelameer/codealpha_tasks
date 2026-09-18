import streamlit as st
from chatbot import get_answer

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. Custom CSS (Clean & Sleek Dark Theme)
# ==========================================
st.markdown("""
<style>
    /* Clean Global Fonts & Palette */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }

    /* Modern Background & Container */
    .stApp {
        background-color: #0D1117;
        color: #E6EDF3;
    }
    
    .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }

    /* Hero Header */
    .hero-header {
        text-align: center;
        padding: 1.5rem 0 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid #21262D;
    }
    .hero-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #F0F6FC;
        letter-spacing: -0.02em;
        margin-bottom: 0.3rem;
    }
    .hero-subtitle {
        font-size: 0.9rem;
        color: #8B949E;
        font-weight: 400;
    }

    /* Prompt Cards Section */
    .suggestion-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #8B949E;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.8rem;
    }

    /* Quick Buttons Styling */
    div.stButton > button {
        width: 100%;
        background-color: #161B22;
        color: #C9D1D9;
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 0.65rem 1rem;
        font-size: 0.88rem;
        font-weight: 500;
        text-align: left;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #21262D;
        color: #58A6FF;
        border-color: #58A6FF;
        transform: translateY(-1px);
    }

    /* Chat Input Bar */
    .stChatInput > div {
        border-radius: 14px !important;
        border: 1px solid #30363D !important;
        background-color: #161B22 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .stChatInput textarea {
        color: #F0F6FC !important;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. Sidebar (Control & Info Center)
# ==========================================
with st.sidebar:
    st.title("🤖 AI Support")
    st.caption("E-Commerce Assistant")
    
    st.divider()
    
    st.markdown("### 📌 About")
    st.write(
        "Welcome! I can assist you with your orders, shipping, refunds, "
        "and payment queries using smart NLP retrieval."
    )
    
    st.divider()
    
    # Reset Chat Option
    if st.button("🔄 Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("Powered by TF-IDF & Cosine Similarity")


# ==========================================
# 4. Main Hero Header
# ==========================================
st.markdown("""
<div class="hero-header">
    <div class="hero-title">Customer FAQ Support</div>
    <div class="hero-subtitle">Instant answers to your questions about orders, payments & shipping</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 5. Session State Initialization
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# 6. Quick Suggestion Prompts (Empty State)
# ==========================================
selected_suggestion = None

if len(st.session_state.messages) == 0:
    st.markdown('<div class="suggestion-title">Frequently Asked Questions</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚚 How do I track my order?", key="sug_1"):
            selected_suggestion = "How do I track my order?"
        if st.button("💳 What payment methods are accepted?", key="sug_2"):
            selected_suggestion = "What payment methods are accepted?"

    with col2:
        if st.button("🔄 What is your return & refund policy?", key="sug_3"):
            selected_suggestion = "What is your return & refund policy?"
        if st.button("⏱️ How long does shipping usually take?", key="sug_4"):
            selected_suggestion = "How long does shipping usually take?"


# ==========================================
# 7. Render Chat History (Native Streamlit UI)
# ==========================================
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# ==========================================
# 8. User Input Handling & Chat Logic
# ==========================================
user_input = st.chat_input("Ask a question about your order, shipping, or returns...")

# Use either typed input or clicked prompt suggestion
final_query = user_input or selected_suggestion

if final_query:
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": final_query})
    with st.chat_message("user", avatar="👤"):
        st.markdown(final_query)

    # Generate & Append Bot Answer
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Searching for answers..."):
            answer = get_answer(final_query)
            st.markdown(answer)
            
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Rerun only if a prompt button was clicked to refresh state
    if selected_suggestion:
        st.rerun()