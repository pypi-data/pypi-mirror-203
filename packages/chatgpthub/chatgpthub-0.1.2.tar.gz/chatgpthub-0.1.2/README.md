<div align="center">
<h2>
     ChatGptHub: Gpt Chatbot Library with LangChain Support 
</h2>
<div>
    <a href="https://pepy.tech/project/chatgpthub"><img src="https://pepy.tech/badge/chatgpthub" alt="downloads"></a>
    <a href="https://badge.fury.io/py/chatgpthub"><img src="https://badge.fury.io/py/chatgpthub.svg" alt="pypi version"></a>
</div>
</div>

This repo is a implementation of the ChatGPT Models with [LangChain](https://github.com/hwchase17/langchain) support.

### Installation
```bash
pip install chatgpthub
```

### Usage
```python
from chatgpthub import ChatGptHubDemo

# translate chatgpt model

demo = ChatGptHubDemo(
    openai_key="openai_key",
    promptlayer_key="promptlayer_key", #optional
)

# translate chatgpt model

demo.translate(
    model_name = "gpt-3.5-turbo",
    input_language = "English",
    output_language = "Turkish",
    text = "Hello, how are you?",
    temperature = 0.0,
)

# promptlayer chatgpt model

demo.promptlayer(
    model_name = "gpt-3.5-turbo",
    text = "Hello, how are you?",
    temperature = 0.0,
)

# custom template chatgpt model

template = "You are a helpful assistant that python to c++ and you are asked to translate the following text: {text}"
text = "print('Hello, world!')"
output = demo.custom_template(
    model_name="gpt-3.5-turbo",
    template=template,
    input_variables="text",
    text=text,
    temperature=0.0,
)
```
