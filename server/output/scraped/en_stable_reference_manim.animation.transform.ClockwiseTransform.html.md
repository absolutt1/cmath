# ClockwiseTransform[¶](https://docs.manim.community/en/stable/reference/<#clockwisetransform> "Link to this heading")
Qualified name: `manim.animation.transform.ClockwiseTransform`
_class_ ClockwiseTransform(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ClockwiseTransform>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ClockwiseTransform> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Transforms the points of a mobject along a clockwise oriented arc.
See also
`[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform"), `[CounterclockwiseTransform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform> "manim.animation.transform.CounterclockwiseTransform")
Examples
Example: ClockwiseExample [¶](https://docs.manim.community/en/stable/reference/<#clockwiseexample>)
```
frommanimimport *
classClockwiseExample(Scene):
  defconstruct(self):
    dl, dr = Dot(), Dot()
    sl, sr = Square(), Square()
    VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
    VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)
    self.add(dl, dr)
    self.wait()
    self.play(
      ClockwiseTransform(dl, sl),
      Transform(dr, sr)
    )
    self.wait()

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **path_arc** (_float_)


_original__init__(_mobject_ , _target_mobject_ , _path_arc =-3.141592653589793_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ClockwiseTransform._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **path_arc** (_float_)


Return type:
    
None
[ Next CounterclockwiseTransform ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.CounterclockwiseTransform.html>) [ Previous ApplyPointwiseFunctionToCenter ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyPointwiseFunctionToCenter.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ClockwiseTransform](https://docs.manim.community/en/stable/reference/<#>)
    * `[ClockwiseTransform`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ClockwiseTransform>)
      * `[ClockwiseTransform._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ClockwiseTransform._original__init__>)


