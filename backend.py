from openai import OpenAI
import base64

# 读取图像并编码为 Base64
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def ocr_assitant(image_path, api_key, red_box=False):

    image_data = encode_image(image_path)
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    prompt_ls = [
        "Extract text in this image, do not output any other information.",
        "Extract text in the red box only in this image, do not output any other information.",
    ]
    
    completion = client.chat.completions.create(
        model="qwen-vl-ocr",  
        messages=[{"role": "user","content": [
                {"type": "text", "text": prompt_ls[red_box]},
                {"type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                ]}]
        )
    
    return completion.choices[0].message.content 