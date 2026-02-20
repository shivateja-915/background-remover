from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from PIL import Image
import io

app = FastAPI()

# VERY IMPORTANT
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

@app.get("/")
def home():
 return {"message":"Backend Running"}

@app.post("/removebg")
async def remove_bg(file: UploadFile = File(...)):

 contents = await file.read()

 input_image = Image.open(io.BytesIO(contents))

 output = remove(input_image)

 buffer = io.BytesIO()

 output.save(buffer,"PNG")

 buffer.seek(0)

 return StreamingResponse(
 buffer,
 media_type="image/png"
 )