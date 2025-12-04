# Groq API Examples

> High-performance AI applications powered by Groq's ultra-fast inference API

A curated collection of production-ready applications demonstrating the power of Groq's low-latency LLM inference. Built with Python and Streamlit for rapid development and deployment.

## Features

- **Ultra-low latency** chat interactions powered by Groq's inference engine
- **Multi-format file analysis** supporting PDF, DOCX, TXT, LOG, JSON, and YAML
- **Streamlit-based UI** for intuitive user experiences
- **Production-ready** code structure with environment variable management

## Projects

### Chat-App
Interactive conversational AI assistant with real-time response generation. Perfect for building chatbots, virtual assistants, or Q&A systems.

**Key Features:**
- Real-time chat interface
- Powered by Groq's GPT-OSS-20B model
- Clean, responsive UI

### File-Analyzer
Intelligent document analysis tool that processes multiple file formats and extracts insights using natural language queries.

**Key Features:**
- Multi-format support (PDF, DOCX, TXT, LOG, JSON, YAML)
- Custom query-based analysis
- Context-aware responses

## Tech Stack

- **Python 3.11+**
- **Groq API** - Ultra-fast LLM inference
- **Streamlit** - Web application framework


## Quick Start

### Prerequisites
- Python 3.11 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Groqapi-Examples.git
cd Groqapi-Examples

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "GROQ_API_KEY=your_api_key_here" > .env
```

### Running Applications

**Chat-App:**
```bash
cd Chat-App
streamlit run main.py
```

**File-Analyzer:**
```bash
cd File-Analyzer
streamlit run app.py
```

## Configuration

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## License

See [LICENSE](LICENSE) file for details.
