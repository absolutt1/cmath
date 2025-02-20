# GrowArrow[¶](https://docs.manim.community/en/stable/reference/<#growarrow> "Link to this heading")
Qualified name: `manim.animation.growing.GrowArrow`
_class_ GrowArrow(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/growing.html#GrowArrow>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowArrow> "Link to this definition")
    
Bases: `[GrowFromPoint`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint> "manim.animation.growing.GrowFromPoint")
Introduce an `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow") by growing it from its start toward its tip.
Parameters:
    
  * **arrow** ([_Arrow_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow")) – The arrow to be introduced.
  * **point_color** (_str_) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.


Examples
Example: GrowArrowExample [¶](https://docs.manim.community/en/stable/reference/<#growarrowexample>)
```
frommanimimport *
classGrowArrowExample(Scene):
  defconstruct(self):
    arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
    VGroup(*arrows).set_x(0).arrange(buff=2)
    self.play(GrowArrow(arrows[0]))
    self.play(GrowArrow(arrows[1], point_color=RED))

```
Copy to clipboard
Make interactive
Methods
`create_starting_mobject`  
---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_arrow_ , _point_color =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowArrow._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **arrow** ([_Arrow_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow"))
  * **point_color** (_str_)


Return type:
    
None
[ Next GrowFromCenter ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromCenter.html>) [ Previous growing ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [GrowArrow](https://docs.manim.community/en/stable/reference/<#>)
    * `[GrowArrow`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowArrow>)
      * `[GrowArrow._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.GrowArrow._original__init__>)


