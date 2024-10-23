from flask import render_template

def create_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/sorteio')
    def sorteio():
        return render_template('sorteio.html')

    @app.route('/tag')
    def tag():
        return render_template('tag.html')

    @app.route('/ajuda')
    def ajuda():
        return render_template('ajuda.html')

    @app.route('/planos')
    def planos():
        return render_template('planos.html')

    @app.route('/cadastro')
    def cadastro():
        return render_template('cadastro.html')
