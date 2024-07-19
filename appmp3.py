import yt_dlp

def download_playlist_mp3(playlist_url):
    # Definindo as opções para o yt-dlp
    ydl_opts = {
        # Seleciona o melhor formato de áudio disponível
        'format': 'bestaudio/best',
        # Pós-processadores para extrair áudio e convertê-lo para MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Utiliza o FFmpeg para extrair áudio
            'preferredcodec': 'mp3',      # Define o codec de áudio para MP3
            'preferredquality': '192',    # Define a qualidade do áudio para 192 kbps
        }],
        # Template para o nome do arquivo de saída, utilizando o título do vídeo
        'outtmpl': '%(title)s.%(ext)s',
        # Indica que é para baixar a playlist inteira, não apenas um vídeo
        'noplaylist': False,
    }

    # Cria uma instância do YoutubeDL com as opções definidas
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Inicia o download da playlist utilizando a URL fornecida
        ydl.download([playlist_url])

# URL da playlist que você deseja baixar
playlist_url = 'INSIRA_O_LINK_DA_PLAYLIST_AQUI'

# Chama a função para baixar a playlist
download_playlist_mp3(playlist_url)
