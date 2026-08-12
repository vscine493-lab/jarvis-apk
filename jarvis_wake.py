import subprocess
import time
import re

WAKE = "jarvis"

SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "tiktok": "https://www.tiktok.com",
    "facebook": "https://www.facebook.com",
    "github": "https://github.com",
}

def ouvir():
    p = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )
    return p.stdout.strip().lower()

def abrir_site(texto):
    for nome, url in SITES.items():
        if nome in texto:
            subprocess.run([
                "am", "start",
                "-a", "android.intent.action.VIEW",
                "-d", url
            ])
            print("JARVIS: abrindo", nome)
            return True
    return False

print("JARVIS: modo de espera ativado.")
print("Diga JARVIS.")

while True:
    try:
        texto = ouvir()

        if not texto:
            continue

        print("Ouvi:", texto)

        if WAKE not in texto:
            continue

        comando = texto.split(WAKE, 1)[1].strip()

        if not comando:
            print("JARVIS: aguardando comando...")
            comando = ouvir()
            print("Comando:", comando)

        if not abrir_site(comando):
            print("JARVIS: comando não configurado.")

        print("JARVIS: modo de espera.")
        time.sleep(1)

    except KeyboardInterrupt:
        print("\nJARVIS encerrado.")
        break
    except Exception as e:
        print("Erro:", e)
        time.sleep(1)
