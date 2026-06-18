import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Trouve automatiquement le chemin du dossier où se trouve WebApp.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("index.html")

# --- ROUTES DE TÉLÉCHARGEMENT COHÉRENTES AVEC TES DOSSIERS ---

@app.route("/downloads/Win")
def WinDownload():
    # En se basant sur tes dossiers visibles sur ta capture : downloads/MyDat_Win/MyDat_Win.zip
    dossier_win = os.path.join(BASE_DIR, "downloads", "MyDat_Win")
    return send_from_directory(dossier_win, "MyDat_Win.zip", as_attachment=True)

@app.route("/downloads/Linux")
def LinuxDownload():
    # Dossier : downloads/MyDat_Linux/MyDat_Linux.zip (à vérifier s'il s'agit d'un .zip ou .tar.gz)
    dossier_linux = os.path.join(BASE_DIR, "downloads", "MyDat_Linux")
    return send_from_directory(dossier_linux, "MyDat_Linux.zip", as_attachment=True)

@app.route("/downloads/IntelMac")
def IntelMacDownload():
    # Dossier : downloads/MyDat_IntelMac/
    dossier_mac = os.path.join(BASE_DIR, "downloads", "MyDat_IntelMac")
    return send_from_directory(dossier_mac, "MyDat_IntelMac.zip", as_attachment=True)

@app.route("/downloads/AppleSiliconMac")
def AppleSiliconMacDownload():
    # Dossier : downloads/MyDat_AppleSiliconMac/
    dossier_mac = os.path.join(BASE_DIR, "downloads", "MyDat_AppleSiliconMac")
    return send_from_directory(dossier_mac, "MyDat_AppleSiliconMac.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")