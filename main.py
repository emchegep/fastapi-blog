from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Peter Chegeh",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
{
        "id": 2,
        "author": "Jone Doe.",
        "title": "Python for Web.",
        "content": "Python is a great language for web development.",
        "date_posted": "April 21, 2025",
    },

{
        "id": 3,
        "author": "Elvis Chege.",
        "title": "Jinja2 Templating Engine.",
        "content": "The Jinja2 templating engine is great for frontend.",
        "date_posted": "February 04, 2026",
    },
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts,
                                                             "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts
