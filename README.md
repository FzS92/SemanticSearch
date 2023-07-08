[![MITLicense](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Python application](https://github.com/FzS92/Semantic_Search/actions/workflows/python-app.yml/badge.svg)](https://github.com/FzS92/Semantic_Search/actions/workflows/python-app.yml)
[![Python package](https://github.com/FzS92/Semantic_Search/actions/workflows/python-package.yml/badge.svg)](https://github.com/FzS92/Semantic_Search/actions/workflows/python-package.yml)
[![Semgrep](https://github.com/FzS92/Semantic_Search/actions/workflows/semgrep.yml/badge.svg)](https://github.com/FzS92/Semantic_Search/actions/workflows/semgrep.yml)
# Semantic Search

This repository contains a Python code that utilizes semantic search. It compares the encoded representation of a query with the encoded representation of each sentence or paragraph in a given context and selects the top k most similar results.

## Installation

To run the code locally, please follow these instructions:

1. Clone this repository:

```python
git clone https://github.com/FzS92/SemanticSearch
cd SemanticSearch
```
2. Install the required dependencies:
```python
pip install -r requirements.txt
```

## Usage
1. Run the application:
```python
python app.py
```
2. Open the web interface and specify your desired search mode, whether it be paragraph or sentence, and enjoy the search! 

![App Screenshot](./screenshots/app_screenshot.png)

## HuggingFace Space
You can access the web interface and try out by visiting the following link:

HuggingFace Space: [Semantic Search](https://huggingface.co/spaces/fzs/SemanticSearch)

