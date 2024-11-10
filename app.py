from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chat import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

# Mounts the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Defines the request body model
class PredictRequest(BaseModel):
    message: str

# Defines the response body model
class PredictResponse(BaseModel):
    answer: str

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    text = request.message  
    response = get_response(text)
    return {"answer": response} 
#---------------------------
# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from chat import get_response

# app=Flask(name, template_folder='template')
# CORS(app)
# @app.route("/", methods=["GET"])
# def index_get():
# return render_template("base.html")

# @app.route("/predict", methods=["POST"])
# def predict():
# text = request.get_json(force=True).get("message")
# response = get_response(text)
# message = {"answer": response}
# return jsonify(message)

# if name == "main":
# app.run(debug=True)
#-----------------------------------

#----------------------------------
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )
#---------------------------------