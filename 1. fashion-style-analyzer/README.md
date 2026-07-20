# Fashion Style Analyzer

AI-powered fashion analysis tool that identifies clothing items, analyzes style elements, and provides detailed fashion insights using computer vision and large language models.

## Overview

Fashion Style Analyzer uses a combination of deep learning techniques to analyze fashion images:

- **Computer Vision**: ResNet50-based image encoding for feature extraction
- **Vector Similarity Search**: Cosine similarity matching against a pre-computed fashion database
- **AI-Powered Analysis**: IBM Watsonx AI with Llama 4 Vision for detailed fashion descriptions
- **Interactive UI**: Gradio-based web interface for easy image upload and analysis

Upload a fashion image and get detailed information about garments, fabrics, colors, styling, and similar items from the database.

## Technology Stack

- **Python 3.8+**
- **PyTorch** - Deep learning framework for image processing
- **TorchVision** - Pre-trained ResNet50 model for feature extraction
- **Gradio** - Web UI framework for the interactive interface
- **IBM Watsonx AI** - LLM service for fashion analysis (Llama 4 Vision)
- **Pandas & NumPy** - Data manipulation and numerical operations
- **scikit-learn** - Cosine similarity calculations
- **Pillow** - Image loading and processing

## Features

- Upload fashion images for instant analysis
- Computer vision-based similarity matching
- Detailed AI-generated fashion descriptions
- Item identification with pricing and links
- Example images included for testing
- Real-time processing feedback

## Prerequisites

- Python 3.8 or higher
- IBM Watsonx AI API access (for LLM integration)
- GPU recommended but not required (CPU fallback available)

## Installation

### 1. Clone or Download

```bash
# If cloning from repository
git clone <repository-url>
cd style-finder

# Or extract if downloaded as archive
tar -xf style-finder.tar
cd <extracted-directory>
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
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

Create a `.env` file in the project root:

```bash
# IBM Watsonx AI Configuration
WATSONX_API_KEY=your_api_key_here
PROJECT_ID=your_project_id_here
REGION=us-south

# Optional: Adjust model parameters in config.py
```

**Note**: If using IBM Skills Network lab environment, the default `PROJECT_ID` is already set to `"skills-network"`.

## Usage

### Running the Application

```bash
python app.py
```

The application will:
1. Load the fashion dataset (`swift-style-embeddings.pkl`)
2. Initialize the ResNet50 model for image processing
3. Connect to IBM Watsonx AI service
4. Launch the Gradio interface on `http://127.0.0.1:5000`

A public shareable link will also be generated (if `share=True` in app.py).

### Using the Interface

1. **Upload an Image**: Click on the upload area or drag and drop a fashion image
2. **Try Examples**: Click example buttons to load pre-configured test images
3. **Analyze**: Click "Analyze Style" to process the image
4. **View Results**: See detailed fashion analysis, item details, and similar products

### Example Usage

Three example images are provided in the `examples/` directory:
- `test-1.png`
- `test-2.png`
- `test-3.png`

Click the corresponding buttons in the UI to load and test these images.

## Project Structure

```
.
├── app.py                          # Main application entry point
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── swift-style-embeddings.pkl      # Pre-computed fashion embeddings dataset
├── models/
│   ├── image_processor.py          # Image encoding and similarity matching
│   └── llm_service.py              # IBM Watsonx AI integration
├── utils/
│   └── helpers.py                  # Utility functions
└── examples/
    ├── test-1.png
    ├── test-2.png
    └── test-3.png
```

## Configuration

### Model Settings (`config.py`)

```python
# LLM Model
LLAMA_MODEL_ID = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"

# IBM Watsonx AI
PROJECT_ID = "skills-network"
REGION = "us-south"

# Image Processing
IMAGE_SIZE = (224, 224)
NORMALIZATION_MEAN = [0.485, 0.456, 0.406]
NORMALIZATION_STD = [0.229, 0.224, 0.225]

# Matching Threshold
SIMILARITY_THRESHOLD = 0.8
```

### Server Configuration

Modify `app.py` launch settings:

```python
demo.launch(
    server_name="127.0.0.1",  # Change to "0.0.0.0" for network access
    server_port=5000,          # Change port if needed
    share=True                 # Set to False to disable public link
)
```

## How It Works

1. **Image Upload**: User uploads a fashion image through the Gradio interface
2. **Feature Extraction**: Image is processed by ResNet50 to generate a 1000-dimensional feature vector
3. **Similarity Matching**: Feature vector is compared against the pre-computed dataset using cosine similarity
4. **Item Retrieval**: Closest matching outfit and all associated items are retrieved
5. **AI Analysis**: Image and matched items are sent to Llama 4 Vision for detailed fashion analysis
6. **Results Display**: Comprehensive analysis with item details, pricing, and links is displayed

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**API Key Errors**
```bash
# Verify .env file exists and contains valid credentials
cat .env

# Check config.py has correct PROJECT_ID and REGION
```

**Dataset Not Found**
```bash
# Ensure swift-style-embeddings.pkl is in the project root
ls -la swift-style-embeddings.pkl
```

**Port Already in Use**
```bash
# Change port in app.py or kill existing process
lsof -ti:5000 | xargs kill -9
```

## Performance Considerations

- **CPU vs GPU**: Application automatically detects and uses GPU if available
- **Model Loading**: Initial startup takes 10-30 seconds to load ResNet50
- **Analysis Time**: Each image analysis takes 5-15 seconds depending on hardware
- **Memory**: Requires approximately 2-4 GB RAM

## Dataset

The application uses `swift-style-embeddings.pkl`, a pre-computed dataset containing:
- Fashion outfit images
- Pre-encoded ResNet50 feature vectors
- Item metadata (names, prices, links)
- Brand and styling information

## Dependencies

Core packages:
- `torch==2.5.1` - PyTorch deep learning framework
- `torchvision==0.20.1` - Pre-trained models and transforms
- `gradio==5.22.0` - Web UI framework
- `ibm-watsonx-ai==1.1.20` - IBM Watsonx AI SDK
- `transformers==4.46.3` - Hugging Face transformers
- `pillow==11.0.0` - Image processing
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn==1.5.2` - Machine learning utilities

See `requirements.txt` for complete list.

## License

This project is provided as-is for educational and research purposes.

## Author

Developed by Anas Ziad (anasziad2015@gmail.com)

## Acknowledgments

- IBM Watsonx AI for LLM capabilities
- PyTorch and TorchVision for deep learning infrastructure
- Gradio for the interactive UI framework
- Meta for the Llama 4 Vision model
