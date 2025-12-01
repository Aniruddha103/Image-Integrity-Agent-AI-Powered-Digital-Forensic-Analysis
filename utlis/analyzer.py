import base64
from google import generativeai as genai
import numpy as np
from PIL import Image
import io

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    b64_img = base64.b64encode(image_bytes).decode()

    prompt = """
    You are an Image Forgery Detection Expert.
    Analyze the image for:
    - copy-move forgery
    - splicing
    - inpainting
    - resampling
    - metadata inconsistencies
    - noise-level anomalies

    Provide a structured explanation.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(
        [{"mime_type": "image/jpeg", "data": b64_img}, prompt]
    )

    return response.text
