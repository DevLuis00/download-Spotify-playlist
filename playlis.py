import os

playlist_url = input("Playlist URL:")

output_folder = os.path.expanduser("~/Music/Prueba")
os.makedirs(output_folder, exist_ok=True)

command = f'spotdl "{playlist_url}" --output "{output_folder}"' 
os.system(command)

