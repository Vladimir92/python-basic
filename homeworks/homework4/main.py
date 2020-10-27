from app import app

app.config.update(
    DEBUG=True  # get debug info even on browser page
)

if __name__ == '__main__':
    app.run(debug=True)