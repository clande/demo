#!/usr/bin/env python3
'''This is only a very simple authentication example which stores session IDs in memory and does not do any password hashing.

Please see the `OAuth2 example at FastAPI <https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/>`_  or
use the great `Authlib package <https://docs.authlib.org/en/v0.13/client/starlette.html#using-fastapi>`_ to implement a real authentication system.

Here we just demonstrate the NiceGUI integration.
'''
import asyncio

import requests
from fastapi import Request, FastAPI
from nicegui import ui


def init(app: FastAPI) -> None:
    # put your own secret key in an environment variable MY_SECRET_KEY
    ui.run_with(app=app, title='demo')


    async def process_stuff():
        ui.notify("starting load_doc")
        await asyncio.sleep(3)
        ui.notify("finished load_doc")


    async def get_status():
        print('executing load status request')
        response = requests.get('http://127.0.0.1:8080/document/load_status', timeout=5)
        print('completed load status request')
        return response.json()

    @ui.page('/oneai')
    async def page_layout(request: Request):

        grid_data = []
        # print('executing load status request')
        # response = requests.get('http://127.0.0.1:8080/document/load_status', timeout=5)
        # print('completed load status request')
        print('calling get_status')
        status = await get_status()
        print('get_status completed')
        grid_data = [status]
        print(f'grid_data = {grid_data}')

        def load_doc():
            ui.notify("starting load_doc")
            # process_stuff()
            # grid_data = []
            # grid.options['rowData'] = grid_data
            # grid.update()
            ui.notify("finished load_doc")

        ui.button('Load Document', on_click=lambda: load_doc())
        grid = ui.aggrid({
            'columnDefs': [
                {'headerName': 'Name', 'field': 'name'},
                {'headerName': 'Collection', 'field': 'collection'},
                {'headerName': 'Status', 'field': 'status'}
            ],
            'rowData': grid_data,
            'rowSelection': 'multiple',
        }).classes('max-h-40')
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            ui.label('Inquisio.ai')
            # ui.button(on_click=lambda: right_drawer.toggle()).props('flat color=white icon=menu')
            with ui.button(on_click=lambda: menu.open()).props('flat color=white icon=menu'):
                with ui.menu() as menu:
                    ui.menu_item('Document Search', on_click=menu.close)
                    ui.menu_item('Document Ingest', on_click=menu.close)
                    ui.separator()
                    ui.menu_item('Logout', lambda: ui.open('/logout'))
        # with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        #     ui.label('LEFT DRAWER')
        with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
            # ui.label('RIGHT DRAWER')
            ui.button(on_click=lambda: right_drawer.toggle()).props('flat color=black icon=arrow_back')
            ui.separator()
            ui.link("Logout", '/logout').tailwind.padding('25px')
        with ui.footer(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            ui.label(f'Contact: ')
