a de Publicação: Projetos Web Inetz

Olá, aluno! Este projeto utiliza um fluxo de **Integração Contínua (CI/CD)**. Ao enviar seu código para o GitHub, ele será publicado automaticamente no servidor da Inetz.

## 📂 Sua URL de Acesso
Com a nova organização por categorias, seu projeto front-end estará disponível em:
`https://lab.inetz.com.br/projetos/web/[seu-RA]/turing`

---

## 🛠️ Configuração do GitHub Actions

Crie o arquivo `.github/workflows/main.yml` no seu repositório e cole o conteúdo abaixo:

```yaml
name: Deploy para Inetz

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Código
        uses: actions/checkout@v4

      - name: Publicar Projeto
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ubuntu
          key: ${{ secrets.key_alunos }}
          source: "."
          target: "/var/inetpub/wwwroot/projetos/web/${{ secrets.ALUNO_RA }}/turing"a de Publicação: Ecossistema de Projetos Inetz
Olá, aluno! Bem-vindo ao laboratório de desenvolvimento da Inetz. Aqui, seu aprendizado vai além do código: você utilizará um fluxo profissional de Integração e Entrega Contínua (CI/CD).

💡 O Conceito de Integração
Neste ambiente, o seu código percorre um caminho automatizado e profissional:

GitHub: É a sua mesa de trabalho onde você versiona e organiza seu código.

GitHub Actions: É o "robô" de transporte. Sempre que você faz um push na branch main, ele é acionado automaticamente para processar seu deploy.

Servidor Inetz: É o destino final, onde seu projeto ganha vida e fica disponível para a internet através do domínio lab.inetz.com.br.

📂 Estrutura de URLs e Pastas
Sua URL oficial é organizada pelo seu RA (Registro Acadêmico). Cada disciplina ou atividade será uma subpasta dentro do seu espaço exclusivo:

Raiz do seu espaço: https://lab.inetz.com.br/projetos/[seu-RA]

Projeto Turing (Front-end): https://lab.inetz.com.br/projetos/[seu-RA]/turing

Projeto Back-end (Node.js/Express): https://lab.inetz.com.br/projetos/[seu-RA]/back-end

Projeto de IA (Python/Prompts): https://lab.inetz.com.br/projetos/[seu-RA]/ia

🛠️ Configuração do GitHub Actions
Para ativar a publicação automática, você deve criar um arquivo no seu repositório no caminho .github/workflows/main.yml e colar o código abaixo exatamente como está:

name: Deploy para Inetz

on:
push:
branches: [ main ]

jobs:
deploy:
runs-on: ubuntu-latest
steps:
- name: Checkout Código
uses: actions/checkout@v4

  - name: Publicar Projeto
    uses: appleboy/scp-action@v0.1.7
    with:
      host: ${{ secrets.SSH_HOST }}
      username: ubuntu
      key: ${{ secrets.SSH_KEY }}
      source: "."
      target: "/var/inetpub/wwwroot/projetos/${{ secrets.ALUNO_RA }}/turing"
🔑 Como configurar as Variáveis (Secrets)
Para que o GitHub consiga conversar com o servidor da Inetz, você precisa cadastrar as credenciais de acesso (Secrets). Siga estes passos:

No seu repositório do GitHub, clique na aba Settings (Configurações) na barra superior.

No menu lateral esquerdo, localize a seção Security e clique em Secrets and variables > Actions.

Clique no botão verde New repository secret.

Você deve criar três segredos, preenchendo o nome e o valor conforme abaixo:

SSH_HOST: O endereço IP ou domínio do servidor fornecido pelo professor.

SSH_KEY: Abra o arquivo key_alunos, copie TODO o texto da chave privada e cole aqui.

ALUNO_RA: Digite apenas os números do seu RA (Ex: 00001106610611).

Importante: Clique em Add secret para salvar cada uma delas individualmente.

🎓 Identidade Estudantil e Projetos Multidisciplinares
Este ecossistema foi desenhado para integrar todas as suas aulas. O seu RA é a sua chave de acesso:

Seu RA: 00001106610611

Seu E-mail Institucional: 00001106610611SP@al.educacao.sp.gov.br

Os projetos multidisciplinares unirão seu conhecimento de Front-end, Back-end e IA. Tudo o que você produzir ficará centralizado na sua pasta de projetos, criando um portfólio real de desenvolvedor.

A Palavra é Integração.
Foque no código, aprenda a lógica e deixe que a automação cuide da infraestrutura. Bons estudos!

