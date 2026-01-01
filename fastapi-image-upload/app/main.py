from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io

app = FastAPI(title="Image Upload API")

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image")

    image_bytes = await file.read()

    try:
        image = Image.open(io.BytesIO(image_bytes))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    width, height = image.size
    format = image.format

    return {
        "width": width,
        "height": height,
        "format": format
    }
