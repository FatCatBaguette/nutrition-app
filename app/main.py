from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Recipe(BaseModel):
    name: str
    calories: int
    protein: float
    fat: float
    carbs: float

recipes = []

@app.post("/add")
def add_recipe(recipe: Recipe):
    recipes.append(recipe)
    return {"message": "Recipe added"}

@app.get("/list")
def list_recipes():
    return recipes
