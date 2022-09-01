from website import create_app

app = create_app()

# this allows u to run the website only when you run the main.py file
if __name__ == "__main__":
    app.run(debug=True)