# Inventory Events.
### Aspectos Tenicos.
- Para la construcion del API se utilizo el framework [FastAPI](https://fastapi.tiangolo.com/).
- Se uso [MongoDB](https://www.mongodb.com/) como base de datos principal.

## Descripción

Esta API se diseñó  para crear una serie de eventos relacionados a la auditoría de inventario para una empresa con múltiples sucursales que se dedica a la venta al menudeo (supermercados), en el cual se podrá hacer CRUD (Crear, leer, actualizar y eliminar) los eventos.

> Nota: Una vez revisado el evento, no podrá ser eliminado y el requerimiento deberá seguir su proceso.


Con esta API inicialmente se podrá manejar tres estados de eventos de auditoria, los cuales son:
- **Solicitud** : Este evento es creado por el gerente regional, para que que desde el departamento de auditoría inicien los respectivos preparativos con el fin de realizar conteo a uno o varios productos, según sea el requerimiento, este proceso requiere de Gestión, una vez sea revisado el evento.

- **Revisión**: en caso de requerir lo, se puede crear un evento con el mismo producto y o varios. En este caso el departamento de auditoría deberá gestionar un segundo conteo con un tiempo no mayor a 7 días hábiles. Con este tipo de evento se entiende que ya ese producto y/o productos fueron contados y se requiere de una segunda revisión.

- **Aprobación**: Este evento indica que ese producto y/o productos ya fueron contados 2 veces, y que según la descripción y los datos, se puede aprobar la auditoría sin requerir ningún tipo de gestión.

## Índice 

- [Preparacion](#Preparacion)
- [Instalación](#instalación)
- [Uso](#uso)

## Preparacion
- Instalar Docker y Docker Compose en su sistema local siguiendo las instrucciones proporcionadas en la   [documentación oficial de Docker ](https://docs.docker.com/) o puedes ver este [video tutorial](https://www.faztweb.com/contenido/doker-desktop-windows) .
- Instalar un editor de código. [Visual Studio Code](https://code.visualstudio.com).
- Tener una cuenta de usuario en [GitHub](https://github.com/).

## Instalación

- Inicie sesión en github e ingrese al siguiente repositorio público. [Inventory](https://github.com/estiven199/inventory).
- Obtenga la url del repositorio dando click en el botron verde (<> Code ),  en la opcion HTTPS.
- Clone el repositorio en su máquina.  [Siga estos pasos ](https://learn.microsoft.com/es-es/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette).
- Luego de clonar el repositorio, abra una terminal integrade dentro de Visual Studio Code, para esto seleccione Ver>Terminal en el menú principal.
- Ejecuta los siguientes comandos para crear las imágenes y contenedores necesarios en Docker.
> Nota: Asegúrese de que Docker se está Ejecutando.

```sh
docker compose build "Construye las imágenes de Docker que se especifican en el archivo docker-compose.yml"
docker compose up  "Crea y ejecuta los contenedores de un proyecto a partir de las imágenes de Docker"
```
- Abra el [Localhost](http://localhost:8000/docs) o la [Documentación](http://localhost:8000/redoc) y deberás ver la documentación del API.


## Uso

- El api está basado en el modelo de autenticación JWT, lo que significa que todos los endpoints requieren de un token para su uso, para ello debes crear un token de la siguiente manera:

 ```sh
import requests
import json
headers = {
'x-token':"gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
'x-api-key':"gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
'x-secret-id':"gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4=",
'user-id':"gAAAAABj4_Pn_TGye9V3YWTRfJo1HZAGEWVHy98Bf1XihDY7orahtgr4uv8XVWTp7KiwSHGJxVE5Jy_aPzzds88EYkx_yH5tXg=="
}
r_token = requests.post('http://127.0.0.1:8000/api/v1/login/access-token',headers=headers)
r_token = json.loads(r_token.text)
r_token
```
-  También se puede generar directamente desde la [documentación interactiva](http://localhost:8000/docs#/login/login_access_token_api_v1_login_access_token_post) de la API, dando click en el boton `"Try it out"`, y escribir los valores para cada campo con los mencionados arriba.  
- Con ese token ya puedes acceder a los demás endpoints .
> Nota: Este es un ejemplo de la respuesta a ese llamado. El token del ejemplo no sirve para el uso del API, por ello se recomienda crear uno.
 
 ```sh 
{'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwidXNlcl9pZCI6ImdBQUFBQUJqNF9Qbl9UR3llOVYzWVdUUmZKbzFIWkFHRVdWSHk5OEJmMVhpaERZN29yYWh0Z3I0dXY4WFZXVHA3S2l3U0hHSnhWRTVKeV9hUHp6ZHM4OEVZa3hfeUg1dFhnPT0iLCJleHAiOjE2NzY2NTg5OTZ9.SXQdcG_rxK2jQjZnyTekh63mDSx_udmfxZ0_OVR7eKQ',
 'token_type': 'bearer'}
 ```

***
### Eventos

> Nota: si desea crear eventos de ejemplo, puede hacer un llamado el endpoint [Generate Data Of Example](http://localhost:8000/docs#/Events/generate_data_of_example_api_v1_genetare_data_put)
- `GET`. Se puede obtener un solo evento o varios según algunos parámetros . [Ver documentación.](http://localhost:8000/docs)
 ```sh
# Se usa para buscar todos los eventos, o por un valor en especifico.
import requests
headers = {'token': r_token['access_token']}
params = {}
r1 = requests.get('http://127.0.0.1:8000/api/v1/events',headers=headers, params=params)
r1 = json.loads(r1.text)
r1

# Se usa para buscar un solo evento por el event_id.
import requests
headers = {'token': r_token['access_token']}
r1 = requests.get('http://127.0.0.1:8000/api/v1/events/63e4fb00fc658bca6378b585', headers=headers)
r1 = json.loads(r1.text)
r1
```
- `POST`. La creación de eventos está restringida a uno campos y valores, para ello se recomienda ver la documentación. [Ver documentación.](http://localhost:8000/docs)

> Nota: 
para el nombre se podrá seguir el siguiente formato:
Primera letra: inicial de la categoría del producto.
Segunda letra: inicial de la marca en específico.
El resto será la letra P seguido del número de identificación del punto de venta
Ejemplo: se desea auditar los aceites de marca girasol en el punto de venta 156
el nombre quedaría: AGP156.

 ```sh
import requests
headers = {'token': r_token['access_token']}
data = {
    "name": "AGP156",
    "type": "solicitud",
    "description": "Auditar los aceites de marca girasol de 3 litros en el punto de venta 156"
}
r1 = requests.post('http://127.0.0.1:8000/api/v1/events',headers=headers,json=data)
r1 = json.loads(r1.text)
r1
```
- `PUT`.  Actualizar un evento. [Ver documentación.](http://localhost:8000/docs)

> Nota: Solo se pueden actualizar eventos con estado `pendiente.`

 ```sh
import requests
headers = {'token': r_token['access_token']}
data = {
    "name": "AGP155"
    }
r1 = requests.put('http://127.0.0.1:8000/api/v1/events/63e4faa031061b0e632c4cf1', headers=headers, json=data)
r1 = json.loads(r1.text)
r1
```

- `DELETE`.  Eliminar un evento. [Ver documentación.](http://localhost:8000/docs)

 ```sh
import requests
headers = {'token': r_token['access_token']}
r1 = requests.delete('http://127.0.0.1:8000/api/v1/events/63e4faa031061b0e632c4cf1', headers=headers)
r1 = json.loads(r1.text)
r1
```


***
### Otros
- `PUT`.  Marcar un evento como Revisado. [Ver documentación.](http://localhost:8000/docs)
> Nota: Solo se pueden marcar eventos como revisado los que tiene estado `pendiente.` Una vez sean marcados, estos se clasifican según su tipo, para determinar si requieren de gestión o no.

 ```sh
import requests
headers = {'token': r_token['access_token']}
r1 = requests.put('http://127.0.0.1:8000/api/v1/events/mark_as_check/63e53d9b9c76d30d2d554476', headers=headers)
r1 = json.loads(r1.text)
r1
```
***