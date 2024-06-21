from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ラーメンが食いたいyo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html> 
        <head>
            <title>デプロイできないよ</title>
        </head>
        <body>
            <h1>デプロイができない</h1>
            <p>学校のwifiじゃないとデプロイできない、、なんてことはないよね</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

    @app.post("/present")
async def give_present(present):
    return {"response": f" よろしく。私,人間です。 {present}では金の斧をあげる。"}  # f文字列というPythonの機能を使っている