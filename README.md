# AI Chatbot Backend

Django REST backend with JWT authentication, chat history, and FAISS-based RAG pipeline.

## Run locally
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Deploy
Compatible with Hugging Face Spaces + Supabase PostgreSQL.
