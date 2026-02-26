from gpt4all import GPT4All
import sympy as sp

model = GPT4All("model/ggml-model.bin")

def think(text):

    try:

        result = sp.sympify(text)

        return str(result)

    except:

        response = model.generate(text)

        return response