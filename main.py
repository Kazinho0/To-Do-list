from fastapi import FastAPI
from fastapi import HTTPException , Depends
from database import connection
from models import Tarefas
from schema import CreateTarefa , ResponseTarefa

app = FastAPI()
