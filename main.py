import boto3
import json
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Configuración
AWS_REGION = "us-east-1"
MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"  # Claude Sonnet 4.5 (regional endpoint)

def crear_cliente_bedrock():
    """
    Crea y retorna un cliente de Bedrock Runtime usando API Key
    """
    try:
        # Obtener API key de variable de entorno
        load_dotenv()
        api_key = os.environ.get('AWS_BEARER_TOKEN_BEDROCK')
        if not api_key:
            raise ValueError("AWS_BEARER_TOKEN_BEDROCK no está configurado")
        
        # Establecer como variable de entorno para boto3
        os.environ['AWS_SESSION_TOKEN'] = api_key
        
        # Crear cliente
        client = boto3.client(
            service_name='bedrock-runtime',
            region_name=AWS_REGION
            # Boto3 detectará automáticamente las credenciales desde las fuentes arriba mencionadas
        )
        return client
    except Exception as e:
        print(f"Error creando cliente: {e}")
        return None

def enviar_mensaje(client, mensaje_usuario, max_tokens=2000):
    """
    Envía un mensaje a Claude Sonnet 4.5 y retorna la respuesta
    """
    try:
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": mensaje_usuario
                }
            ],
            "temperature": 1.0
        })
        
        response = client.invoke_model(
            modelId=MODEL_ID,
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        texto_respuesta = response_body['content'][0]['text']
        
        return texto_respuesta
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        print(f"Error de AWS: {error_code} - {error_message}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def chat_con_historial(client, historial_mensajes, nuevo_mensaje, max_tokens=2000):
    """
    Mantiene un historial de conversación con Claude
    """
    try:
        historial_mensajes.append({
            "role": "user",
            "content": nuevo_mensaje
        })
        
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": historial_mensajes,
            "temperature": 1.0
        })
        
        response = client.invoke_model(
            modelId=MODEL_ID,
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        texto_respuesta = response_body['content'][0]['text']
        
        historial_mensajes.append({
            "role": "assistant",
            "content": texto_respuesta
        })
        
        return texto_respuesta, historial_mensajes
        
    except Exception as e:
        print(f"Error: {e}")
        return None, historial_mensajes

if __name__ == "__main__":
    print("=== Ejemplo 1: Mensaje Simple ===")
    client = crear_cliente_bedrock()
    
    if client:
        respuesta = enviar_mensaje(
            client, 
            "Hola, explícame en 3 líneas qué es machine learning"
        )
        if respuesta:
            print(f"Claude responde:\n{respuesta}\n")
    
        print("=== Ejemplo 2: Conversación con Historial ===")
        historial = []
        
        respuesta1, historial = chat_con_historial(
            client,
            historial,
            "¿Cuál es la capital de Francia?"
        )
        print(f"Usuario: ¿Cuál es la capital de Francia?")
        print(f"Claude: {respuesta1}\n")
        
        respuesta2, historial = chat_con_historial(
            client,
            historial,
            "¿Y cuántos habitantes tiene?"
        )
        print(f"Usuario: ¿Y cuántos habitantes tiene?")
        print(f"Claude: {respuesta2}")
