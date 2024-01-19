function buscarFornecedores() {
  const consumoMensal = document.getElementById('consumoInput').value;

  fetch('http://localhost:5000/escolher_fornecedor', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ consumo_mensal_kwh: consumoMensal }),
  })
    .then(response => response.json())
    .then(data => exibirResultado(data))  // Corrigir aqui para acessar diretamente data
    .catch(error => console.error('Erro na requisição:', error));
}

function exibirResultado(fornecedores) {
  const resultadoDiv = document.getElementById('resultado');
  resultadoDiv.innerHTML = '<h2>Fornecedores Disponíveis:</h2>';

  fornecedores.forEach(fornecedor => {
    resultadoDiv.innerHTML += `
      <div class="fornecedor-card">
        <h3>${fornecedor.nome}</h3>
        <p>Estado: ${fornecedor.estado}</p>
        <p>Custo por kWh: R$${fornecedor.custo_por_kwh}</p>
        <p>Limite Mínimo de kWh: ${fornecedor.limite_minimo_kwh}</p>
        <p>Número Total de Clientes: ${fornecedor.num_total_clientes}</p>
        <p>Avaliação Média: ${fornecedor.avaliacao_media}</p>
      </div>
    `;
  });
}
document.getElementById('seuBotao').addEventListener('click', buscarFornecedores);
