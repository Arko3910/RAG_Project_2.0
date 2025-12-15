from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from rag.pipeline import run_rag

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session, _ = ChatSession.objects.get_or_create(user=request.user)
        ChatMessage.objects.create(session=session, role="user", content=request.data["message"])
        reply = run_rag(request.data["message"])
        ChatMessage.objects.create(session=session, role="assistant", content=reply)
        return Response({"response": reply})
