# Slogan Classifier & Generator

A Python project for processing a slogan dataset, building an industry-aware slogan generator using spaCy for preprocessing and a TensorFlow LSTM for sequence generation.

## Project Overview

This project aims to:
- Load and clean a dataset of business slogans.
- Preprocess text using spaCy, including tokenisation, lemmatisation, and stop-word cleaning.
- Engineer features by combining industry information with processed slogan text.
- Build and train an LSTM neural network to generate new, industry-specific slogans.
- Explore industry classification, sequence modelling, or future extensions.
**The core work is implemented in the notebook:**
neural_network_task.ipynb

## Project Structure
├── neural_network_task.ipynb
├── slogan-valid.csv
├── README.md   ← (this file)

## Technologies Used
**Languages:**
    - Python 3.8+

**Libraries:**
- spaCy (text preprocessing)
- TensorFlow / Keras (LSTM model)
- NumPy, Pandas (data handling)
- Matplotlib / Seaborn (visualisation)
- ML / NLP

**Tokenisation & lemmatisation**
- Sequence vectorisation
- Word embeddings
- LSTM sequence generation

## Dataset Information

The project uses a file named slogan-valid.csv, containing:
- slogan – company slogan text
- business_name – associated company name
- industry – category or sector
- Additional columns depending on source

# The notebook:

- Loads the dataset
- Removes null/invalid rows
- Adds a modified_slogan column containing
industry + processed_slogan
to give the model context.

### Preprocessing Steps
- Convert text to lowercase
- Tokenise using spaCy
- Remove stop words & punctuation
- Apply lemmatisation
- Recombine cleaned tokens
- Build the combined industry-aware text field

## Model Architecture
- The LSTM model includes:
- Tokeniser vocabulary from processed slogans
- Sequences padded via pad_sequences
- Embedding layer for word vector representation
- LSTM layers for sequence learning
- Dense output layer for predicting next tokens

## How to Run the Project
1. Install dependencies
'''
pip install pandas numpy spacy tensorflow
'''

'''
python -m spacy download en_core_web_md
'''
1. Open the notebook
neural_network_task.ipynb
4. Run each cell in order

## The notebook is self-contained and includes instructions for:
- Loading the dataset
- Preprocessing text
- Preparing training sequences
- Training the model
- Generating new slogans

## Example Usage

Once the model is trained, you can generate a slogan using:
'''
generate_slogan("technology")
'''

## Possible output:

"technology delivering innovation for the future"

## Future Improvements

- Add a Transformer-based generator (e.g., GPT-2 Finetune)
- Add industry classification as a secondary task
- Improve sequence diversity using temperature sampling
- Add a web interface with Flask / FastAPI

### License

This project is provided as open educational material.
Add your license here if needed (MIT, GPL, etc.).
