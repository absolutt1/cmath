# UpdateFromAlphaFunc[¶](https://docs.manim.community/en/stable/reference/<#updatefromalphafunc> "Link to this heading")
Qualified name: `manim.animation.updaters.update.UpdateFromAlphaFunc`
_class_ UpdateFromAlphaFunc(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc> "Link to this definition")
    
Bases: `[UpdateFromFunc`](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc> "manim.animation.updaters.update.UpdateFromFunc")
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject> "manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **update_function** (_Callable_ _[__[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]__,__Any_ _]_)
  * **suspend_mobject_updating** (_bool_)


_original__init__(_mobject_ , _update_function_ , _suspend_mobject_updating =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **update_function** (_Callable_ _[__[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]__,__Any_ _]_)
  * **suspend_mobject_updating** (_bool_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next UpdateFromFunc ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.UpdateFromFunc.html>) [ Previous MaintainPositionRelativeTo ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.MaintainPositionRelativeTo.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [UpdateFromAlphaFunc](https://docs.manim.community/en/stable/reference/<#>)
    * `[UpdateFromAlphaFunc`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc>)
      * `[UpdateFromAlphaFunc._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc._original__init__>)
      * `[UpdateFromAlphaFunc.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject>)


