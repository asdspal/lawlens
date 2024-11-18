# Legal LLM Application

## Overview

This Legal LLM Application is a comprehensive tool designed to assist legal professionals, researchers, and scholars in various aspects of legal analysis and research. It leverages advanced natural language processing techniques and graph-based retrieval to provide intelligent insights into legal documents, cases, and trends.

## Features

1. **Legal Precedent Explorer**: Search and analyze legal precedents based on complex queries.
2. **Judgment Summarization**: Generate concise summaries of lengthy legal judgments.
3. **Legal Trend Analyzer**: Identify and explain trends in Supreme Court decisions over time.
4. **Case Outcome Predictor**: Predict potential outcomes of new cases based on historical data.
5. **Legal Research Assistant**: Intelligent search and cross-referencing of legal documents.
6. **Constitutional Interpretation Tracker**: Track the evolution of constitutional article interpretations.  
7. **Judge Profile and Analysis Tool**: Analyze patterns in individual judges' decision-making.

## Installation

1. Clone the repository:
git clone https://github.com/asdspal/lawlens.git
cd llawlens


2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install the required packages:

pip install -r requirements.txt


## Usage

To run the Streamlit application:

streamlit run app/main.py


Navigate to the provided local URL in your web browser to interact with the application.

## Configuration

The application configuration can be modified in `app/config.py`. This includes paths for data directories and other settings.

## Data

The application expects legal documents and case data to be present in the `data/raw` directory. Processed data will be stored in `data/processed`, and the knowledge graph data in `data/knowledge_graph`.

## Testing

To run the unit tests:

python -m unittest discover tests


## Logging

Logs are stored in the `logs` directory. There are separate log files for the main application, models, and features.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


