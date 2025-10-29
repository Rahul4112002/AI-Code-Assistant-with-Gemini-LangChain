# 🤖 AI Code Assistant with Gemini & LangChain

A powerful AI-powered code assistant built with **Streamlit**, **LangChain**, and **Google Gemini AI**. Features 9 specialized modes for code generation, debugging, optimization, and documentation, supporting multiple file formats with an interactive chat interface.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

### 🎯 **9 Specialized AI Modes**
- **General** - Full-stack developer assistant for any coding tasks
- **Code Analysis** - Expert code analyst to break down and explain code
- **Code Generator** - Generate high-quality, production-ready code
- **Debugger** - Find issues, explain them, and suggest fixes
- **Code Guide** - Mentor for teaching coding best practices
- **Optimization** - Performance engineer to optimize code
- **Explain Code** - Teacher to explain code in simple terms
- **Project Builder** - Build entire projects end-to-end
- **Documentation** - Generate professional documentation

### 📂 **Multi-File Support**
Upload and analyze multiple files simultaneously:
- **Code Files**: Python, JavaScript, TypeScript, Java, C++, C, Go, Ruby, PHP, C#
- **Web Files**: HTML, CSS, JSON
- **Documents**: PDF, DOCX, TXT, Markdown

### 💬 **Interactive Chat Interface**
- Real-time conversation with AI assistant
- Persistent chat history
- Context-aware responses
- File analysis on demand

### 🔍 **Smart File Analysis**
- Automatic text extraction from various formats
- Support for code and documentation files
- PDF and DOCX document parsing with LangChain loaders

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- Google API Key (Gemini AI)
- pip or uv package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rahul4112002/AI-Code-Assistant-with-Gemini-LangChain.git
cd AI-Code-Assistant-with-Gemini-LangChain
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**
The app will automatically open at `http://localhost:8501`

---

## 📖 Usage Guide

### 1. **Select AI Mode**
Choose from 9 specialized modes in the sidebar based on your task:
- Need to debug? Select **Debugger**
- Want to generate code? Select **Code Generator**
- Need explanations? Select **Explain Code**

### 2. **Upload Files (Optional)**
- Click on "Upload project files" in the sidebar
- Select multiple files (code, documents, PDFs)
- Click "🔍 Analyze Uploaded Files" button to get AI analysis

### 3. **Chat with AI**
- Type your question or request in the chat input
- Ask AI to:
  - Generate code snippets
  - Debug existing code
  - Explain complex concepts
  - Optimize performance
  - Review code quality
  - Create documentation

### Example Queries:
```
"Create a REST API with FastAPI for user authentication"
"Debug this Python function: [paste code]"
"Explain how async/await works in JavaScript"
"Optimize this SQL query for better performance"
"Generate unit tests for this class"
```

---

## 🏗️ Project Structure

```
AI-Code-Assistant-with-Gemini-LangChain/
│
├── app.py                  # Main Streamlit application
├── langchain_client.py     # LangChain + Gemini AI integration
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web UI and user interaction |
| **AI Model** | Google Gemini 2.5 Flash | Language model for code assistance |
| **Framework** | LangChain | AI orchestration and prompt management |
| **Document Loaders** | langchain-community | PDF and DOCX parsing |
| **Environment** | python-dotenv | Environment variable management |

---

## 📦 Dependencies

```
streamlit              # Web application framework
langchain              # LLM orchestration framework
langchain-google-genai # Google Gemini integration
langchain-community    # Document loaders (PDF, DOCX)
python-dotenv          # Environment variable loader
pypdf                  # PDF text extraction
docx2txt              # DOCX text extraction
```

---

## 🧠 How It Works

### Architecture Overview

1. **User Interface (Streamlit)**
   - Provides interactive web interface
   - Handles file uploads and mode selection
   - Manages chat history and session state

2. **LangChain Client**
   - Initializes Gemini AI model with mode-specific prompts
   - Converts conversation history to LangChain message format
   - Manages API calls to Google Gemini

3. **Document Processing**
   - Extracts text from uploaded files
   - Uses specialized loaders for PDF and DOCX
   - Handles plain text and code files

4. **AI Processing**
   - System prompt sets AI's role based on selected mode
   - Maintains conversation context
   - Generates contextual responses

### Code Flow

```
User Input → Streamlit UI → LangChainClient → Gemini API
                ↓                                  ↓
         File Upload → Extract Text → Add to Context
                                          ↓
                              Generate Response → Display
```

---

## 🎨 Screenshots

### Main Interface
The clean, intuitive interface with sidebar controls and chat area.

### File Upload & Analysis
Upload multiple files and get instant AI-powered analysis.

### Chat Interaction
Interactive conversation with context-aware responses.

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |

### Model Settings

You can customize the AI model in `langchain_client.py`:

```python
self.model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Model version
    temperature=0.2,            # Lower = more focused
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

**Temperature Guide:**
- `0.0-0.3`: Focused, deterministic (good for code)
- `0.4-0.7`: Balanced creativity
- `0.8-1.0`: More creative, varied responses

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contribution:
- Add more AI modes (Code Reviewer, Test Generator, etc.)
- Support for more file formats
- Dark mode theme
- Export chat history
- Multi-language support
- Voice input integration

---

## 🐛 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Solution: Install all dependencies
pip install -r requirements.txt
```

**2. API Key Not Found**
```bash
# Solution: Check .env file exists and has correct format
GOOGLE_API_KEY=your_key_here
```

**3. Streamlit Port Already in Use**
```bash
# Solution: Use a different port
streamlit run app.py --server.port 8502
```

**4. File Upload Issues**
- Check file size (Streamlit has 200MB default limit)
- Verify file format is in the supported list
- Ensure proper file encoding (UTF-8 recommended)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Rahul**
- GitHub: [@Rahul4112002](https://github.com/Rahul4112002)
- Project Link: [AI-Code-Assistant-with-Gemini-LangChain](https://github.com/Rahul4112002/AI-Code-Assistant-with-Gemini-LangChain)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [LangChain](https://www.langchain.com/) - For LLM orchestration tools
- [Google Gemini](https://deepmind.google/technologies/gemini/) - For the powerful AI model
- [Python Community](https://www.python.org/community/) - For continuous support

---

## 🔮 Future Enhancements

- [ ] Add code execution sandbox
- [ ] Support for more AI models (OpenAI, Claude, etc.)
- [ ] GitHub repository integration
- [ ] Code diff and comparison features
- [ ] Real-time collaboration
- [ ] Plugin system for extensibility
- [ ] Mobile-responsive design
- [ ] API endpoint for programmatic access

---

## 📊 Version History

- **v1.0.0** (2025-10-29)
  - Initial release
  - 9 specialized AI modes
  - Multi-file upload support
  - Interactive chat interface
  - PDF and DOCX support

---

## ⭐ Show Your Support

If this project helped you, please consider giving it a ⭐ on GitHub!

---

**Made with ❤️ using Python, Streamlit, and Google Gemini AI**