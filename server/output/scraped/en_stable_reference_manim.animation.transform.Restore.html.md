# Restore[¶](https://docs.manim.community/en/stable/reference/<#restore> "Link to this heading")
Qualified name: `manim.animation.transform.Restore`
_class_ Restore(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#Restore>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Restore> "Link to this definition")
    
Bases: `[ApplyMethod`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod> "manim.animation.transform.ApplyMethod")
Transforms a mobject to its last saved state.
To save the state of a mobject, use the `[save_state()`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state> "manim.mobject.mobject.Mobject.save_state") method.
Examples
Example: RestoreExample [¶](https://docs.manim.community/en/stable/reference/<#restoreexample>)
```
frommanimimport *
classRestoreExample(Scene):
  defconstruct(self):
    s = Square()
    s.save_state()
    self.play(FadeIn(s))
    self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
    self.play(s.animate.shift(5*DOWN).rotate(PI/4))
    self.wait()
    self.play(Restore(s), run_time=2)

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
    
**mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
_original__init__(_mobject_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Restore._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
Return type:
    
None
[ Next ScaleInPlace ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ScaleInPlace.html>) [ Previous ReplacementTransform ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ReplacementTransform.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Restore](https://docs.manim.community/en/stable/reference/<#>)
    * `[Restore`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Restore>)
      * `[Restore._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Restore._original__init__>)


