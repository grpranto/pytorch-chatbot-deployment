# Chatbot Deployment with FastAPI and JavaScript

Deployed the contextual chatbot model that I developed in [this](https://github.com/grpranto/pytorch-chatbot) repo with FastAPI and JavaScript.

![image](https://github.com/user-attachments/assets/27372977-9cc5-4dc2-b392-5ab67023a7d3)

This gives the following deployment option:
- Deploy within FastAPI app with jinja2 template

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/grpranto/pytorch-chatbot-deployment.git
$ cd pytorch-chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install fastapi[standard] torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt_tab')
```
Modify `intents.json` with different intents and responses for your own Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.

## Run the FastAPI server

```
uvicorn app:app --reload
```

## Access the FastAPI application

```
http://localhost:8000/
```

## Note

You must re-run the training whenever the `intents.json` file is modified.

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
