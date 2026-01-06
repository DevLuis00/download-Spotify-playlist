# Descargador de Playlists de Spotify

Script para descargar playlists de Spotify usando spotdl.

## Instalación

### Linux (Fedora)

bash
# Instalar Python 3.12
sudo dnf install python3.12 python3.12-pip -y

# Crear entorno virtual
cd ~/Documents/playlist
python3.12 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar spotdl
pip install spotdl

### Windows

cmd
# Descargar e instalar Python 3.12 desde python.org

# Crear entorno virtual
cd Documents\playlist
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar spotdl
pip install spotdl

## Configurar VS Code

1. Ctrl + Shift + P
2. Python: Select Interpreter
3. Seleccionar `./venv/bin/python` (Linux) o `.\venv\Scripts\python.exe` (Windows)

## Ejecutar

**Antes de presionar F5:**

Linux:
## bash
source ~/venv-spotdl/bin/activate


Windows:
## cmd
venv\Scripts\activate


Luego presiona F5 o ejecuta:
## bash
python playlis.py


## Notas

- Las canciones se guardan en `~/Music/Playlists` (Linux) o `%USERPROFILE%\Music\Playlists` (Windows)
- Debes activar el entorno virtual cada vez que abras una nueva terminal
- Requiere Python 3.12 (no funciona con Python 3.14)