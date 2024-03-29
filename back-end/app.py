from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fornecedores.sqlite'
db = SQLAlchemy(app)

# Modelo Fornecedor
class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    custo_por_kwh = db.Column(db.Float, nullable=False)
    limite_minimo_kwh = db.Column(db.Integer, nullable=False)
    num_total_clientes = db.Column(db.Integer, nullable=False)
    avaliacao_media = db.Column(db.Float, nullable=False)

# Rota para buscar fornecedores
@app.route('/escolher_fornecedor', methods=['POST'])
def escolher_fornecedor():
    try:
        dados_usuario = request.get_json()
        consumo_usuario = dados_usuario.get('consumo_mensal_kwh', 0)

        fornecedores_disponiveis = Fornecedor.query.filter(Fornecedor.limite_minimo_kwh < consumo_usuario).all()

        resultado_json = [
            {
                'nome': fornecedor.nome,
                'estado': fornecedor.estado,
                'custo_por_kwh': fornecedor.custo_por_kwh,
                'limite_minimo_kwh': fornecedor.limite_minimo_kwh,
                'num_total_clientes': fornecedor.num_total_clientes,
                'avaliacao_media': fornecedor.avaliacao_media
            } for fornecedor in fornecedores_disponiveis
        ]

        return jsonify(resultado_json)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
