from fastapi import FastAPI
from fastapi.responses import HTMLResponse as hr
from fastapi.responses import RedirectResponse as rr
from fastapi.responses import FileResponse

app = FastAPI()

file_path="TinDog-start-masrter2/index.html"

@app.get("/")
async def rout():
    return FileResponse(file_path)



@app.get("/reshtml", response_class=hr)
async def rout():
    return """<html>
                <body><h1>fsdfdfs</h1></body>
              </html>

"""

@app.get("/item/{item}")
async def item(item):
    return item

@app.get("/redirectex", response_class = rr)
async def redirect():
    return "https://google.com/"
