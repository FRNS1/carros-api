from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='172.31.47.123', port=5000, debug=True)