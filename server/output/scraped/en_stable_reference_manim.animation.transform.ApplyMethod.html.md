# ApplyMethod[¶](https://docs.manim.community/en/stable/reference/<#applymethod> "Link to this heading")
Qualified name: `manim.animation.transform.ApplyMethod`
_class_ ApplyMethod(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ApplyMethod>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMethod> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Animates a mobject by applying a method.
Note that only the method needs to be passed to this animation, it is not required to pass the corresponding mobject. Furthermore, this animation class only works if the method returns the modified mobject.
Parameters:
    
  * **method** (_Callable_) – The method that will be applied in the animation.
  * **args** – Any positional arguments to be passed when applying the method.
  * **kwargs** – Any keyword arguments passed to `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform").


Methods
`check_validity_of_input`  
---  
`create_target`  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_method_ , _* args_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMethod._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**method** (_Callable_)
Return type:
    
None
[ Next ApplyPointwiseFunction ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyPointwiseFunction.html>) [ Previous ApplyMatrix ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMatrix.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ApplyMethod](https://docs.manim.community/en/stable/reference/<#>)
    * `[ApplyMethod`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMethod>)
      * `[ApplyMethod._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ApplyMethod._original__init__>)


