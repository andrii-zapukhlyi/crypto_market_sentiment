# Crypto Market Sentiment Analysis with NLP
## Demo 
#### Using Docker Image
A Docker image for **amd64** and **ARM** platforms is available on **DockerHub**. You can pull and run the container on your machine using the following commands:
```
docker pull b3nett/crypto_sentiment_app:latest
docker run -d -p 80:80 b3nett/crypto_sentiment_app
```
Then, open `http://localhost:80` in your browser. 

#### Using FastAPI
If you prefer not to use Docker, you can clone the repository and run the API with **Uvicorn**:
```
git clone https://github.com/andrii-zapukhlyi/crypto_market_sentiment.git
cd crypto_market_sentiment/app
uvicorn api:app --host 0.0.0.0 --port 80
```
Then, open `http://localhost:80` in your browser. 

## Objective
The main objective of this project is to analyze cryptocurrency market sentiment using Natural Language Processing (NLP) techniques. By extracting insights from news articles, the project aims to enhance decision-making by providing traders and investors with sentiment-based insights to optimize their trading strategies.

## Solution
To analyze cryptocurrency market sentiment, news articles are processed using NLP techniques such as cleaning and tokenization. Features like TF-IDF and n-grams are extracted and visualized. Both classic ML models (Logistic Regression, tree-based models, gradient boosting) and deep learning models (LSTM, GRU, CNN) are trained for sentiment classification.

## Achievements
The best model (CNN) achieved:

-  Accuracy: 0.95
- ROC AUC score: 0.98
- F1-score: 0.95

The LSTM and GRU models achieved slightly lower performance.

## Conclusion
The project successfully analyzed cryptocurrency market sentiment using NLP, with deep learning models outperforming traditional approaches. The CNN model achieved the best results, with a ROC AUC score of 0.98 and an F1-score of 0.95. While some misclassifications occurred, the overall accuracy was high, demonstrating the model's effectiveness in providing sentiment-based insights for trading decisions.
