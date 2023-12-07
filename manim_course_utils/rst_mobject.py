from manim import *
from subprocess import Popen
import os
import shutil


__all__ = ["RstMobject"]


class EmptyTexTemplate(TexTemplate):
    def __init__(self):
        super().__init__()

    def _rebuild(self):
        self.body = self.placeholder_text


def create_pandoc_folder():
    if not os.path.exists("pandoc"):
        os.mkdir("pandoc")


def write_rst_file(rst_content: str):
    file_name = os.path.join("pandoc", "temp.rst")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(rst_content)
    return file_name


def rst_to_tex(rst_content: str):
    create_pandoc_folder()
    file_name = write_rst_file(rst_content)
    tex_file_name = file_name.replace(".rst", ".tex")
    p = Popen(["pandoc", file_name, "-t", "latex",
              "--standalone", "-o", tex_file_name, file_name])
    p.wait()
    with open(tex_file_name, "r", encoding="utf-8") as f:
        tex_content = f.read()
    tex_content = tex_content.replace(
        "\documentclass[\n]{article}", "\documentclass[preview]{standalone}")
    return tex_content


def clean_up():
    shutil.rmtree("pandoc")


class RstMobject(Tex):
    def __init__(
        self,
        rst_string: str,
        arg_separator="",
        tex_environment=None,
        tex_template=EmptyTexTemplate(),
        **kwargs
    ):
        super().__init__(
            rst_to_tex(rst_string),
            arg_separator=arg_separator,
            tex_environment=tex_environment,
            tex_template=tex_template,
            **kwargs
        )
