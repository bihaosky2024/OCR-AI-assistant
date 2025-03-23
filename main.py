import streamlit as st
from backend import ocr_red_box
from utils import save_temp_file


st.title("🖊️ OCR文字识别小助手")
st.markdown("##### 基于OpenAI GPT4o的AI小助手：\n##### 输入图片，并使用红色方框标记出需要识别的文字区域。")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")


uploaded_file = st.file_uploader("上传你的图片（使用红色方框标记出需要识别的文字区域）：", type=["png", "jpg", "jpeg"])
if not uploaded_file:
    st.stop()

temp_file_path = "temp"
save_temp_file(temp_file_path, uploaded_file)

submit = st.button("开始识别")
if submit:
    if not openai_api_key:
        st.info("请先输入OpenAI API密钥")
        st.stop()
    else:
        with st.spinner("正在识别..."):
            result = ocr_red_box(temp_file_path, openai_api_key)
            st.success("识别结果：")
            st.write(result)
