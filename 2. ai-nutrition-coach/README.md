# AI Nutrition Coach

AI-powered nutrition assistant that analyzes photos of food and returns a detailed calorie and nutrient breakdown using a vision-language model.

## Overview

AI Nutrition Coach lets a user upload a photo of a meal along with a question (e.g. "How many calories are in this food?"), then uses Groq (vision-capable LLM) to:

- Identify each food item in the image
- Estimate portion size and calories per item
- Total the calories for the meal
- Break down key nutrients (protein, carbohydrates, fats, vitamins, minerals)
- Give a short health evaluation of the meal

## Technology Stack

- **Python 3.9+**
- **Flask** - Web application framework
- **Groq** - LLM service for image analysis (vision-capable model)
- **python-dotenv** - Environment variable management

## Features

- Upload a food image and ask a free-form question about it
- AI-generated calorie and nutrient breakdown, formatted as structured HTML
- Live image preview before submitting
- Loading indicator while the model responds
- Flash messages for missing image/input errors

## Prerequisites

- Python 3.9 or higher
- Groq API access (free tier available at [console.groq.com](https://console.groq.com))

## Installation

### 1. Clone or Download

```bash
git clone <repository-url>
cd "2. ai-nutrition-coach"
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

This project shares a single `.env` file with the rest of the portfolio, located in the repo root (one level up from this folder, i.e. `../.env`). Copy the template and fill in your key:

```bash
cp ../.env.example ../.env
```

```
GROQ_API_KEY=your_api_key_here
FLASK_SECRET_KEY=change-me
DEBUG=false
```

Get a free API key at [console.groq.com](https://console.groq.com).

## Usage

### Running the Application

```bash
python app.py
```

The application will:
1. Connect to the Groq API
2. Launch the Flask server on `http://127.0.0.1:5000`

### Using the Interface

1. **Ask a question**: Type a question about the meal (defaults to "How many calories are in this food?")
2. **Upload an image**: Choose a photo of the food
3. **Submit**: Click "Tell me the total calories"
4. **View results**: See the identification, calorie estimate, nutrient breakdown, and health evaluation

## Project Structure

```
.
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── templates/
│   └── index.html       # Main page template
└── static/
    └── style.css         # Page styling
```

## How It Works

1. **Image Upload**: User uploads a food image and a question through the Flask form
2. **Encoding**: Image is base64-encoded and combined with the question and a nutritionist system prompt
3. **AI Analysis**: The payload is sent to a vision-capable model on Groq
4. **Formatting**: The model's response is converted from markdown-style text to HTML
5. **Results Display**: The formatted breakdown is rendered back on the page alongside the uploaded image

## Troubleshooting

**Import Errors**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**API Key Errors**
```bash
# Verify .env exists and contains valid credentials
cat .env
```

**Port Already in Use**
```bash
lsof -ti:5000 | xargs kill -9
```

## License

This project is provided as-is for educational and research purposes.

## Author

Developed by Anas AlGhannam

## Acknowledgments

- Groq for LLM inference
- Flask for the web framework
