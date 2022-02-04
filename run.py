from flask import Flask

app = Flask(__name__)

@app.route("/nps")
def NPS():
    return ("<iframe title='first_charts2 - Histórico Chamados x Estatísticas Avaliações' width='1140' height='541.25' src='https://app.powerbi.com/reportEmbed?reportId=600c6eb9-e998-4301-b55a-28f4a8ee516d&autoAuth=true&ctid=b64427b3-01ab-49de-b497-36810b81f343&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D' frameborder='0' allowFullScreen='true'></iframe>")


@app.route("/")
def index():
    return ("<h1>Clinica São José</h1> <a href="https://cjs-nps.herokuapp.com/nps"><button>NPS</button></a>")

    
