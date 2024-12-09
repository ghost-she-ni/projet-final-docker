from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import motor.motor_asyncio
import os
from bson import ObjectId

# Récupérer l'URI de MongoDB depuis les variables d'environnement
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Initialisation de l'application et de la base de données
app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.task_manager
tasks_collection = db.tasks

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (vous pouvez restreindre à une liste spécifique)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

# Custom Pydantic Model to handle ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# Modèle pour les tâches
class Task(BaseModel):
    id: str = Field(default_factory=str, alias="_id")  # Inclure l'ID dans la réponse
    title: str
    description: str
    status: str = "À faire"  # Par défaut

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "648d1f95c4e8f4e2e0a4c123",
                "title": "Apprendre FastAPI",
                "description": "Créer une API REST avec FastAPI",
                "status": "À faire"
            }
        }

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    task_dict = task.dict(exclude={"_id"})  # Exclut l'_id s'il est vide ou non défini
    result = await tasks_collection.insert_one(task_dict)  # Insère la tâche dans MongoDB
    task_dict["_id"] = str(result.inserted_id)  # Récupère et assigne l'ID généré par MongoDB
    return task_dict  # Retourne la tâche avec l'ID

@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    tasks = await tasks_collection.find().to_list(length=100)
    for task in tasks:
        task["_id"] = str(task["_id"])  # Convertir l'ObjectId en chaîne
    return tasks

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    result = await tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 1:
        return {"message": "Tâche supprimée"}
    raise HTTPException(status_code=404, detail="Tâche non trouvée")
