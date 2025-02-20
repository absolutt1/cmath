# Indicate[¶](https://docs.manim.community/en/stable/reference/<#indicate> "Link to this heading")
Qualified name: `manim.animation.indication.Indicate`
_class_ Indicate(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#Indicate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Indicate> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Indicate a Mobject by temporarily resizing and recoloring it.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to indicate.
  * **scale_factor** (_float_) – The factor by which the mobject will be temporally scaled
  * **color** (_str_) – The color the mobject temporally takes.
  * **rate_func** (_Callable_ _[__[__float_ _,__float_ _|__None_ _]__,__np.ndarray_ _]_) – The function defining the animation progress at every point in time.
  * **kwargs** – Additional arguments to be passed to the `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession") constructor


Examples
Example: UsingIndicate [¶](https://docs.manim.community/en/stable/reference/<#usingindicate>)
```
frommanimimport *
classUsingIndicate(Scene):
  defconstruct(self):
    tex = Tex("Indicate").scale(3)
    self.play(Indicate(tex))
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
_original__init__(_mobject_ , _scale_factor=1.2_ , _color=ManimColor('#FFFF00')_ , _rate_func= <function there_and_back>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Indicate._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **scale_factor** (_float_)
  * **color** (_str_)
  * **rate_func** (_Callable_ _[__[__float_ _,__float_ _|__None_ _]__,__ndarray_ _]_)


Return type:
    
None
[ Next ShowPassingFlash ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.ShowPassingFlash.html>) [ Previous FocusOn ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.FocusOn.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Indicate](https://docs.manim.community/en/stable/reference/<#>)
    * `[Indicate`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Indicate>)
      * `[Indicate._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Indicate._original__init__>)


