# ML Application with Pretrained Model and Tests

[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

## Overview

This FastAPI application provides endpoints to perform sentiment analysis on provided English text using the [Hugging Face](https://huggingface.co/) library.

## Endpoints

### GET /

Returns a welcome message.

- **URL**: `/`
- **Method**: `GET`
- **Response**:
  - `200 OK`: `{"message": "Hello World"}`

### POST /predict/

Returns the sentiment analysis of the provided text.

- **URL**: `/predict/`
- **Method**: `POST`
- **Request Body**:
  - `text`: `string`
- **Response**:
  - `200 OK`: `{"label": "LABEL_NAME", "score": "SCORE_VALUE"}`

### GET /model_info/

Returns information about the model used for sentiment analysis.

- **URL**: `/model_info/`
- **Method**: `GET`
- **Response**:
  - `200 OK`: `{"model": "distilbert-base-uncased-finetuned-sst-2-english", "task": "sentiment-analysis"}`

## Running the App

To run the app locally, use the following command:

```bash
uvicorn app:app --reload
