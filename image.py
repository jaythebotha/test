import os
import requests
import discord
from PIL import Image

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1130860000366047343/ah1cyP6z81VokXuQ3sQaMyxWcJRiuNy3QDZABV-HSQLb26KCNG7-uaXDpXWOPsEico8p"

def send_to_discord(file_path):
    with open(file_path, "rb") as f:
        image_data = f.read()
        response = requests.post(DISCORD_WEBHOOK_URL, files={"file": image_data})

    if response.status_code!= 204:
        print(f"Failed to send image to Discord: {response.text}")

def log_image(image_directory):
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_directory, filename)
            if os.path.isfile(image_path):
                send_to_discord(image_path)
                print(f"Sent image to Discord: {image_path}")
                os.remove(image_path)

if __name__ == "__main__":
    image_directory = "C:\\Users\\jared\\Downloads\\Dog-Piece-Assets\\Portgas-D.-Ace-replica-prop-one-piece-cosplay-by-blasters4masters10"
    log_image(image_directory)
