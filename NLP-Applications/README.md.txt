```markdown
# Amazon Product Reviews Sentiment Analysis  
**Using spaCy + TextBlob (via spaCyTextBlob)**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![spaCy](https://img.shields.io/badge/spaCy-v3.0%2B-orange)  
![TextBlob](https://img.shields.io/badge/TextBlob-sentiment-green)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Project Overview
This repository contains a complete sentiment analysis pipeline that:
- Downloads the **Datafiniti Consumer Reviews of Amazon Products** dataset from Kaggle
- Cleans and preprocesses the review text
- Performs sentiment analysis using **TextBlob** integrated into a spaCy pipeline
- Computes semantic similarity between reviews using spaCy's medium English model (`en_core_web_md`)
- Outputs a DataFrame with polarity, subjectivity, and sentiment labels

The project is fully documented in `sentiment_analysis_report.pdf`.

## Repository Structure
```
.
├── sentiment_analysis.ipynb               # Main Jupyter notebook with full pipeline
├── sentiment_analysis_report.pdf          # Detailed 4-page project report
├── Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv   # (auto-downloaded)
├── README.md                              # This file
└── requirements.txt                       # Python dependencies
```

## Dataset
**Source:** [Datafiniti Consumer Reviews of Amazon Products](https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products)  
- ~28K verified Amazon customer reviews across multiple product categories  
- Key column used: `reviews.text` (main review content)

The dataset is automatically downloaded via `kagglehub` when you run the notebook.

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/amazon-reviews-sentiment-analysis.git
cd amazon-reviews-sentiment-analysis

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download the spaCy medium model
python -m spacy download en_core_web_md
```

### requirements.txt
```txt
pandas
spacy>=3.0
spacytextblob
kagglehub
textblob
jupyter
```

## How to Run

Simply open and run the Jupyter notebook:

```bash
jupyter notebook sentiment_analysis.ipynb
```

The notebook will:
1. Load the dataset (cached via kagglehub for speed)
2. Clean missing/duplicated reviews
3. Preprocess text (lowercase, remove stop words & punctuation)
4. Add sentiment polarity & subjectivity using TextBlob
5. Show example outputs and review similarity
6. Return a final DataFrame with the following new columns:
   - `clean_text`
   - `sentiment_label`  (Positive / Negative / Neutral)
   - `polarity`         (-1 to +1)
   - `subjectivity`    (0 to 1)

## Sample Output
```
Review: This product is amazing! Works better than expected.  
Sentiment: Positive | Polarity: 0.3833 | Subjectivity: 0.6000  

Review: Terrible quality. Completely disappointed.  
Sentiment: Negative | Polarity: -0.8750 | Subjectivity: 0.8750  

Similarity between two real reviews: **0.8651**

## Key Features
- Rule-based sentiment thresholds (`>0.1` → Positive, `< -0.1` → Negative)
- Semantic similarity using spaCy word vectors
- Clean, modular, well-documented code
- Full reproducibility

## Strengths & Limitations (from the report)

| Strengths                                 | Limitations                                      |
|-------------------------------------------|--------------------------------------------------|
| Simple & highly interpretable             | TextBlob not fine-tuned for Amazon reviews       |
| Fast preprocessing with spaCy             | Struggles with sarcasm and mixed opinions        |
| Built-in subjectivity scoring             | No transformer models (e.g., BERT, RoBERTa)    |
| Good performance on clear emotional text  | Medium spaCy model less accurate than transformer embeddings |

## Future Improvements
- Replace TextBlob with a fine-tuned BERT model (`nlptown/bert-base-multilingual-uncased-sentiment` or `cardiffnlp/twitter-roberta-base-sentiment-latest`)
- Add aspect-based sentiment extraction
- Visualize sentiment distribution by product category
- Deploy as a web app (Streamlit/FastAPI)

## Author
**Koketso Llale**  
November 2025

## License
This project is licensed under the MIT License.

---
**Feel free to star the repo if you find it useful!**
``` 
