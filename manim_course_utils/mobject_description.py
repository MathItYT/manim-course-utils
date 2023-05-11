from manim import *


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
        self.title = title or mobject.__class__.__name__
        self.title_mobject = Text(title, font_size=36, weight=BOLD)
        self.description_mobject = Text(self.description, font_size=24)
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
        self[2].become(Text(self.description, font_size=24))
        return self
    
    def set_title(self, title: str):
        self.title = title
        self[0].become(Text(title, font_size=36, weight=BOLD))
        return self
    
    def set_mobject(self, mobject: Mobject, description: str | None = None, title: str | None = None):
        self[1].become(mobject)
        self.set_description(mobject.__doc__ if description is None else description)
        self.set_title(title or mobject.__class__.__name__)
        return self
