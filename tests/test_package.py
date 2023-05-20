from manim_course_utils import *
from manim import *


__all__ = ["test_mobject_description", "test_animation_description"]


def test_mobject_description():
    class SceneToShow(Scene):
        def construct(self):
            circ = Circle()
            desc = MobjectDescription(circ)
            ideal_title = "Circle"
            ideal_description = circ.__doc__
            examples_idx = ideal_description.find("Examples")
            if examples_idx != -1:
                ideal_description = ideal_description[:examples_idx]
            ideal_description = ideal_description.split("\n")
            for i in range(1, len(ideal_description)):
                ideal_description[i] = ideal_description[i].removeprefix(4 * " ")
            ideal_description = "\n".join(ideal_description)
            assert desc.title == ideal_title
            assert desc.description == ideal_description
            self.add(desc)
    with tempconfig({"preview": True}):
        SceneToShow().render()


def test_animation_description():
    class SceneToShow(Scene):
        def construct(self):
            anim = Create(Circle())
            desc = AnimationDescription(anim.mobject, anim)
            ideal_title = "Create"
            ideal_description = anim.__doc__
            examples_idx = ideal_description.find("Examples")
            if examples_idx != -1:
                ideal_description = ideal_description[:examples_idx]
            ideal_description = ideal_description.split("\n")
            for i in range(1, len(ideal_description)):
                ideal_description[i] = ideal_description[i].removeprefix(4 * " ")
            ideal_description = "\n".join(ideal_description)
            assert desc.title == ideal_title
            assert desc.description == ideal_description
            self.add(desc)
            desc.play_animation(self)
    
    with tempconfig({"preview": True}):
        SceneToShow().render()
