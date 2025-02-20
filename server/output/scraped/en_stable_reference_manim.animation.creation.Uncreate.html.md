# Uncreate[¶](https://docs.manim.community/en/stable/reference/<#uncreate> "Link to this heading")
Qualified name: `manim.animation.creation.Uncreate`
_class_ Uncreate(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Uncreate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Uncreate> "Link to this definition")
    
Bases: `[Create`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Create.html#manim.animation.creation.Create> "manim.animation.creation.Create")
Like `[Create`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Create.html#manim.animation.creation.Create> "manim.animation.creation.Create") but in reverse.
Examples
Example: ShowUncreate [¶](https://docs.manim.community/en/stable/reference/<#showuncreate>)
```
frommanimimport *
classShowUncreate(Scene):
  defconstruct(self):
    self.play(Uncreate(Square()))

```
Copy to clipboard
Make interactive
See also
`[Create`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Create.html#manim.animation.creation.Create> "manim.animation.creation.Create")
Methods
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **reverse_rate_function** (_bool_)
  * **remover** (_bool_)


_original__init__(_mobject_ , _reverse_rate_function =True_, _remover =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Uncreate._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **reverse_rate_function** (_bool_)
  * **remover** (_bool_)


Return type:
    
None
[ Next UntypeWithCursor ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.UntypeWithCursor.html>) [ Previous TypeWithCursor ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.TypeWithCursor.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Uncreate](https://docs.manim.community/en/stable/reference/<#>)
    * `[Uncreate`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Uncreate>)
      * `[Uncreate._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Uncreate._original__init__>)


