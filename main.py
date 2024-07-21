import uvicorn
import uvicorn
from fastapi import FastAPI

from infraestructure.configuration.seed_categories import seed_categories
from infraestructure.web.rest.controller import routes

app = FastAPI()


app.include_router(routes.controller)

seed_categories()

if __name__ == "__main__":
    uvicorn.run(app, port=3001)

