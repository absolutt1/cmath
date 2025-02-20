# MaintainPositionRelativeTo[¶](https://docs.manim.community/en/stable/reference/<#maintainpositionrelativeto> "Link to this heading")
Qualified name: `manim.animation.updaters.update.MaintainPositionRelativeTo`
_class_ MaintainPositionRelativeTo(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject> "manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **tracked_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


_original__init__(_mobject_ , _tracked_mobject_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **tracked_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next UpdateFromAlphaFunc ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.UpdateFromAlphaFunc.html>) [ Previous update ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MaintainPositionRelativeTo](https://docs.manim.community/en/stable/reference/<#>)
    * `[MaintainPositionRelativeTo`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo>)
      * `[MaintainPositionRelativeTo._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo._original__init__>)
      * `[MaintainPositionRelativeTo.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject>)


