import os
import urllib.request
import json
import xml.etree.ElementTree as ET
import ssl
from datetime import datetime
import tarfile
import io

API_KEY = os.environ.get("AEMET_API_KEY")
if not API_KEY:
    print("Error: No AEMET_API_KEY provided.")
    exit(1)

print("Obteniendo URL de datos de AEMET OpenData...")
try:
    req = urllib.request.Request(
        'https://opendata.aemet.es/opendata/api/avisos_cap/ultimoelaborado/area/esp',
        headers={'api_key': API_KEY}
    )
    context = ssl._create_unverified_context()
    resp = urllib.request.urlopen(req, context=context)
    data = json.loads(resp.read().decode('utf-8'))
except Exception as e:
    print(f"Error al conectar con AEMET: {e}")
    exit(1)

if 'datos' not in data:
    print("Error: la respuesta de AEMET no contiene URL de datos.", data)
    exit(1)

datos_url = data['datos']
print(f"Descargando TAR desde {datos_url} ...")

try:
    req2 = urllib.request.Request(datos_url)
    resp2 = urllib.request.urlopen(req2, context=context)
    tar_data = resp2.read()
except Exception as e:
    print(f"Error al descargar el TAR: {e}")
    exit(1)

print("Extrayendo y parseando XMLs del TAR...")
namespace = {'cap': 'urn:oasis:names:tc:emergency:cap:1.2'}
alertas_segovia = []

try:
    with tarfile.open(fileobj=io.BytesIO(tar_data), mode='r') as tar:
        for member in tar.getmembers():
            if member.isfile() and member.name.endswith('.xml'):
                f = tar.extractfile(member)
                if f:
                    xml_content = f.read().decode('windows-1252', errors='replace')
                    try:
                        root = ET.fromstring(xml_content)
                        # Root should be <cap:alert>
                        status = root.find('cap:status', namespace)
                        if status is None or status.text != 'Actual':
                            continue
                            
                        for info in root.findall('cap:info', namespace):
                            lang = info.find('cap:language', namespace)
                            if lang is None or lang.text != 'es-ES':
                                continue
                                
                            area = info.find('cap:area', namespace)
                            if area is not None:
                                areaDesc = area.find('cap:areaDesc', namespace)
                                if areaDesc is not None and ('Segovia' in areaDesc.text or 'Sistema Central' in areaDesc.text):
                                    headline = info.find('cap:headline', namespace).text if info.find('cap:headline', namespace) is not None else ""
                                    desc = info.find('cap:description', namespace).text if info.find('cap:description', namespace) is not None else ""
                                    valido_hasta = info.find('cap:expires', namespace).text if info.find('cap:expires', namespace) is not None else ""
                                    
                                    nivel = "Amarillo"
                                    for param in info.findall('cap:parameter', namespace):
                                        vn = param.find('cap:valueName', namespace)
                                        if vn is not None and vn.text == 'AEMET-Meteoalerta nivel':
                                            val = param.find('cap:value', namespace).text
                                            if val == 'amarillo': nivel = 'Amarillo'
                                            elif val == 'naranja': nivel = 'Naranja'
                                            elif val == 'rojo': nivel = 'Rojo'
                                    
                                    alertas_segovia.append({
                                        "nivel": nivel,
                                        "titulo": headline,
                                        "descripcion": desc,
                                        "valido_hasta": valido_hasta
                                    })
                    except Exception as ex:
                        print(f"Error parseando {member.name}: {ex}")
                        pass
except Exception as e:
    print(f"Error leyendo el TAR: {e}")
    exit(1)

print(f"Se han encontrado {len(alertas_segovia)} avisos para Segovia.")

unique_alertas = []
seen_titles = set()
for a in alertas_segovia:
    if a['titulo'] not in seen_titles:
        unique_alertas.append(a)
        seen_titles.add(a['titulo'])

from datetime import timezone
json_output = {
    "ultima_actualizacion": datetime.now(timezone.utc).isoformat(),
    "alertas": unique_alertas
}

cwd = "c:/Users/nexus/OneDrive/Documentos/ProyectosWeb/avpcelespinar/avpcelespinar-template"
os.makedirs(os.path.join(cwd, "data"), exist_ok=True)
json_path = os.path.join(cwd, "data", "alertas_aemet.json")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=4, ensure_ascii=False)

print(f"JSON guardado correctamente en {json_path}")
