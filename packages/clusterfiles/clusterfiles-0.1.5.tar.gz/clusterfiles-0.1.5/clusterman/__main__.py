from clusterman.cli.app import create_app

app = create_app()

with app.app_context():
    app.cli()
