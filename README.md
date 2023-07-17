
pip install -r requirements.txt

source venv/bin/activate

uvicorn main:app --host localhost --port 8000 --reload