# 📖 Libaccess - Tradutor em Libras com Interface Gráfica

![Python 3.9](https://img.shields.io/badge/Python-3.9-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-yellow)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-red)

Bem-vindo ao **Libaccess**! Este é um projeto que utiliza tecnologias como **Tkinter**, **Pillow** e reconhecimento de áudio para criar uma interface gráfica capaz de converter texto e áudio em Libras (Língua Brasileira de Sinais). Este projeto visa promover inclusão e acessibilidade para pessoas com deficiência auditiva. 🎉

---
### 🛠 Funcionalidades
#### ✨ Reconhecimento de áudio: Converte áudio em texto usando a função de conversão de fala. 
#### ✨ Tradução para Libras: Mostra imagens correspondentes às letras do texto traduzido. 
#### ✨ Interface gráfica moderna: Design limpo e amigável, desenvolvido com Tkinter. 
#### ✨ Exibição de palavras em Libras: Espaçamento adequado entre palavras para melhor visualização. 
#### ✨ Modularidade: Fácil de integrar com novas funcionalidades.
---
### 🖥️ Como Funciona
#### O usuário grava um áudio clicando em um botão. 🎙️

#### O sistema converte o áudio em texto.

#### As letras são exibidas em Libras através de imagens. 🖼️

#### As palavras são organizadas com espaçamento entre elas para maior clareza.

---
### 🚀 Tecnologias Utilizadas
#### Python 🐍

#### Tkinter (Interface Gráfica)

#### Pillow (Manipulação de Imagens)

#### SpeechRecognition (Reconhecimento de Áudio)

#### OS Module (Gerenciamento de arquivos e caminhos)

---
## 🚀 Como Configurar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Crie um Ambiente Virtual (opcional, mas recomendado)
```bash
python -m venv venv
# Ative o ambiente:
# No Windows
venv\Scripts\activate
# No Mac/Linux
source venv/bin/activate
```
### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```
### 4. Configure a Estrutura de Arquivos
Certifique-se de que você possui as imagens de Libras para cada letra na pasta libras/, organizadas assim:
``` bash
libras/
│
├── a.png
├── b.png
├── c.png
...
```
▶️ Como Executar o Projeto
Execute o arquivo principal para iniciar o programa:

```bash
python interface.py
```
Se tudo estiver configurado corretamente, a interface gráfica será aberta e estará pronta para uso! 🎉

### 📂 Estrutura do Projeto
```bash
projeto/
│
├── main.py                # Funções principais do sistema
├── interface.py           # Interface gráfica
├── libras/                # Imagens correspondentes às letras
│   ├── a.png
│   ├── b.png
│   ├── ...
├── imagens/               # Outras imagens (logo, splash screen)
│   ├── logo.jpg
│   ├── fundo_boas_vindas.jpg
├── requirements.txt       # Bibliotecas necessárias
└── README.md              # Documentação do projeto
```
📝 Recursos Futuros
🔊 Adição de mais vozes e suporte a outros idiomas.

🤖 Automatização para busca de Libras online, caso imagens estejam faltando.

💻 Versão web do projeto para acessibilidade em qualquer navegador.

---
### 🛠️ Principais Arquivos
#### main.py: Contém as funções principais do projeto, como seleção de PDFs e reconhecimento de áudio para converter em libras.

#### interface.py: Gerencia a interface gráfica e a interação com o usuário.

#### libras/: Pasta com as imagens das letras em Libras.

---
### 🙌 Contribuições
Contribuições são sempre bem-vindas! Siga os passos abaixo:

Faça um fork deste repositório.

Crie uma branch para suas alterações: git checkout -b minha-feature.

Faça o commit das alterações: git commit -m "Minha feature maravilhosa".

Faça o push: git push origin minha-feature.

Abra um Pull Request.
--- 
### 📧 Contato
Se tiver dúvidas ou sugestões, entre em contato:

### E-mail: ddpessoall@gmail.com

### GitHub: deyv7
