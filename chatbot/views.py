
# chatbot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

from chatterbot import ChatBot

class ChatBotView(APIView):
    chatbot = ChatBot('MyBot')

    def post(self, request):
        user_message = request.data['message']
        bot_response = self.chatbot.get_response(user_message)
        return Response({'message': str(bot_response)})

