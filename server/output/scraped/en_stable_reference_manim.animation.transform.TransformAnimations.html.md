# TransformAnimations[¶](https://docs.manim.community/en/stable/reference/<#transformanimations> "Link to this heading")
Qualified name: `manim.animation.transform.TransformAnimations`
_class_ TransformAnimations(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#TransformAnimations>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Methods
`[interpolate`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations.interpolate> "manim.animation.transform.TransformAnimations.interpolate") | Set the animation progress.  
---|---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
Parameters:
    
  * **start_anim** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **end_anim** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **rate_func** (_Callable_)


_original__init__(_start_anim_ , _end_anim_ , _rate_func= <function squish_rate_func.<locals>.result>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **start_anim** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **end_anim** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **rate_func** (_Callable_)


Return type:
    
None
interpolate(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#TransformAnimations.interpolate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations.interpolate> "Link to this definition")
    
Set the animation progress.
This method gets called for every frame during an animation.
Parameters:
    
**alpha** (_float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning the end.
Return type:
    
None
[ Next TransformFromCopy ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.TransformFromCopy.html>) [ Previous Transform ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TransformAnimations](https://docs.manim.community/en/stable/reference/<#>)
    * `[TransformAnimations`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations>)
      * `[TransformAnimations._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations._original__init__>)
      * `[TransformAnimations.interpolate()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformAnimations.interpolate>)


