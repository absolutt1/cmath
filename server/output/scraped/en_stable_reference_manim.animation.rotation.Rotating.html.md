# Rotating[¶](https://docs.manim.community/en/stable/reference/<#rotating> "Link to this heading")
Qualified name: `manim.animation.rotation.Rotating`
_class_ Rotating(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/rotation.html#Rotating>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating.interpolate_mobject> "manim.animation.rotation.Rotating.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **axis** (_np.ndarray_)
  * **radians** (_np.ndarray_)
  * **about_point** (_np.ndarray_ _|__None_)
  * **about_edge** (_np.ndarray_ _|__None_)
  * **run_time** (_float_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


_original__init__(_mobject_ , _axis=array([0._ , _0._ , _1.])_ , _radians=6.283185307179586_ , _about_point=None_ , _about_edge=None_ , _run_time=5_ , _rate_func= <function linear>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **axis** (_np.ndarray_)
  * **radians** (_np.ndarray_)
  * **about_point** (_np.ndarray_ _|__None_)
  * **about_edge** (_np.ndarray_ _|__None_)
  * **run_time** (_float_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/rotation.html#Rotating.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next specialized ](https://docs.manim.community/en/stable/reference/<manim.animation.specialized.html>) [ Previous Rotate ](https://docs.manim.community/en/stable/reference/<manim.animation.rotation.Rotate.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Rotating](https://docs.manim.community/en/stable/reference/<#>)
    * `[Rotating`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating>)
      * `[Rotating._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating._original__init__>)
      * `[Rotating.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotating.interpolate_mobject>)


