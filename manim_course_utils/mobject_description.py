from manim import *
from .rst_mobject import RstMobject


__all__ = ["MobjectDescription"]


class MobjectDescription(Group):
    def __init__(
        self,
        mobject: Mobject,
        title: str | None = None,
        description: str | None = None,
        rec_config: dict | None = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.mobject = mobject
        self.description = mobject.__doc__ if description is None else description
        examples_idx = self.description.find("Examples")
        if examples_idx != -1:
            self.description = self.description[:examples_idx]
        self.title = mobject.__class__.__name__ or title
        self.title_mobject = Tex(f"\\textbf{{{title}}}", font_size=36)
        self.description_mobject = RstMobject(self.description, font_size=24)
        self.add(self.title_mobject, self.mobject, self.description_mobject)
        self.arrange(DOWN, buff=0.5)
        rec_config = rec_config or {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "fill_color": BLACK,
            "fill_opacity": 0.5,
            "buff": 0.2,
            "corner_radius": 0.2
        }
        self.add(SurroundingRectangle(self, **rec_config))
    
    def set_description(self, description: str):
        self.description = description
        examples_idx = self.description.find("Examples")
        if examples_idx != -1:
            self.description = self.description[:examples_idx]
        self[2].become(RstMobject(self.description, font_size=24))
        return self
    
    def set_title(self, title: str):
        self.title = title
        self[0].become(Tex(f"\\textbf{{{title}}}", font_size=36))
        return self
    
    def set_mobject(self, mobject: Mobject, description: str | None = None, title: str | None = None):
        self[1].become(mobject)
        self.set_description(mobject.__doc__ if description is None else description)
        self.set_title(mobject.__class__.__name__ or title)
        return self
