from manim import *
from .rst_mobject import RstMobject


__all__ = ["AnimationDescription"]


class AnimationDescription(Group):
    def __init__(
        self,
        mobject_to_animate: Mobject,
        animation: Animation,
        title: str | None = None,
        description: str | None = None,
        rec_config: dict | None = None
    ):
        super().__init__()
        self.mobject_to_animate = mobject_to_animate
        self.animation = animation
        self.title = animation.__class__.__name__ if title is None else title
        self.description = animation.__doc__ if description is None else description
        examples_idx = self.description.find("Examples")
        if examples_idx != -1:
            self.description = self.description[:examples_idx]
        self.rec_config = rec_config or {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "fill_color": BLACK,
            "fill_opacity": 0.5,
            "buff": 0.2,
            "corner_radius": 0.2
        }
        self.title_mobject = Tex(f"\\textbf{{{self.title}}}", font_size=36)
        self.description_mobject = RstMobject(self.description, font_size=24)
        self.add(self.title_mobject, self.mobject_to_animate, self.description_mobject)
        self.arrange(DOWN, buff=0.5)
        self.add(SurroundingRectangle(self, **self.rec_config))
    
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
    
    def set_mobject_and_animation(
        self,
        mobject_to_animate: Mobject,
        animation: Animation,
        description: str | None = None,
        title: str | None = None
    ):
        self[1].become(mobject_to_animate)
        self.set_description(animation.__doc__ if description is None else description)
        self.set_title(animation.__class__.__name__ if title is None else title)
        self.animation = animation
        return self
    
    def set_animation(self, animation: Animation, description: str | None = None, title: str | None = None):
        self.set_mobject_and_animation(self.mobject_to_animate, animation, description, title)
        return self
    
    def set_mobject(self, mobject: Mobject, description: str | None = None, title: str | None = None):
        self.set_mobject_and_animation(mobject, self.animation, description, title)
        return self
    
    def play_animation(self, scene: Scene, run_time: float | None = 1, **kwargs):
        if run_time is not None:
            kwargs["run_time"] = run_time
        scene.play(self.animation, **kwargs)
        return self
