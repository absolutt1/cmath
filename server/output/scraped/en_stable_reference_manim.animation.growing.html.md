# growing[¶](https://docs.manim.community/en/stable/reference/<#module-manim.animation.growing> "Link to this heading")
Animations that introduce mobjects to scene by growing them from points.
Example: Growing [¶](https://docs.manim.community/en/stable/reference/<#growing>)
```
frommanimimport *
classGrowing(Scene):
  defconstruct(self):
    square = Square()
    circle = Circle()
    triangle = Triangle()
    arrow = Arrow(LEFT, RIGHT)
    star = Star()
    VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
    VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)
    self.play(GrowFromPoint(square, ORIGIN))
    self.play(GrowFromCenter(circle))
    self.play(GrowFromEdge(triangle, DOWN))
    self.play(GrowArrow(arrow))
    self.play(SpinInFromNothing(star))

```
Copy to clipboard
Make interactive
Classes
`[GrowArrow`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowArrow.html#manim.animation.growing.GrowArrow> "manim.animation.growing.GrowArrow") | Introduce an `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow") by growing it from its start toward its tip.  
---|---  
`[GrowFromCenter`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter> "manim.animation.growing.GrowFromCenter") | Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") by growing it from its center.  
`[GrowFromEdge`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromEdge.html#manim.animation.growing.GrowFromEdge> "manim.animation.growing.GrowFromEdge") | Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") by growing it from one of its bounding box edges.  
`[GrowFromPoint`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint> "manim.animation.growing.GrowFromPoint") | Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") by growing it from a point.  
`[SpinInFromNothing`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.SpinInFromNothing.html#manim.animation.growing.SpinInFromNothing> "manim.animation.growing.SpinInFromNothing") | Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") spinning and growing it from its center.  
[ Next GrowArrow ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowArrow.html>) [ Previous FadeOut ](https://docs.manim.community/en/stable/reference/<manim.animation.fading.FadeOut.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
