# ApplyMatrix[¶](https://docs.manim.community/en/stable/reference/<#applymatrix> "Link to this heading")
Qualified name: `manim.animation.transform.ApplyMatrix`
_class_ ApplyMatrix(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ApplyMatrix>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMatrix> "Link to this definition")
    
Bases: `[ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction> "manim.animation.transform.ApplyPointwiseFunction")
Applies a matrix transform to an mobject.
Parameters:
    
  * **matrix** (_np.ndarray_) – The transformation matrix.
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **about_point** (_np.ndarray_) – The origin point for the transform. Defaults to `ORIGIN`.
  * **kwargs** – Further keyword arguments that are passed to `[ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction> "manim.animation.transform.ApplyPointwiseFunction").


Examples
Example: ApplyMatrixExample [¶](https://docs.manim.community/en/stable/reference/<#applymatrixexample>)
```
frommanimimport *
classApplyMatrixExample(Scene):
  defconstruct(self):
    matrix = [[1, 1], [0, 2/3]]
    self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

```
Copy to clipboard
Make interactive
Methods
`initialize_matrix`  
---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_matrix_ , _mobject_ , _about_point =array([0., 0., 0.])_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMatrix._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **matrix** (_ndarray_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **about_point** (_ndarray_)


Return type:
    
None
[ Next ApplyMethod ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html>) [ Previous ApplyFunction ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyFunction.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ApplyMatrix](https://docs.manim.community/en/stable/reference/<#>)
    * `[ApplyMatrix`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMatrix>)
      * `[ApplyMatrix._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMatrix._original__init__>)


