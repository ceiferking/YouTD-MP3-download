# Baixar Playlist do YouTube em MP3 com Python

## Pré-requisitos

### Python 3.8

- **O que é**: Linguagem de programação necessária para rodar o script.
- **Como instalar**: 
  - Acesse o [site oficial do Python](https://www.python.org/downloads/release/python-380/).
  - Baixe e instale a versão 3.8(3.8.10(versão exata de desenvolvimento na virtual lenv))

### ffmpeg

- **O que é**: Ferramenta necessária para converter arquivos de áudio para MP3.
- **Como instalar**:

  #### Windows
  - Baixe o `ffmpeg` [aqui](https://ffmpeg.org/download.html).
  - Extraia os arquivos e adicione o caminho da pasta `bin` ao PATH do sistema.

  #### macOS
  - **Instale o Homebrew** (se ainda não tiver) com o comando:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  - **Instale o `ffmpeg`** com o Homebrew:
    ```sh
    brew install ffmpeg
    ```

  #### Linux
  - **Use o gerenciador de pacotes** da sua distribuição. No Ubuntu, por exemplo, use:
    ```sh
    sudo apt-get install ffmpeg
    ```

## Configurando o Projeto

### Arquivo `requirements.txt`

- **O que é**: Arquivo que lista as dependências do projeto.
- **O que fazer**: Certifique-se de que o arquivo `requirements.txt` já está incluído no projeto.

## Instalando as Dependências

- **O que fazer**: Instalar as bibliotecas necessárias listadas no `requirements.txt`.
- **Passos**:
  - Abra o terminal ou prompt de comando.
  - Navegue até a pasta onde estão os arquivos do projeto.
  - Execute o comando `pip install -r requirements.txt` para instalar todas as dependências.

## Executando o Script

- **O que fazer**: Rodar o script para baixar e converter a playlist.
- **Passos**:
  - Abra o terminal ou prompt de comando na pasta onde o script está localizado.
  - Execute o script com `python appmp3.py`.
  - Insira o link da playlist do YouTube quando solicitado.

## Conclusão

E é isso! Com esses passos, você vai conseguir baixar qualquer playlist do YouTube em formato MP3 usando Python e `yt-dlp`. Se surgir qualquer dúvida ou problema, sinta-se à vontade para perguntar!
