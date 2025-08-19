from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatSession, ChatMessage
import json
import uuid
import requests

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            session_id = data.get('session_id')

            if not user_message:
                return JsonResponse({'error': 'Message not provided'}, status=400)

            # Get or create chat session
            if session_id and ChatSession.objects.filter(session_id=session_id).exists():
                session = ChatSession.objects.get(session_id=session_id)
            else:
                session = ChatSession.objects.create()

            # Save user message
            ChatMessage.objects.create(
                session=session,
                sender='user',
                message=user_message
            )

            # --- Ollama API Integration ---
            ollama_url = "http://ollama:11434/api/generate"
            model_name = "llama2" # You can change this to any model you have pulled in Ollama

            try:
                payload = {
                    "model": model_name,
                    "prompt": user_message,
                    "stream": False # We want a single response, not a stream
                }
                headers = {"Content-Type": "application/json"}

                response = requests.post(ollama_url, json=payload, headers=headers)
                response.raise_for_status() # Raise an exception for HTTP errors

                ollama_response = response.json()
                bot_message_text = ollama_response.get("response", "Извините, не удалось получить ответ от Ollama.")

            except requests.exceptions.RequestException as e:
                bot_message_text = f"Извините, произошла ошибка при обращении к Ollama: {e}"
            except Exception as e:
                bot_message_text = f"Извините, произошла непредвиденная ошибка: {e}"
            # --- End Ollama API Integration ---
            
            # Save bot message
            ChatMessage.objects.create(
                session=session,
                sender='bot',
                message=bot_message_text
            )

            return JsonResponse({
                'response': bot_message_text,
                'session_id': str(session.session_id)
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)