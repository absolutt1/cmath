# TransformFromCopy[¶](https://docs.manim.community/en/stable/reference/<#transformfromcopy> "Link to this heading")
Qualified name: `manim.animation.transform.TransformFromCopy`
_class_ TransformFromCopy(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#TransformFromCopy>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Performs a reversed Transform
Methods
`[interpolate`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy.interpolate> "manim.animation.transform.TransformFromCopy.interpolate") | Set the animation progress.  
---|---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


_original__init__(_mobject_ , _target_mobject_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


Return type:
    
None
interpolate(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#TransformFromCopy.interpolate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy.interpolate> "Link to this definition")
    
Set the animation progress.
This method gets called for every frame during an animation.
Parameters:
    
**alpha** (_float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning the end.
Return type:
    
None
[ Next transform_matching_parts ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.html>) [ Previous TransformAnimations ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.TransformAnimations.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TransformFromCopy](https://docs.manim.community/en/stable/reference/<#>)
    * `[TransformFromCopy`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy>)
      * `[TransformFromCopy._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy._original__init__>)
      * `[TransformFromCopy.interpolate()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.TransformFromCopy.interpolate>)


