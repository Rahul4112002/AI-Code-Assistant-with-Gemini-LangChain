# Required Libraries Import
import os  # Operating system operations ke liye
from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini AI model ke liye
from langchain.schema import HumanMessage, SystemMessage, AIMessage  # Chat message types
from dotenv import load_dotenv  # .env file se environment variables load karne ke liye

# .env file se environment variables load karna (GOOGLE_API_KEY)
load_dotenv()

# LangChain Client Class - Gemini AI se communicate karne ke liye
class LangChainClient:
    def __init__(self, mode="General"):
        """
        Initialize LangChain client with specific mode
        
        Args:
            mode (str): Assistant mode - determines AI ka behavior/role
        """
        
        # Different modes ke liye system prompts define karna
        # System prompt AI ko batata hai ki uska role kya hai
        role_prompts = {
            "Code Analysis": "You are an expert code analyst. Break down and explain code clearly.",
            "Code Generator": "You are a senior developer. Generate high-quality, production-ready code.",
            "Debugger": "You are a debugging assistant. Find issues, explain them, and suggest fixes.",
            "Code Guide": "You are a mentor. Teach coding best practices step by step.",
            "Optimization": "You are a performance engineer. Optimize code for speed and efficiency.",
            "Explain Code": "You are a teacher. Explain code in simple terms with examples.",
            "Project Builder": "You are a full-stack developer. Build entire projects end-to-end.",
            "Documentation": "You are a technical writer. Generate professional documentation.",
            "General": "You are a full-stack developer assistant. Help with any coding tasks."
        }

        # Selected mode ka system prompt save karna
        # Agar mode nahi mila toh "General" mode use hoga
        self.system_prompt = role_prompts.get(mode, role_prompts["General"])
        
        # Google Gemini AI model initialize karna
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",  # Model version - fast aur efficient
            temperature=0.2,  # Low temperature = More focused, deterministic responses (code ke liye better)
            google_api_key=os.getenv("GOOGLE_API_KEY")  # .env file se API key lena
        )

    def chat(self, messages):
        """
        Gemini model ko messages bhejke response lena
        
        Args:
            messages (list): Chat history - list of dicts with 'role' and 'content' keys
            
        Returns:
            str: AI model ka response text
        """
        
        # Message list banani hai LangChain format mein
        # Pehle system prompt add karna (AI ka role define karta hai)
        prompt_messages = [SystemMessage(content=self.system_prompt)]
        
        # Conversation history ko LangChain message objects mein convert karna
        for m in messages:
            if m["role"] == "user":
                # User ka message HumanMessage ban jayega
                prompt_messages.append(HumanMessage(content=m["content"]))
            else:
                # Assistant ka message AIMessage ban jayega
                prompt_messages.append(AIMessage(content=m["content"]))

        # Gemini API ko call karna with all messages
        resp = self.model.invoke(prompt_messages)
        
        # Response ka content return karna (text format mein)
        return resp.content
