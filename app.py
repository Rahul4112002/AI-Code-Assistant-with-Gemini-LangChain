# Required Libraries Import
import streamlit as st  # Web UI banane ke liye
from langchain_client import LangChainClient  # Humara custom LangChain client
import tempfile, os  # File handling aur temporary files ke liye
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader  # PDF aur DOCX files read karne ke liye

# Streamlit page configuration - Title aur layout set karna
st.set_page_config(page_title="AI Code Assistant", layout="wide")

# --- Session state initialization ---
# Session state: Page refresh hone par bhi data save rehta hai
if "messages" not in st.session_state:
    st.session_state.messages = []  # Chat history store karne ke liye
if "mode" not in st.session_state:
    st.session_state.mode = None  # Current assistant mode store karne ke liye
if "uploaded_texts" not in st.session_state:
    st.session_state.uploaded_texts = {}  # {filename: extracted_text} - Uploaded files ka content store karna

# Main heading display karna
st.title("🤖 AI Code Assistant (Gemini + LangChain + Streamlit)")

# --- Sidebar Upload Section ---
st.sidebar.header("📂 Project Files")
# File uploader - Multiple files ek saath upload kar sakte ho
uploaded_files = st.sidebar.file_uploader(
    "Upload project files",
    accept_multiple_files=True,  # Multiple files allow hai
    type=[  # Supported file types
        "py", "js", "ts", "java", "cpp", "c", "html", "css", "json",
        "go", "rb", "php", "cs", "txt", "md", "docx", "pdf"
    ]
)

# --- Sidebar Mode Selection Dropdown ---
st.sidebar.header("⚙️ Mode Selection")
# User ko different modes choose karne ka option
mode = st.sidebar.selectbox(
    "Choose assistant mode (required)",
    [  # Available modes - Har mode ka alag behavior hoga
        "General", "Code Analysis", "Code Generator", "Debugger",
        "Code Guide", "Optimization", "Explain Code",
        "Project Builder", "Documentation"
    ],
    index=0  # Default mein "General" mode selected hoga
)
st.session_state.mode = mode  # Selected mode ko session state mein save karna

# LangChain client initialize karna with selected mode
LC = LangChainClient(mode=st.session_state.mode)
# Current mode display karna user ko
st.caption(f"🟢 Assistant is running in **{mode}** mode")

# --- File Content Extractor Function (LangChain loaders ka use karke) ---
def extract_text(file):
    """
    Yeh function uploaded file se text extract karta hai
    - PDF, DOCX files ke liye special loaders use karta hai
    - Code aur text files ko directly read karta hai
    """
    # File ka extension nikalna (e.g., .pdf, .py, .docx)
    suffix = os.path.splitext(file.name)[-1].lower()
    
    # Temporary file banana disk par (kyunki loaders ko file path chahiye)
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file.read())  # Uploaded file ka content temporary file mein write karna
        tmp_path = tmp.name  # Temporary file ka path save karna

    try:
        # File type ke hisaab se appropriate loader use karna
        if suffix == ".docx":
            loader = Docx2txtLoader(tmp_path)  # Word documents ke liye
        elif suffix == ".pdf":
            loader = PyPDFLoader(tmp_path)  # PDF files ke liye
        else:
            # Plain text ya code files ke liye simple read
            with open(tmp_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        # Loader se documents load karna aur text extract karna
        docs = loader.load()
        return "\n".join([doc.page_content for doc in docs])  # Saare pages ka text combine karna
    finally:
        os.unlink(tmp_path)  # Temporary file ko delete karna (cleanup)

# --- Uploaded files ko process karna aur session mein save karna ---
if uploaded_files:
    # Har uploaded file ko loop mein process karna
    for f in uploaded_files:
        # Agar file pehle se session mein nahi hai (duplicate avoid karne ke liye)
        if f.name not in st.session_state.uploaded_texts:
            try:
                # File ka text extract karke session state mein save karna
                st.session_state.uploaded_texts[f.name] = extract_text(f)
            except Exception as e:
                # Agar error aaye toh error message save karna
                st.session_state.uploaded_texts[f.name] = f"⚠ Could not read {f.name}: {e}"
    # Sidebar mein success message show karna
    st.sidebar.success(f"{len(st.session_state.uploaded_texts)} file(s) ready for analysis.")

# --- Analyze Button - Uploaded files ko AI se analyze karvana ---
if uploaded_files:
    if st.sidebar.button("🔍 Analyze Uploaded Files"):
        # Sabhi uploaded files ka text combine karna
        # Har file ka sirf first 3000 characters lena (token limit ke liye)
        combined_texts = "\n\n".join(
            [f"📄 {name}:\n{text[:3000]}" for name, text in st.session_state.uploaded_texts.items()]
        )
        
        # AI assistant message ke format mein response show karna
        with st.chat_message("assistant"):
            # Loading spinner dikhana jab tak response nahi aata
            with st.spinner("Analyzing uploaded files..."):
                # LLM ko combined text bhejke analysis result lena
                # Existing messages + new file content bhej rahe hain
                reply = LC.chat(
                    st.session_state.messages + [{"role": "user", "content": combined_texts}]
                )
                st.markdown(reply)  # Response ko markdown format mein display karna
        
        # Analysis result ko chat history mein save karna
        st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Chat History Display ---
# Pichle saare messages ko screen par dikhana
for m in st.session_state.messages:
    # Message ka role (user ya assistant) ke hisaab se chat bubble dikhana
    with st.chat_message(m["role"]):
        st.markdown(m["content"])  # Message content ko markdown format mein show karna

# --- Chat Input Box ---
# User se input lena (walrus operator := use karke condition check + assignment ek saath)
if prompt := st.chat_input("Ask me to generate code, debug, review, or explain..."):
    # User ka message history mein save karna
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # User message ko display karna
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI assistant ka response generate karna
    with st.chat_message("assistant"):
        # "Thinking..." spinner dikhana jab tak response generate ho raha hai
        with st.spinner("Thinking..."):
            # Pura conversation history LLM ko bhejke response lena
            reply = LC.chat(st.session_state.messages)
            st.markdown(reply)  # Response display karna

    # Assistant ka response history mein save karna
    st.session_state.messages.append({"role": "assistant", "content": reply})
