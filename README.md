## Grupo 7

### Equipo

| Nombre del equipo |
| - | 
|XCode |

### Integrantes

| Nombre | Correo | Usuario GitHub |
| - | - | - | 
| Andres Felipe Losada Luna | af.losada@uniandes.edu.co | [@AfLosada](https://github.com/AfLosada) | 
| Cristian Arnulfo Arias Vargas | ca.ariasv1@uniandes.edu.co | [@CristianAAV](https://github.com/CristianAAV) | 
| Emerson Chaparro Ampa | e.chaparroa@uniandes.edu.co | [@echaparroa-uniandes](https://github.com/echaparroa-uniandes) | 
| Juan Camilo Vallejos | j.vallejosg@uniandes.edu.co | [@juanca-uniandes](https://github.com/juanca-uniandes) | 

### Diagrama 
[Diagrama](https://github.com/CristianAAV/DEVOPS/wiki/Diagrama-E1)

### Instrucciones para la ejecución local
- Crear contenedor para la BD de pruebas, puede utilizar el siguiente comando:
    ```bash
    docker run --name cntpostgres \
        -e POSTGRES_DB=postgres_db \
        -e POSTGRES_USER=postgres_user \
        -e POSTGRES_PASSWORD=postgres_pass \
        -p 5432:5432 \
        -d postgres:14
    ```
- Activar el entorno virtual, puede utilizar los siguientes comandos en Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
- Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
- Ejecutar la aplicación:
    ```bash
    export FLASK_DEBUG=1
    export FLASK_APP=application.py
    flask run
    ```
### Instrucciones para la ejecución de pruebas de manera local
- Para ejecutar pruebas de manera local, en el archivo `src/config/app_config.py`, actualizar la varible con el siguiente valor `env_file = find_dotenv('.env.test')` para ejecutar en SQLite y correr el siguiente comando:
    ```bash
    pytest tests/test_blacklist.py
    ```
    ***Total de covertura: 87%***
