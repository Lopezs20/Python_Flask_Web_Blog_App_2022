from website import create_app

# run the Flask application from this main file
# turn off debug for production
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)