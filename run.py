from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<iframe title='first_charts2 - Histórico Chamados x Estatísticas Avaliações' width='1140' height='541.25' src='https://app.powerbi.com/reportEmbed?reportId=4e19597e-3470-4e3b-bd20-e0d1a852ab84&autoAuth=true&ctid=dfb66dc4-3f3c-492c-991d-727dbd1c89d4&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D' frameborder='0' allowFullScreen='true'></iframe>")
