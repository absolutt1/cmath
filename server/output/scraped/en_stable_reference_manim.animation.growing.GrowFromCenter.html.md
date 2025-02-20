# GrowFromCenter[¶](https://docs.manim.community/en/stable/reference/<#growfromcenter> "Link to this heading")
Qualified name: `manim.animation.growing.GrowFromCenter`
_class_ GrowFromCenter(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/growing.html#GrowFromCenter>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromCenter> "Link to this definition")
    
Bases: `[GrowFromPoint`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint> "manim.animation.growing.GrowFromPoint")
Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") by growing it from its center.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
  * **point_color** (_str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples
Example: GrowFromCenterExample [¶](https://docs.manim.community/en/stable/reference/<#growfromcenterexample>)
```
frommanimimport *
classGrowFromCenterExample(Scene):
  defconstruct(self):
    squares = [Square() for _ in range(2)]
    VGroup(*squares).set_x(0).arrange(buff=2)
    self.play(GrowFromCenter(squares[0]))
    self.play(GrowFromCenter(squares[1], point_color=RED))

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _point_color =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromCenter._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **point_color** (_str_)


Return type:
    
None
[ Next GrowFromEdge ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromEdge.html>) [ Previous GrowArrow ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowArrow.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [GrowFromCenter](https://docs.manim.community/en/stable/reference/<#>)
    * `[GrowFromCenter`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromCenter>)
      * `[GrowFromCenter._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowFromCenter._original__init__>)


