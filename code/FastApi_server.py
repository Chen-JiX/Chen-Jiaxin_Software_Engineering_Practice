# coding=utf-8
from fastapi import FastAPI, UploadFile
import uvicorn
import os


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello! This is a test checking application"}


# @app.get("/path")
# async def function_demo_get():
#     return {"message": "This is /path endpoint"}


# @app.post('/path')
# async def postdata(people: People):
#     return people


@app.post('/uploadrightanswer')
async def get_answer(file: UploadFile):

    path = os.path.join("answer", file.filename)

    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    # ans_matrix = read_frame.read_frame(path)
    # print(ans_matrix)
    print("Get right answer")
    return {
        "message": "The right answer uploaded successfully"
    }


@app.post('/upload')
async def get_student_answer(file: UploadFile):

    path = os.path.join("student_answers", file.filename)

    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)

    print(f"Got the test answer from {file.filename[0:-4]}")


if __name__ == "__main__":
    uvicorn.run("FastApi_server:app", host="127.0.0.1", port=8080, reload=True)
