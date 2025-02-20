# AnimatedBoundary[¶](https://docs.manim.community/en/stable/reference/<#animatedboundary> "Link to this heading")
Qualified name: `manim.animation.changing.AnimatedBoundary`
_class_ AnimatedBoundary(_vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max_stroke_width=3, cycle_rate=0.5, back_and_forth=True, draw_rate_func=<function smooth>, fade_rate_func=<function smooth>, **kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/changing.html#AnimatedBoundary>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.AnimatedBoundary> "Link to this definition")
    
Bases: `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
Boundary of a `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") with animated color change.
Examples
Example: AnimatedBoundaryExample [¶](https://docs.manim.community/en/stable/reference/<#animatedboundaryexample>)
```
frommanimimport *
classAnimatedBoundaryExample(Scene):
  defconstruct(self):
    text = Text("So shiny!")
    boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                  cycle_rate=3)
    self.add(text, boundary)
    self.wait(2)

```
Copy to clipboard
Make interactive
Methods
`full_family_become_partial`  
---  
`update_boundary_copies`  
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
_original__init__(_vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max_stroke_width=3, cycle_rate=0.5, back_and_forth=True, draw_rate_func=<function smooth>, fade_rate_func=<function smooth>, **kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.AnimatedBoundary._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next TracedPath ](https://docs.manim.community/en/stable/reference/<manim.animation.changing.TracedPath.html>) [ Previous changing ](https://docs.manim.community/en/stable/reference/<manim.animation.changing.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [AnimatedBoundary](https://docs.manim.community/en/stable/reference/<#>)
    * `[AnimatedBoundary`](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.AnimatedBoundary>)
      * `[AnimatedBoundary._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.changing.AnimatedBoundary._original__init__>)


