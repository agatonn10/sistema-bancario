import json

ARCHIVO_DATOS = "base_datos.json"
Datos = {}

def guardado(data):
  """Datos Guardandose al JSON"""
  with open(ARCHIVO_DATOS, "w", encoding = "utf-8") as f:
    json.dump(data,f, indent=4, ensure_ascii=False)

def cargar_datos():
  """Datos Guardados al archivo JSON"""
  try:
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
      return json.load(f)
  except FileNotFoundError:
    return {}
