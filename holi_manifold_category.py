from manim import *
import numpy as np

class HoliManifoldCategory(ThreeDScene):
    def construct(self):

        # --------------------------------
        # 1️⃣ 3D Geometry Section
        # --------------------------------
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        torus = Torus(major_radius=2, minor_radius=0.7)
        torus.set_fill_by_checkerboard(RED, ORANGE, opacity=0.8)

        self.play(FadeIn(torus), run_time=2)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(3)

        surface = Surface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(40, 40),
        )

        surface.set_fill_by_checkerboard(
            RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE,
            opacity=0.85
        )

        self.play(Transform(torus, surface), run_time=4)
        self.wait(2)

        self.play(FadeOut(torus), run_time=2)
        self.stop_ambient_camera_rotation()

        # Reset to flat 2D camera
        self.move_camera(phi=0, theta=0)
        self.wait(1)

        # --------------------------------
        # 2️⃣ Category Visualization
        # --------------------------------

        title = Tex(r"\textbf{Category of Smooth Manifolds}")
        title.to_edge(UP)

        M = Tex(r"$M$")
        N = Tex(r"$N$")
        f = Tex(r"$f : M \to N$")

        M.shift(LEFT * 3)
        N.shift(RIGHT * 3)

        arrow = Arrow(M.get_right(), N.get_left())
        f.next_to(arrow, UP)

        diagram = VGroup(M, N, arrow, f)

        self.add_fixed_in_frame_mobjects(title, diagram)

        self.play(Write(title))
        self.play(FadeIn(M), FadeIn(N))
        self.play(GrowArrow(arrow), Write(f))
        self.wait(2)

        # --------------------------------
        # 3️⃣ Functor
        # --------------------------------

        functor = Tex(r"$F : \mathbf{Man} \to \mathbf{Top}$")
        functor.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(functor)
        self.play(Write(functor))
        self.wait(2)

        # --------------------------------
        # 4️⃣ Manifold Properties
        # --------------------------------

        properties = Tex(
            r"\text{Locally Euclidean} \\"
            r"\text{Hausdorff} \\"
            r"\text{Second Countable}"
        )

        properties.scale(0.9)
        properties.next_to(title, DOWN)

        self.add_fixed_in_frame_mobjects(properties)
        self.play(FadeIn(properties))
        self.wait(3)

        # --------------------------------
        # 5️⃣ Final Message
        # --------------------------------

        final_text = Tex(
            r"\textbf{Happy Holi --- Across All Categories}"
        )
        final_text.set_color_by_gradient(
            RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE
        )
        final_text.scale(1.2)
        final_text.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(final_text)
        self.play(FadeIn(final_text))
        self.wait(4)
