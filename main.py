from fastapi import FastAPI
from api.environment import router as environment_router

app = FastAPI()

app.include_router(environment_router, prefix="/api")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
