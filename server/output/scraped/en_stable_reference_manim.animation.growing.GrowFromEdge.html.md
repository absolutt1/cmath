# GrowFromEdge[¶](https://docs.manim.community/en/stable/reference/<#growfromedge> "Link to this heading")
Qualified name: `manim.animation.growing.GrowFromEdge`
_class_ GrowFromEdge(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/growing.html#GrowFromEdge>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromEdge> "Link to this definition")
    
Bases: `[GrowFromPoint`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint> "manim.animation.growing.GrowFromPoint")
Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") by growing it from one of its bounding box edges.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
  * **edge** (_np.ndarray_) – The direction to seek bounding box edge of mobject.
  * **point_color** (_str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples
Example: GrowFromEdgeExample [¶](https://docs.manim.community/en/stable/reference/<#growfromedgeexample>)
```
frommanimimport *
classGrowFromEdgeExample(Scene):
  defconstruct(self):
    squares = [Square() for _ in range(4)]
    VGroup(*squares).set_x(0).arrange(buff=1)
    self.play(GrowFromEdge(squares[0], DOWN))
    self.play(GrowFromEdge(squares[1], RIGHT))
    self.play(GrowFromEdge(squares[2], UR))
    self.play(GrowFromEdge(squares[3], UP, point_color=RED))

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _edge_ , _point_color =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromEdge._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **edge** (_np.ndarray_)
  * **point_color** (_str_)


Return type:
    
None
[ Next GrowFromPoint ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html>) [ Previous GrowFromCenter ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromCenter.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [GrowFromEdge](https://docs.manim.community/en/stable/reference/<#>)
    * `[GrowFromEdge`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromEdge>)
      * `[GrowFromEdge._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromEdge._original__init__>)


