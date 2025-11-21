# AWS Bedrock Claude Integration

A Python application that provides an interface to interact with AWS Bedrock's Claude Sonnet 4.5 model. This project demonstrates how to implement both single message interactions and conversational chat with maintained history.

## Features

- **Single Message Interaction**: Send individual queries to Claude and receive responses
- **Conversational Chat**: Maintain conversation history for context-aware interactions
- **Error Handling**: Robust error handling for AWS client errors and general exceptions
- **Environment Configuration**: Secure configuration using environment variables

## Prerequisites

- Python 3.x
- AWS Bedrock access with Claude Sonnet 4.5 model permissions
- Valid AWS credentials/API key for Bedrock access

## Installation

### Automatic Setup

Run the provided setup script:

```bash
chmod +x auto.sh
./auto.sh
```

### Manual Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requeriments.txt
   ```

## Configuration

1. **Environment Variables:**
   Create a `.env` file in the project root with your AWS Bedrock credentials:
   ```
   AWS_BEARER_TOKEN_BEDROCK=your_aws_bearer_token_here
   ```

   **Important:** Never commit the `.env` file to version control. Add it to your `.gitignore`.

2. **AWS Region:**
   The application is configured to use `us-east-1` region by default. You can modify this in the `main.py` file if needed.

## Usage

### Running the Application

```bash
python main.py
```

### Code Examples

#### Simple Message
```python
from main import crear_cliente_bedrock, enviar_mensaje

client = crear_cliente_bedrock()
response = enviar_mensaje(client, "Your question here")
print(response)
```

#### Conversational Chat
```python
from main import crear_cliente_bedrock, chat_con_historial

client = crear_cliente_bedrock()
historial = []

response, historial = chat_con_historial(
    client, 
    historial, 
    "Your first message"
)

response, historial = chat_con_historial(
    client, 
    historial, 
    "Follow-up question"
)
```

## Project Structure

```
bedrock_sample/
├── main.py              # Main application code
├── requeriments.txt     # Python dependencies
├── auto.sh             # Automatic setup script
├── .env                # Environment variables (create this)
└── README.md           # This file
```

## Functions Overview

- `crear_cliente_bedrock()`: Creates and configures the AWS Bedrock client
- `enviar_mensaje()`: Sends a single message to Claude and returns the response
- `chat_con_historial()`: Manages conversational interactions with message history

## Model Information

- **Model**: Claude Sonnet 4.5 (global.anthropic.claude-sonnet-4-5-20250929-v1:0)
- **API Version**: bedrock-2023-05-31
- **Default Max Tokens**: 2000
- **Temperature**: 1.0

## Error Handling

The application includes comprehensive error handling for:
- Missing environment variables
- AWS client errors
- Model invocation failures
- Network connectivity issues

## Security Considerations

- Store sensitive credentials in environment variables
- Never hardcode API keys in source code
- Add `.env` files to `.gitignore`
- Use appropriate IAM permissions for AWS Bedrock access

## Dependencies

- `boto3`: AWS SDK for Python
- `botocore`: Core functionality for AWS SDK
- `python-dotenv`: Load environment variables from .env files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is provided as-is for educational and development purposes.

## Support

For issues related to:
- **AWS Bedrock**: Check AWS documentation and service status
- **Model Limits**: Verify your AWS account limits and permissions
- **Authentication**: Ensure your credentials are valid and have appropriate permissions

---

**Note**: Make sure to configure your AWS credentials properly before running the application. The application requires valid AWS Bedrock access permissions.