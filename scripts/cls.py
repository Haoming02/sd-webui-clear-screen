from modules.script_callbacks import on_ui_settings, on_script_unloaded
from modules.ui_components import ToolButton
from modules.shared import OptionInfo, opts
from modules import scripts
import os


def _clear_console():
    os.system("cls" if os.name == "nt" else "clear")


class CLS(scripts.Script):

    def title(self):
        return "Clear Screen"

    def show(self, is_img2img):
        return None if is_img2img else scripts.AlwaysVisible

    def ui(self, is_img2img):
        if is_img2img:
            return None

        reload_button = ToolButton("🆑", elem_id="cls_btn", tooltip="Clear Console")
        reload_button.click(fn=_clear_console, queue=False)


def on_cls_settings():
    opts.add_option(
        "cls_on_reload",
        OptionInfo(
            False,
            "Automatically triggers Clear Console on ReloadUI",
            section=("system", "System"),
            category_id="system",
        ),
    )


def auto_clear_console():
    if getattr(opts, "cls_on_reload", False):
        _clear_console()


on_ui_settings(on_cls_settings)
on_script_unloaded(auto_clear_console)
