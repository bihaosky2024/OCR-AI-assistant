from init_model import init_openai_model

from langchain_core.messages import HumanMessage
import base64

# 读取图像并编码为 Base64
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def ocr_red_box(image_path, api_key):
    image_data = encode_image(image_path)

    llm = init_openai_model(api_key, model_name="gpt-4o")
    message = HumanMessage(
        content=[
            {"type": "text", "text": "extract text in the red box only in this image, do not output any other information. Follow the format of text in the image, For example, keep the end of line, punctuation marks, and capitalization etc."},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ],
    )
    response = llm.invoke([message])
    
    return response.content



