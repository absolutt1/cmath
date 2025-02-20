# ScaleInPlace[¶](https://docs.manim.community/en/stable/reference/<#scaleinplace> "Link to this heading")
Qualified name: `manim.animation.transform.ScaleInPlace`
_class_ ScaleInPlace(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ScaleInPlace>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ScaleInPlace> "Link to this definition")
    
Bases: `[ApplyMethod`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod> "manim.animation.transform.ApplyMethod")
Animation that scales a mobject by a certain factor.
Examples
Example: ScaleInPlaceExample [¶](https://docs.manim.community/en/stable/reference/<#scaleinplaceexample>)
```
frommanimimport *
classScaleInPlaceExample(Scene):
  defconstruct(self):
    self.play(ScaleInPlace(Text("Hello World!"), 2))

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
  * **scale_factor** (_float_)


_original__init__(_mobject_ , _scale_factor_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ScaleInPlace._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **scale_factor** (_float_)


Return type:
    
None
[ Next ShrinkToCenter ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ShrinkToCenter.html>) [ Previous Restore ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Restore.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ScaleInPlace](https://docs.manim.community/en/stable/reference/<#>)
    * `[ScaleInPlace`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ScaleInPlace>)
      * `[ScaleInPlace._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ScaleInPlace._original__init__>)


