from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model


def init_openai_model(api_key, model_name="gpt-4o-mini", temperature=0.1):

    model = ChatOpenAI(model=model_name,
                       openai_api_key=api_key,
                       temperature=temperature,
                       openai_api_base="https://api.aigc369.com/v1")
    return model
    
def init_ds_model(api_key, model_name="deepseek-chat"):

    model = init_chat_model(model=model_name,
                            model_provider="deepseek",
                            api_key=api_key,
                            base_url="https://api.deepseek.com")
    return model