# FocusOn[¶](https://docs.manim.community/en/stable/reference/<#focuson> "Link to this heading")
Qualified name: `manim.animation.indication.FocusOn`
_class_ FocusOn(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#FocusOn>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.FocusOn> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Shrink a spotlight to a position.
Parameters:
    
  * **focus_point** (_np.ndarray_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.
  * **opacity** (_float_) – The opacity of the spotlight.
  * **color** (_str_) – The color of the spotlight.
  * **run_time** (_float_) – The duration of the animation.


Examples
Example: UsingFocusOn [¶](https://docs.manim.community/en/stable/reference/<#usingfocuson>)
```
frommanimimport *
classUsingFocusOn(Scene):
  defconstruct(self):
    dot = Dot(color=YELLOW).shift(DOWN)
    self.add(Tex("Focusing on the dot below:"), dot)
    self.play(FocusOn(dot))
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`create_target`  
---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_focus_point_ , _opacity =0.2_, _color =ManimColor('#888888')_, _run_time =2_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.FocusOn._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **focus_point** (_ndarray_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **opacity** (_float_)
  * **color** (_str_)
  * **run_time** (_float_)


Return type:
    
None
[ Next Indicate ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Indicate.html>) [ Previous Flash ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Flash.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [FocusOn](https://docs.manim.community/en/stable/reference/<#>)
    * `[FocusOn`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.FocusOn>)
      * `[FocusOn._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.FocusOn._original__init__>)


