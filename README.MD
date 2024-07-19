# Tutorial: Baixar Playlist do YouTube em MP3 com Python

Este tutorial irá guiá-lo através dos passos necessários para baixar uma playlist inteira do YouTube em formato MP3 usando Python e `yt-dlp` é um codigo simples para uso pessoal apenas.

Primeiro, certifique-se de ter o Python 3.8 instalado no seu sistema. Se você ainda não o tem, faça o download e instale a partir do site oficial: [python.org](https://www.python.org/downloads/release/python-380/).

Depois, instale o `yt-dlp`, uma ferramenta de linha de comando que permite baixar vídeos e áudios de sites como o YouTube. Abra o terminal ou prompt de comando e execute o comando para instalar o `yt-dlp`.

Você também precisará instalar o `ffmpeg`, que é necessário para converter os arquivos de áudio para MP3. Siga as instruções abaixo para instalar o `ffmpeg` no seu sistema:

- **Windows**: Baixe o `ffmpeg` [aqui](https://ffmpeg.org/download.html). Extraia os arquivos e adicione o caminho da pasta `bin` do `ffmpeg` ao seu PATH do sistema.

- **macOS**: Instale o Homebrew se ainda não o tiver com o comando apropriado para instalação. Depois, instale o `ffmpeg` usando o Homebrew.

- **Linux**: Use o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, use o comando para instalar o `ffmpeg`.

Agora, você deve criar um script Python para baixar e converter a playlist. Abra um editor de texto e cole o código fornecido em um novo arquivo. Salve o arquivo com a extensão `.py`, por exemplo, `baixar_playlist.py`.

Substitua o placeholder pelo link da playlist do YouTube que você deseja baixar.

Em seguida, crie um arquivo chamado `requirements.txt` na mesma pasta onde está o script Python e adicione a linha necessária para instalar as dependências.

No terminal ou prompt de comando, navegue até a pasta onde estão os arquivos e execute o comando para instalar as dependências a partir do `requirements.txt`.

Finalmente, para executar o script e baixar a playlist, abra o terminal ou prompt de comando na pasta onde você salvou o script e execute o comando para rodar o script.

O script irá baixar todos os vídeos da playlist e convertê-los para MP3, salvando-os na mesma pasta onde o script está localizado.

Seguindo os passos acima, você será capaz de baixar qualquer playlist do YouTube em formato MP3 usando Python e `yt-dlp`. Se tiver qualquer dúvida ou problema, sinta-se à vontade para buscar ajuda.
