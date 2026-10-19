from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        port=os.environ.get('DB_PORT', '5432'),
        dbname=os.environ.get('DB_NAME', 'hackathon'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASSWORD', 'secret123')
    )

@app.route('/')
def home():
    return "Привет! Это ответ от Python-бэкенда."

@app.route('/api/data')
def get_data():
    return jsonify({"status": "success", "message": "Nginx пробросил запрос!"})

@app.route('/api/users')
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "users": [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
