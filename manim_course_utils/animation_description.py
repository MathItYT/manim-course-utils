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
        rec_config: dict | None = None,
        height: float | None = None,
        buff: float = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.mobject_to_animate = mobject_to_animate
        self.animation = animation
        self.title = animation.__class__.__name__ if title is None else title
        self.description = animation.__doc__ if description is None else description
        examples_idx = self.description.find("Examples")
        if examples_idx != -1:
            self.description = self.description[:examples_idx]
        self.description = self.description.split("\n")
        for i in range(1, len(self.description)):
            self.description[i] = self.description[i].removeprefix(4 * " ")
        self.description = "\n".join(self.description)
        self.description.replace("~.", "")
        self.rec_config = {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "fill_color": BLACK,
            "fill_opacity": 0.5,
            "buff": 0.2,
            "corner_radius": 0.2
        } if rec_config is None else rec_config
        self.title_mobject = Tex(f"\\textbf{{{self.title}}}")
        self.description_mobject = RstMobject(
            self.description).scale_to_fit_height(5)
        self.add(self.title_mobject, self.mobject_to_animate,
                 self.description_mobject)
        buff = 0.5 if buff is None else buff
        self.arrange(DOWN, buff=buff)
        self.add_to_back(SurroundingRectangle(self, **self.rec_config))
        height = 7 if height is None else height
        self.scale_to_fit_height(height)

    def play_animation(self, scene: Scene, run_time: float | None = 1, **kwargs):
        if run_time is not None:
            kwargs["run_time"] = run_time
        scene.play(self.animation, **kwargs)
        return self
