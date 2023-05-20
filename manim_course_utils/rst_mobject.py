from manim import *
from manim.utils.tex_file_writing import *
from uuid import uuid4
from subprocess import Popen


__all__ = ["RstMobject"]


def create_rst_file(rst: str):
    file_name = f"{uuid4()}.rst"
    with open(file_name, "w") as f:
        f.write(rst)
    return file_name

def convert_rst_file_to_latex(file_name: str):
    Popen(f"rst2latex.py {file_name} {file_name.replace('.rst', '.tex')}").wait()
    return file_name.replace(".rst", ".tex")

def convert_latex_to_tex_str(file_name: str):
    with open(file_name, "r") as f:
        return f.read()

def rst_to_tex_str(rst: str):
    latex_file = convert_rst_file_to_latex(create_rst_file(rst))
    return convert_latex_to_tex_str(latex_file), latex_file

def remove_everything(prefix):
    for file_name in Path(".").glob(f"{prefix}*"):
        file_name.unlink()


class EmptyTexTemplate(TexTemplate):
    def __init__(self):
        super().__init__()

    def _rebuild(self):
        return TexTemplate.default_placeholder_text


class RstMobject(MathTex):
    def __init__(self, rst: str, **kwargs):
        tex_str, latex_file = rst_to_tex_str(rst)
        super().__init__(tex_str, tex_template=EmptyTexTemplate(), **kwargs)
        remove_everything(latex_file.replace(".tex", ""))