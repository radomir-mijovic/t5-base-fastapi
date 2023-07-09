# FastAPI and T5-base Model application for user input translation

# What is the t5 base model
The model t5 base is a Natural Language Processing
(NLP) Model implemented in a Transformer library,
generally using the Python programming language used for text-text translations.

For more information about the model, visit https://huggingface.co/t5-base

# Installation
```
Building with Docker Compose and running using Nginx
```

docker-compose -f compose.yaml up -d --build

Navigate to http://127.0.0.1:80/

**Note** On startup, the t5-base model would be downloaded.

The application was developed with a 24GB RAM and 1.80GHz CPU Speed.