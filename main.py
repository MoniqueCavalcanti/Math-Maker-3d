from flask import Flask, render_template, request
import unidecode

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index1():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = ['modelagem','modelagem 3d','m','impressao 3d','impressao', '3d','i','eletronica e robotica','robotica e eletronica','eletronica','robotica','e','r']
        palpite1= request.form.get("name").lower()
        palpite = unidecode.unidecode(palpite1)

        if search[0] == palpite:
            return render_template("Modelagem.html")
        elif search[1] == palpite:
            return render_template("Modelagem.html")
        elif search[2] == palpite:
            return render_template("Modelagem.html")
        elif search[3] == palpite:
            return render_template("Impressao3D.html")
        elif search[4] == palpite:
            return render_template("Impressao3D.html")
        elif search[5] == palpite:
            return render_template("Impressao3D.html")
        elif search[6] == palpite:
            return render_template("Impressao3D.html")
        elif search[7] == palpite:
            return render_template("robo_eletro.html")
        elif search[8] == palpite:
            return render_template("robo_eletro.html")
        elif search[9] == palpite:
            return render_template("robo_eletro.html")
        elif search[10] == palpite:
            return render_template("robo_eletro.html")
        elif search[11] == palpite:
            return render_template("robo_eletro.html")
        elif search[12] == palpite:
            return render_template("robo_eletro.html")
        else:
            return render_template("index.html")
@app.route('/area1', methods=["POST"])
def area1():
    return render_template("Modelagem.html")
@app.route('/area2', methods=["POST"])
def area2():
    return render_template("Impressao3D.html")
@app.route('/area3', methods=["POST"])
def area3():
    return render_template("robo_eletro.html")
@app.route('/clicar1', methods=["POST"])
def clicar1():
    return render_template("index.html")
@app.route('/clicar2', methods=["POST"])
def clicar2():
    return render_template("Modelagem.html")
@app.route('/clicar3', methods=["POST"])
def clicar3():
    return render_template("Impressao3D.html")
@app.route('/clicar4', methods=["POST"])
def clicar4():
    return render_template("robo_eletro.html")
@app.route('/clicar5', methods=["POST"])
def clicar5():
    return render_template("blog.html")
@app.route('/clicar6', methods=["POST"])
def clicar6():
    return render_template("historia.html")
@app.route('/clicar7', methods=["POST"])
def clicar7():
    return render_template("orcamento.html") 
@app.route('/orcamento', methods=["POST"])
def orcamento():
    return render_template("orcamento.html")
@app.route('/imagem', methods=["POST"])
def imagem():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
