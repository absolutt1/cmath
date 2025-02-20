# TracedPath[¶](https://docs.manim.community/en/stable/reference/<#tracedpath> "Link to this heading")
Qualified name: `manim.animation.changing.TracedPath`
_class_ TracedPath(_traced_point_func_ , _stroke_width =2_, _stroke_color =ManimColor('#FFFFFF')_, _dissipating_time =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/changing.html#TracedPath>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.TracedPath> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
Traces the path of a point returned by a function call.
Parameters:
    
  * **traced_point_func** (_Callable_) – The function to be traced.
  * **stroke_width** (_float_) – The width of the trace.
  * **stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_) – The color of the trace.
  * **dissipating_time** (_float_ _|__None_) – The time taken for the path to dissipate. Default set to `None` which disables dissipation.


Examples
Example: TracedPathExample [¶](https://docs.manim.community/en/stable/reference/<#tracedpathexample>)
```
frommanimimport *
classTracedPathExample(Scene):
  defconstruct(self):
    circ = Circle(color=RED).shift(4*LEFT)
    dot = Dot(color=RED).move_to(circ.get_start())
    rolling_circle = VGroup(circ, dot)
    trace = TracedPath(circ.get_start)
    rolling_circle.add_updater(lambda m: m.rotate(-0.3))
    self.add(trace, rolling_circle)
    self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)

```
Copy to clipboard
Make interactive
Example: DissipatingPathExample [¶](https://docs.manim.community/en/stable/reference/<#dissipatingpathexample>)
```
frommanimimport *
classDissipatingPathExample(Scene):
  defconstruct(self):
    a = Dot(RIGHT * 2)
    b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
    self.add(a, b)
    self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
    self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`update_path`  
---  
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
_original__init__(_traced_point_func_ , _stroke_width =2_, _stroke_color =ManimColor('#FFFFFF')_, _dissipating_time =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.TracedPath._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **traced_point_func** (_Callable_)
  * **stroke_width** (_float_)
  * **stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **dissipating_time** (_float_ _|__None_)


[ Next composition ](https://docs.manim.community/en/stable/reference/<manim.animation.composition.html>) [ Previous AnimatedBoundary ](https://docs.manim.community/en/stable/reference/<manim.animation.changing.AnimatedBoundary.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TracedPath](https://docs.manim.community/en/stable/reference/<#>)
    * `[TracedPath`](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.TracedPath>)
      * `[TracedPath._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.TracedPath._original__init__>)


