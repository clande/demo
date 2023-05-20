#!/usr/bin/env python3

import requests
from fastapi import Request, FastAPI
from nicegui import ui


def init(app: FastAPI) -> None:
    # put your own secret key in an environment variable MY_SECRET_KEY
    ui.run_with(app=app, title='demo')

    @ui.page('/')
    async def page_layout(request: Request):

        ui.label('prelabel')
        grid_data = []
        print('calling get_status')
        response = requests.get('http://127.0.0.1:8080/document/load_status', timeout=5)
        status = response.json()
        print('get_status completed')
        grid_data = [status]
        print(f'grid_data = {grid_data}')
        ui.label('postlabel')


