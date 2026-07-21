# Generative AI Projects Portfolio

Collection of AI/ML projects focusing on computer vision, LLMs, and generative AI applications.

**Author**: Anas AlGhannam
**GitHub**: [@AnasAlghannam](https://github.com/AnasAlghannam)

---

## Shared API Key Setup

All projects in this portfolio share a single `.env` file kept in this root folder (not committed to git). Set it up once:

```bash
cp .env.example .env
```

Then fill in `GROQ_API_KEY` (free tier at [console.groq.com](https://console.groq.com)) in that one file — every project's `app.py` reads it automatically from here, so you don't need a `.env` inside each project folder.

---

## Projects Overview

| Project | Description | Tech Stack | Status |
|---------|-------------|------------|--------|
| [Fashion Style Analyzer](#1-fashion-style-analyzer) | Fashion analysis using CV + LLM | PyTorch, Groq, Gradio | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| [AI Nutrition Coach](#2-ai-nutrition-coach) | Food image calorie & nutrient analysis using an LLM | Flask, Groq | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| [NLP SQL Agent](#3-nlp-sql-agent) | Natural-language questions answered by an LLM writing & running SQL | LangChain, Groq, MySQL | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |

---

## Projects

### 1. Fashion Style Analyzer
> AI-powered fashion analysis tool

**Repository**: [1. fashion-style-analyzer/](./1.%20fashion-style-analyzer/)

**Description**: Analyzes fashion images using computer vision and an LLM to identify clothing items, styles, and provide detailed fashion insights. Uses ResNet50-based feature extraction with cosine similarity search against a pre-computed fashion database, then Groq (vision-capable LLM) for AI-generated descriptions.

**Key Features**:
- ResNet50-based image feature extraction
- Vector similarity search (cosine similarity)
- Groq LLM integration
- Interactive Gradio web interface
- Real-time fashion analysis

**Tech Stack**: Python, PyTorch, TorchVision, Gradio, Groq, Pandas, scikit-learn

[View Code](./1.%20fashion-style-analyzer/) | [Documentation](./1.%20fashion-style-analyzer/README.md)

---

### 2. AI Nutrition Coach
> AI-powered food image nutrition analyzer

**Repository**: [2. ai-nutrition-coach/](./2.%20ai-nutrition-coach/)

**Description**: Upload a photo of a meal and ask a question about it (e.g. "How many calories are in this food?"). Uses Groq (vision-capable LLM) to identify each food item, estimate portion size and calories, total the calories, break down key nutrients, and give a short health evaluation.

**Key Features**:
- Food identification and calorie estimation from a single photo
- Full nutrient breakdown (protein, carbohydrates, fats, vitamins, minerals)
- Groq LLM integration
- Flask-based web interface with live image preview

**Tech Stack**: Python, Flask, Groq, python-dotenv

[View Code](./2.%20ai-nutrition-coach/) | [Documentation](./2.%20ai-nutrition-coach/README.md)

---

### 3. NLP SQL Agent
> Natural-language-to-SQL agent for MySQL

**Repository**: [3. nlp-sql-agent/](./3.%20nlp-sql-agent/)

**Description**: Ask a plain-English question about a MySQL database (e.g. "Which genre has the most tracks?") and get back an answer. A LangChain SQL agent backed by Groq inspects the schema, writes and validates a SQL query, executes it, and explains the result. Ships with the Chinook sample database for out-of-the-box testing.

**Key Features**:
- Natural-language question answering over any MySQL schema
- Agent reasoning trace (tables inspected, SQL drafted, query validated and run)
- Groq LLM integration
- Bundled Chinook sample database

**Tech Stack**: Python, LangChain, langchain-groq, Groq, MySQL, python-dotenv

[View Code](./3.%20nlp-sql-agent/) | [Documentation](./3.%20nlp-sql-agent/README.md)

---

## Adding a New Project

For any project that needs an LLM API key, default to [Groq](https://console.groq.com) (free tier) rather than a paid provider.

1. Create a new numbered subdirectory, e.g. `3. project-name/`
2. Add the project's full code and its own `README.md`
3. Update this README: add a row to the Projects Overview table and a detailed project card
4. Commit and push:
   ```bash
   git add .
   git commit -m "Add [project-name]: [brief description]"
   git push
   ```
