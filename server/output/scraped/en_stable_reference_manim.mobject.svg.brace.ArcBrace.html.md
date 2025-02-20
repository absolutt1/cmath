# ArcBrace[¶](https://docs.manim.community/en/stable/reference/<#arcbrace> "Link to this heading")
Qualified name: `manim.mobject.svg.brace.ArcBrace`
_class_ ArcBrace(_arc =None_, _direction =array([1., 0., 0.])_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#ArcBrace>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace> "Link to this definition")
    
Bases: `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace")
Creates a `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace") that wraps around an `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc").
The direction parameter allows the brace to be applied from outside or inside the arc.
Warning
The `[ArcBrace`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace> "manim.mobject.svg.brace.ArcBrace") is smaller for arcs with smaller radii.
Note
The `[ArcBrace`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace> "manim.mobject.svg.brace.ArcBrace") is initially a vertical `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace") defined by the length of the `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc"), but is scaled down to match the start and end angles. An exponential function is then applied after it is shifted based on the radius of the arc.
The scaling effect is not applied for arcs with radii smaller than 1 to prevent over-scaling.
Parameters:
    
  * **arc** ([_Arc_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc") _|__None_) – The `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc") that wraps around the `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace") mobject.
  * **direction** (_Sequence_ _[__float_ _]_) – The direction from which the brace faces the arc. `LEFT` for inside the arc, and `RIGHT` for the outside.


Example
Example: ArcBraceExample [¶](https://docs.manim.community/en/stable/reference/<#arcbraceexample>)
![../_images/ArcBraceExample-1.png](https://docs.manim.community/en/stable/_images/ArcBraceExample-1.png)
```
frommanimimport *
classArcBraceExample(Scene):
  defconstruct(self):
    arc_1 = Arc(radius=1.5,start_angle=0,angle=2*PI/3).set_color(RED)
    brace_1 = ArcBrace(arc_1,LEFT)
    group_1 = VGroup(arc_1,brace_1)
    arc_2 = Arc(radius=3,start_angle=0,angle=5*PI/6).set_color(YELLOW)
    brace_2 = ArcBrace(arc_2)
    group_2 = VGroup(arc_2,brace_2)
    arc_3 = Arc(radius=0.5,start_angle=-0,angle=PI).set_color(BLUE)
    brace_3 = ArcBrace(arc_3)
    group_3 = VGroup(arc_3,brace_3)
    arc_4 = Arc(radius=0.2,start_angle=0,angle=3*PI/2).set_color(GREEN)
    brace_4 = ArcBrace(arc_4)
    group_4 = VGroup(arc_4,brace_4)
    arc_group = VGroup(group_1, group_2, group_3, group_4).arrange_in_grid(buff=1.5)
    self.add(arc_group.center())

```
Copy to clipboard
Make interactive
References: `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc")
Methods
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_arc =None_, _direction =array([1., 0., 0.])_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **arc** ([_Arc_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc") _|__None_)
  * **direction** (_Sequence_ _[__float_ _]_)


[ Next Brace ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html>) [ Previous brace ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ArcBrace](https://docs.manim.community/en/stable/reference/<#>)
    * `[ArcBrace`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace>)
      * `[ArcBrace._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.ArcBrace._original__init__>)


