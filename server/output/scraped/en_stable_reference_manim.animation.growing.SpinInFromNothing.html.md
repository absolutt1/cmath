# SpinInFromNothing[¶](https://docs.manim.community/en/stable/reference/<#spininfromnothing> "Link to this heading")
Qualified name: `manim.animation.growing.SpinInFromNothing`
_class_ SpinInFromNothing(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/growing.html#SpinInFromNothing>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.SpinInFromNothing> "Link to this definition")
    
Bases: `[GrowFromCenter`](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter> "manim.animation.growing.GrowFromCenter")
Introduce an `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") spinning and growing it from its center.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
  * **angle** (_float_) – The amount of spinning before mobject reaches its full size. E.g. 2*PI means that the object will do one full spin before being fully introduced.
  * **point_color** (_str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples
Example: SpinInFromNothingExample [¶](https://docs.manim.community/en/stable/reference/<#spininfromnothingexample>)
```
frommanimimport *
classSpinInFromNothingExample(Scene):
  defconstruct(self):
    squares = [Square() for _ in range(3)]
    VGroup(*squares).set_x(0).arrange(buff=2)
    self.play(SpinInFromNothing(squares[0]))
    self.play(SpinInFromNothing(squares[1], angle=2 * PI))
    self.play(SpinInFromNothing(squares[2], point_color=RED))

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _angle =1.5707963267948966_, _point_color =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.SpinInFromNothing._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **angle** (_float_)
  * **point_color** (_str_)


Return type:
    
None
[ Next indication ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.html>) [ Previous GrowFromPoint ](https://docs.manim.community/en/stable/reference/<manim.animation.growing.GrowFromPoint.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SpinInFromNothing](https://docs.manim.community/en/stable/reference/<#>)
    * `[SpinInFromNothing`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.SpinInFromNothing>)
      * `[SpinInFromNothing._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.growing.SpinInFromNothing._original__init__>)


