from ultralytics import YOLO
import gradio as gr
from PIL import Image
import numpy as np

model = YOLO('runs/detect/train/weights/best.pt')

def detect(image):
    if image is None:
        return None
    results = model.predict(source=image, device='cpu')
    return Image.fromarray(results[0].plot())

app = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="numpy", label="上传图片"),
    outputs=gr.Image(type="pil", label="检测结果"),
    title="YOLOv8 实时检测 Web 应用",
    description="上传一张图片，AI 会自动识别图片里的物体并画框"
)

app.launch()