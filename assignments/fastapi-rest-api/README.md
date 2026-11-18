# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST com FastAPI para gerenciar tarefas, praticando rotas HTTP, validação de dados e operações CRUD.

## 📝 Tarefas

### 🛠️ Criar o Aplicativo e Listar Tarefas

#### Descrição
Configure a aplicação FastAPI e implemente uma rota para consultar as tarefas armazenadas. Renomeie o arquivo inicial para `main.py`, instale `fastapi` e `uvicorn` e inicie o servidor com `uvicorn main:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma instância FastAPI chamada `app`.
- Expor `GET /tasks`, retornando a lista de tarefas em formato JSON.
- Permitir testar a rota e visualizar a documentação interativa em `/docs`.

### 🛠️ Criar e Consultar Tarefas

#### Descrição
Use os modelos Pydantic fornecidos no código inicial para aceitar novas tarefas e consultar uma tarefa pelo identificador.

Exemplo de corpo para criar uma tarefa:

```json
{
  "title": "Study FastAPI",
  "completed": false
}
```

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com um identificador inteiro único.
- Validar os dados de entrada: `title` deve ter pelo menos um caractere e `completed` deve ser booleano, com valor padrão `false`.
- Responder à criação com status HTTP `201 Created` e os dados da tarefa criada.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa solicitada ou status HTTP `404 Not Found` quando ela não existir.

### 🛠️ Atualizar e Remover Tarefas

#### Descrição
Complete as operações restantes para que clientes possam atualizar ou remover tarefas já cadastradas.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e responder com status HTTP `204 No Content`.
- Responder com status HTTP `404 Not Found` quando uma atualização ou remoção solicitar um identificador inexistente.
- Testar as rotas de criação, consulta, atualização e remoção pela documentação interativa em `/docs`.
