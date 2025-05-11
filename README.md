# Finance Assistant Chat Application

A modern web-based chat application that uses Google's Gemini AI to provide financial advice and information. The application features a beautiful UI built with Flask, HTML, CSS, and JavaScript.

## Features

- Interactive chat interface
- Real-time responses from Gemini AI
- Modern and responsive design
- Conversation history management
- Error handling and user feedback

## Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/finance-assistant.git
cd finance-assistant
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install flask google-generativeai
```

4. Set up your environment variables:
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Windows Command Prompt
set GEMINI_API_KEY=your-api-key-here

# Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
finance-assistant/
├── app.py              # Flask application
├── static/
│   ├── css/
│   │   └── style.css   # Styles
│   └── js/
│       └── script.js   # Frontend logic
├── templates/
│   └── index.html      # Main page template
├── .gitignore
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Flask for the web framework
- All contributors who have helped with the project 