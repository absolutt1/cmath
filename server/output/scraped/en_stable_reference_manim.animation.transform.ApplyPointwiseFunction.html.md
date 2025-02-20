# ApplyPointwiseFunction[¶](https://docs.manim.community/en/stable/reference/<#applypointwisefunction> "Link to this heading")
Qualified name: `manim.animation.transform.ApplyPointwiseFunction`
_class_ ApplyPointwiseFunction(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ApplyPointwiseFunction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyPointwiseFunction> "Link to this definition")
    
Bases: `[ApplyMethod`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod> "manim.animation.transform.ApplyMethod")
Animation that applies a pointwise function to a mobject.
Examples
Example: WarpSquare [¶](https://docs.manim.community/en/stable/reference/<#warpsquare>)
```
frommanimimport *
classWarpSquare(Scene):
  defconstruct(self):
    square = Square()
    self.play(
      ApplyPointwiseFunction(
        lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
      )
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
    
  * **function** (_types.MethodType_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **run_time** (_float_)


_original__init__(_function_ , _mobject_ , _run_time =3.0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyPointwiseFunction._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **function** (_MethodType_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **run_time** (_float_)


Return type:
    
None
[ Next ApplyPointwiseFunctionToCenter ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyPointwiseFunctionToCenter.html>) [ Previous ApplyMethod ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ApplyPointwiseFunction](https://docs.manim.community/en/stable/reference/<#>)
    * `[ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyPointwiseFunction>)
      * `[ApplyPointwiseFunction._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyPointwiseFunction._original__init__>)


