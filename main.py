import streamlit as st
from backend import ocr_assitant
from utils import save_temp_file


st.title("🖊️ OCR文字识别小助手")
st.markdown("##### 基于通义千问视觉模型的AI小助手：\n##### 输入图片，并使用红色方框标记出需要识别的文字区域。")

with st.sidebar:
    api_key = st.text_input("请输入通义千问 API密钥：", type="password")
    st.markdown("[获取通义千问 API密钥](https://bailian.console.aliyun.com/)")


uploaded_file = st.file_uploader("上传你的图片（使用红色方框标记出需要识别的文字区域）：", type=["png", "jpg", "jpeg"])
if not uploaded_file:
    st.stop()

temp_file_path = "temp"
save_temp_file(temp_file_path, uploaded_file)

option = st.selectbox("请选择需要文字识别的区域：", ["全图识别", "自定义识别（红色矩形框标记）"], index=0)
submit = st.button("开始识别")
if submit:
    if not api_key:
        st.info("请先输入通义千问 API密钥")
        st.stop()
    else:
        with st.spinner("正在识别..."):
            result = ocr_assitant(temp_file_path, api_key, red_box=(option == "自定义识别（红色矩形框标记）"))
            st.success("识别结果：")
            st.write(result)
