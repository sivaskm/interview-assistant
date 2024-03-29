from fastapi import FastAPI 
from schema import UserRequest, ScoreRequest, StartRequest
from handler import save_cv, save_jd, extract_text_from_pdf, get_response, get_score, start_interview
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import Dict

app = FastAPI()


@app.post("/interview")
async def query(user_request: UserRequest):
    response = get_response(user_request)
    return response


@app.post("/uploadjd")
async def upload_job_description(text: str = Form(None), file: UploadFile = File(None)):
    # print(extract_text_from_pdf(file))
    return save_jd(text, file)

@app.post("/uploadcv")
async def upload_job_description(text: str = Form(None), file: UploadFile = File(None)):
    return save_cv(text, file)

@app.post("/score")
async def score(score_request: ScoreRequest):
    return get_score(score_request)

@app.post("/start")
async def score(start_request: StartRequest):
    return start_interview(start_request)