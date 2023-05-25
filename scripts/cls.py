import modules.scripts as scripts
import gradio as gr
import os

class CLS(scripts.Script):

    def title(self):
        return "Clear Screen"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        if is_img2img == True:
            return None

        reload_button = gr.Button('🆑', elem_id='cls_btn')
            
        def clear_console():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        reload_button.click(fn=clear_console)
        return None