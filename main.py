from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def inicio():
    return RedirectResponse(url="/deporte")

@app.get("/deporte")
def deporte(request: Request):
    datos = {
        "nombre": "Fútbol",
        "jugadores_por_equipo": 11,
        "usa_balon": True,
    }
    return templates.TemplateResponse(
        request=request,
        name="deporte.html",
        context={"deporte": datos},
    )

@app.get("/planetas")
def planetas(request: Request):
    lista_planetas = [
        "Mercurio",
        "Venus",
        "Tierra",
        "Marte",
        "Júpiter",
        "Saturno",
        "Urano",
        "Neptuno",
    ]
    return templates.TemplateResponse(
        request=request,
        name="planetas.html",
        context={"planetas": lista_planetas},
    )

@app.get("/categorias")
def categorias(request: Request):
    datos = {
        "Electrónica": [
            {"producto": "Laptop",    "precio": "$850"},
            {"producto": "Audífonos", "precio": "$120"},
            {"producto": "Cargador",  "precio": "$35"},
        ],
        "Ropa": [
            {"producto": "Camiseta",  "precio": "$25"},
            {"producto": "Pantalón",  "precio": "$55"},
        ],
        "Alimentos": [],
    }
    return templates.TemplateResponse(
        request=request,
        name="categoria.html",
        context={"categorias": datos},
    )