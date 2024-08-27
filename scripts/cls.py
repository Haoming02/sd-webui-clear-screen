from modules.script_callbacks import on_ui_settings, on_script_unloaded
from modules.shared import OptionInfo, opts
from modules import scripts
import gradio as gr
import os


class CLS(scripts.Script):

    def title(self):
        return "Clear Screen"

    def show(self, is_img2img):
        return None if is_img2img else scripts.AlwaysVisible

    def ui(self, is_img2img):
        if is_img2img is True:
            return None

        def clear_console():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        reload_button = gr.Button("🆑", elem_id="cls_btn")
        reload_button.click(fn=clear_console)
        return None


def ui_settings():
    opts.add_option(
        "cls_on_reload",
        OptionInfo(
            False,
            "Automatically Clear Screen on ReloadUI",
            section=("system", "System"),
        ),
    )


def auto_clear_console():
    if getattr(opts, "cls_on_reload", False):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


on_ui_settings(ui_settings)
on_script_unloaded(auto_clear_console)
