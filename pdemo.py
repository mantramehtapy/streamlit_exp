import gradio as gr
import pandas as pd

box = gr.Blocks()

def insert(upload_csv):
    df = pd.DataFrame(upload_csv)
    return df

with box:
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["image", "video"], file_count="multiple")
    upload_button.upload(upload_button,df)
    button = gr.Button("press me") 
    button.click(fn=insert, inputs=[upload_csv],outputs=[gr.Dataframe()])
box.launch(share=True)