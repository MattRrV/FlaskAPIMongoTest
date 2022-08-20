# Perguntas
## 1) Você acha que este código está estruturado, legível e escalável?
# Não

## 2) O que você mudaria nos arquivos e na estrutura de pastas para melhorá-lo nesse sentido?
# Colocaria o MongoDB Client dentro das pastas src/infra/orm e colocaria o nome do arquivo como orm_define
# O api.run colocaria ele em um arquivo chamado wsgi na pasta raiz do projeto
# As rotas colocaria dentro das pastas src/controllers
# E chamaria os endpoints através de um http, dentro das pastas tests/http

## 3) Quanto a arquitetura API e sua conteinerização, liste as brechas de segurança que você identificou neste código? Como você as resolveria?
# Poderia colocar tokens jwt para validar o usuário

