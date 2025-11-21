# Integración con AWS Bedrock Claude

Una aplicación en Python que proporciona una interfaz para interactuar con el modelo Claude Sonnet 4.5 de AWS Bedrock. Este proyecto demuestra cómo implementar tanto interacciones de mensajes individuales como chat conversacional con historial mantenido.

## Características

- **Interacción de Mensaje Simple**: Envía consultas individuales a Claude y recibe respuestas
- **Chat Conversacional**: Mantiene el historial de conversación para interacciones conscientes del contexto
- **Manejo de Errores**: Manejo robusto de errores para errores del cliente AWS y excepciones generales
- **Configuración de Entorno**: Configuración segura usando variables de entorno

## Requisitos Previos

- Python 3.x
- Acceso a AWS Bedrock con permisos para el modelo Claude Sonnet 4.5
- Credenciales/API key válidas de AWS para acceso a Bedrock

## Instalación

### Configuración Automática

Ejecuta el script de configuración proporcionado:

```bash
chmod +x auto.sh
./auto.sh
```

### Configuración Manual

1. **Crear un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requeriments.txt
   ```

## Configuración

1. **Variables de Entorno:**
   Crea un archivo `.env` en la raíz del proyecto con tus credenciales de AWS Bedrock:
   ```
   AWS_BEARER_TOKEN_BEDROCK=tu_token_bearer_aws_aqui
   ```

   **Importante:** Nunca subas el archivo `.env` al control de versiones. Agrégalo a tu `.gitignore`.

2. **Región de AWS:**
   La aplicación está configurada para usar la región `us-east-1` por defecto. Puedes modificar esto en el archivo `main.py` si es necesario.

## Uso

### Ejecutar la Aplicación

```bash
python main.py
```

### Ejemplos de Código

#### Mensaje Simple
```python
from main import crear_cliente_bedrock, enviar_mensaje

client = crear_cliente_bedrock()
respuesta = enviar_mensaje(client, "Tu pregunta aquí")
print(respuesta)
```

#### Chat Conversacional
```python
from main import crear_cliente_bedrock, chat_con_historial

client = crear_cliente_bedrock()
historial = []

respuesta, historial = chat_con_historial(
    client, 
    historial, 
    "Tu primer mensaje"
)

respuesta, historial = chat_con_historial(
    client, 
    historial, 
    "Pregunta de seguimiento"
)
```

## Estructura del Proyecto

```
bedrock_sample/
├── main.py              # Código principal de la aplicación
├── requeriments.txt     # Dependencias de Python
├── auto.sh             # Script de configuración automática
├── .env                # Variables de entorno (crear este archivo)
└── README.md           # Este archivo
```

## Descripción de Funciones

- `crear_cliente_bedrock()`: Crea y configura el cliente de AWS Bedrock
- `enviar_mensaje()`: Envía un mensaje individual a Claude y devuelve la respuesta
- `chat_con_historial()`: Gestiona interacciones conversacionales con historial de mensajes

## Información del Modelo

- **Modelo**: Claude Sonnet 4.5 (global.anthropic.claude-sonnet-4-5-20250929-v1:0)
- **Versión de API**: bedrock-2023-05-31
- **Tokens Máximos por Defecto**: 2000
- **Temperatura**: 1.0

## Manejo de Errores

La aplicación incluye manejo integral de errores para:
- Variables de entorno faltantes
- Errores del cliente AWS
- Fallos en la invocación del modelo
- Problemas de conectividad de red

## Consideraciones de Seguridad

- Almacena credenciales sensibles en variables de entorno
- Nunca hardcodees API keys en el código fuente
- Agrega archivos `.env` al `.gitignore`
- Usa permisos IAM apropiados para acceso a AWS Bedrock

## Dependencias

- `boto3`: SDK de AWS para Python
- `botocore`: Funcionalidad central para AWS SDK
- `python-dotenv`: Carga variables de entorno desde archivos .env

## Contribuir

1. Haz un fork del repositorio
2. Crea una rama de características
3. Realiza tus cambios
4. Prueba exhaustivamente
5. Envía un pull request

## Licencia

Este proyecto se proporciona tal como está para fines educativos y de desarrollo.

## Soporte

Para problemas relacionados con:
- **AWS Bedrock**: Consulta la documentación de AWS y el estado del servicio
- **Límites del Modelo**: Verifica los límites de tu cuenta AWS y permisos
- **Autenticación**: Asegúrate de que tus credenciales sean válidas y tengan los permisos apropiados

---

**Nota**: Asegúrate de configurar tus credenciales de AWS correctamente antes de ejecutar la aplicación. La aplicación requiere permisos válidos de acceso a AWS Bedrock.