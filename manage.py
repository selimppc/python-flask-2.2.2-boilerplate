from app import create_app

app = create_app()


@app.route('/health', methods=['GET'])
def health():
    return 'Running!'


if __name__ == '__main__':
    app.run()
