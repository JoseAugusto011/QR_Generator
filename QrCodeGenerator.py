import qrcode 
import PIL
import os
import requests
from PIL import Image


class QRCodeGenerator:
    def __init__(self, url):

        # verificar se url é válida

        
        
        try:
            response = requests.head(url, timeout=5)
            if response.status_code >= 400:
                raise ValueError(f"URL returned status code: {response.status_code}")
        except requests.RequestException as e:
            raise ValueError(f"Invalid URL or connection error: {e}")

        self.url = url
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate(self, filename="qrcode.png", folder="output"):
        """Generates a QR code image from the URL and saves it to a folder."""
        self.qr.add_data(self.url)
        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color="black", back_color="white")

        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, filename)
        img.save(file_path)
        return file_path

if __name__ == "__main__":

    url = "https://gemini.google.com/share/a02d6fb32325"
    qr = QRCodeGenerator(url)
    qr.generate()