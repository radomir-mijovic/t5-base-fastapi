from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.v1 import translate
from app.core.config import Settings

settings = Settings()


app = FastAPI()
app.include_router(translate.router, prefix=settings.TRANSLATE_PREFIX)


@app.get("/", include_in_schema=False)
def home():
    # Redirect user from a root path
    # to the automatically compiled FastAPI documentation (/docs)
    return RedirectResponse(url=settings.DOCS_PREFIX)
