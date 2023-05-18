from manim import TexTemplate


__all__ = ["MarkdownTexTemplate"]


class MarkdownTexTemplate(TexTemplate):
    def __init__(self):
        super().__init__(tex_compiler="lualatex", output_format=".pdf")
        self.add_to_preamble(r"\usepackage[fencedCode,hashEnumerators,hybrid,smartEllipses]{markdown}")
