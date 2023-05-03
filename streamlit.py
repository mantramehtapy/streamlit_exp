import gradio as gr
import os
from langchain.llms import Cohere,OpenAI
os.environ["COHERE_API_KEY"] = "3vwcW4Gu0m5XWaT5bx4PBJ8IiQ5rT11rSsMijTBu"
llm = Cohere(model="command-nightly",temperature=0.5)

box = gr.Blocks()

def fake(textbox):
  
  foo=f"""
  instructions: You are intelligent Generative model who are good in check the foul language.
  IF you found any violence or any slang languate kindly set response as No.
  Otherwise if you are able to found normal text kindly response with yes.
  context:{textbox}
  response:
  """
  out = llm(foo)
  return out

with box:
  textbox = gr.Textbox("enter")
  button = gr.Button("press me")
  button.click(fn=fake, inputs=[textbox],outputs=[gr.Label()])

box.launch(share = True)