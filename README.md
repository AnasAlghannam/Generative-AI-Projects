# Generative AI Projects Portfolio

Collection of AI/ML projects focusing on computer vision, LLMs, and generative AI applications.

**Author**: Anas AlGhannam
**GitHub**: [@AnasAlghannam](https://github.com/AnasAlghannam)

## Contributors

<a href="https://github.com/AnasAlghannam">
  <img src="https://github.com/AnasAlghannam.png" width="50" height="50" style="border-radius:50%" alt="Anas AlGhannam" />
</a>

[Anas AlGhannam](https://github.com/AnasAlghannam) — Creator & Maintainer

---

## Projects Overview

| Project | Description | Tech Stack | Status |
|---------|-------------|------------|--------|
| [Fashion Style Analyzer](#1-fashion-style-analyzer) | Fashion analysis using CV + LLM | PyTorch, IBM Watsonx (Llama 4 Vision), Gradio | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |

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
