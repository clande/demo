#!/usr/bin/env python3
import frontend
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/document/load_status')
def get_load_status():
    print('loading status')
    x = {"status":"alive"}
    print('loaded status')
    return x

frontend.init(app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
    # print('Please start the app with the "uvicorn" command as shown in the start.sh script')