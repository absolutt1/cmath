# Create[¶](https://docs.manim.community/en/stable/reference/<#create> "Link to this heading")
Qualified name: `manim.animation.creation.Create`
_class_ Create(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Create>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Create> "Link to this definition")
    
Bases: `[ShowPartial`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial> "manim.animation.creation.ShowPartial")
Incrementally show a VMobject.
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_ _|__OpenGLSurface_) – The VMobject to animate.
  * **lag_ratio** (_float_)
  * **introducer** (_bool_)


Raises:
    
**TypeError** – If `mobject` is not an instance of `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").
Examples
Example: CreateScene [¶](https://docs.manim.community/en/stable/reference/<#createscene>)
```
frommanimimport *
classCreateScene(Scene):
  defconstruct(self):
    self.play(Create(Square()))

```
Copy to clipboard
Make interactive
See also
`[ShowPassingFlash`](https://docs.manim.community/en/stable/reference/<manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash> "manim.animation.indication.ShowPassingFlash")
Methods
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _lag_ratio =1.0_, _introducer =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Create._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_ _|__OpenGLSurface_)
  * **lag_ratio** (_float_)
  * **introducer** (_bool_)


Return type:
    
None
[ Next DrawBorderThenFill ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.DrawBorderThenFill.html>) [ Previous AddTextWordByWord ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.AddTextWordByWord.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Create](https://docs.manim.community/en/stable/reference/<#>)
    * `[Create`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Create>)
      * `[Create._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Create._original__init__>)


