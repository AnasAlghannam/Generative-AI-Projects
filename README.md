# Generative AI Projects Portfolio

Collection of AI/ML projects focusing on computer vision, LLMs, and generative AI applications.

**Author**: Anas AlGhannam
**GitHub**: [@AnasAlghannam](https://github.com/AnasAlghannam)

---

## Projects Overview

| Project | Description | Tech Stack | Status |
|---------|-------------|------------|--------|
| [Fashion Style Analyzer](#1-fashion-style-analyzer) | Fashion analysis using CV + LLM | PyTorch, IBM Watsonx (Llama 4 Vision), Gradio | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| [AI Nutrition Coach](#2-ai-nutrition-coach) | Food image calorie & nutrient analysis using an LLM | Flask, IBM Watsonx (Llama 4 Maverick) | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |

---

## Projects

### 1. Fashion Style Analyzer
> AI-powered fashion analysis tool

**Repository**: [1. fashion-style-analyzer/](./1.%20fashion-style-analyzer/)

**Description**: Analyzes fashion images using computer vision and an LLM to identify clothing items, styles, and provide detailed fashion insights. Uses ResNet50-based feature extraction with cosine similarity search against a pre-computed fashion database, then IBM Watsonx AI (Llama 4 Vision) for AI-generated descriptions.

**Key Features**:
- ResNet50-based image feature extraction
- Vector similarity search (cosine similarity)
- IBM Watsonx AI (Llama 4 Vision) integration
- Interactive Gradio web interface
- Real-time fashion analysis

**Tech Stack**: Python, PyTorch, TorchVision, Gradio, IBM Watsonx AI, Pandas, scikit-learn

[View Code](./1.%20fashion-style-analyzer/) | [Documentation](./1.%20fashion-style-analyzer/README.md)

---

### 2. AI Nutrition Coach
> AI-powered food image nutrition analyzer

**Repository**: [2. ai-nutrition-coach/](./2.%20ai-nutrition-coach/)

**Description**: Upload a photo of a meal and ask a question about it (e.g. "How many calories are in this food?"). Uses IBM Watsonx AI (Llama 4 Maverick) to identify each food item, estimate portion size and calories, total the calories, break down key nutrients, and give a short health evaluation.

**Key Features**:
- Food identification and calorie estimation from a single photo
- Full nutrient breakdown (protein, carbohydrates, fats, vitamins, minerals)
- IBM Watsonx AI (Llama 4 Maverick) integration
- Flask-based web interface with live image preview

**Tech Stack**: Python, Flask, IBM Watsonx AI, python-dotenv

[View Code](./2.%20ai-nutrition-coach/) | [Documentation](./2.%20ai-nutrition-coach/README.md)

---

## Adding a New Project

1. Create a new numbered subdirectory, e.g. `2. project-name/`
2. Add the project's full code and its own `README.md`
3. Update this README: add a row to the Projects Overview table and a detailed project card
4. Commit and push:
   ```bash
   git add .
   git commit -m "Add [project-name]: [brief description]"
   git push
   ```
