# Projeto: Busca de Operadoras de Saúde

Este projeto é uma aplicação web que permite buscar operadoras de saúde utilizando um frontend Vue.js e um backend Flask.

## 📌 Tecnologias Utilizadas

- **Frontend:** Vue.js  
- **Backend:** Flask  
- **Banco de Dados:** JSON/SQL (dependendo da implementação)  
- **Estilização:** CSS puro (pode ser adaptado para Tailwind, Bootstrap, etc.)


## 🚀 Como Rodar o Projeto

### 🔧 Backend (Flask)
1. Acesse a pasta `backend` e crie um ambiente virtual:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
   O backend estará rodando em `http://127.0.0.1:5000/`.

### 🌐 Frontend (Vue.js)
1. Acesse a pasta `frontend` e instale as dependências:
   ```bash
   cd frontend
   npm install
   ```
2. Inicie o servidor Vue:
   ```bash
   npm run dev
   ```
   O frontend estará rodando em `http://localhost:5173/` (ou outra porta definida).

## 🛠 Endpoints da API

- **`GET /buscar?q={termo}`** → Retorna uma lista de operadoras filtradas pelo termo de busca.

Exemplo de resposta:
```json
[
    
    {
        "Bairro": "BARRA DA TIJUCA",
        "CEP": 22631455,
        "CNPJ": 23532987000190,
        "Cargo_Representante": "ADMINISTRADOR",
        "Cidade": "Rio de Janeiro",
        "Complemento": "BLOCO 01 - SALA 1701",
        "DDD": 21.0,
        "Data_Registro_ANS": "2016-01-11",
        "Endereco_eletronico": "LEONARDO@UNIMEDICASAUDE.COM",
        "Fax": NaN,
        "Logradouro": "RUA AFONSO ARINOS DE MELO FRANCO",
        "Modalidade": "Administradora de Benefícios",
        "Nome_Fantasia": NaN,
        "Numero": "222",
        "Razao_Social": "VECTORIAL ADMINISTRADORA DE BENEFÍCIOS LTDA",
        "Regiao_de_Comercializacao": 6.0,
        "Registro_ANS": 420018,
        "Representante": "MARCELO SARMENTO DE CASTRO",
        "Telefone": 35531692.0,
        "UF": "RJ"
    },
]
```

## 📝 Melhorias Futuras
- Implementação de paginação na busca
- Adicionar testes automatizados
- Melhorar a interface com frameworks de UI (Bootstrap, Tailwind, etc.)

---
📌 **Autor:** Seu Nome  
📅 **Última atualização:** `31/03/2025`

