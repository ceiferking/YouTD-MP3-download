import yt_dlp
from concurrent.futures import ThreadPoolExecutor

# Função para baixar e converter um vídeo da playlist
def download_video(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Função principal para baixar a playlist
def download_playlist(playlist_url):
    ydl_opts = {
        'extract_flat': True,  # Apenas lista os vídeos sem baixar
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
    
    # Extraindo URLs dos vídeos da playlist
    video_urls = [entry['url'] for entry in result['entries']]

    # Usando ThreadPoolExecutor para processar vídeos em paralelo
    with ThreadPoolExecutor() as executor:
        executor.map(download_video, video_urls)

if __name__ == "__main__":
    playlist_url = input('Insira o link da playlist: ')
    download_playlist(playlist_url)
