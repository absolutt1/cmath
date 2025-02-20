# PhaseFlow[¶](https://docs.manim.community/en/stable/reference/<#phaseflow> "Link to this heading")
Qualified name: `manim.animation.movement.PhaseFlow`
_class_ PhaseFlow(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/movement.html#PhaseFlow>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow.interpolate_mobject> "manim.animation.movement.PhaseFlow.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
Parameters:
    
  * **function** (_Callable_ _[__[__np.ndarray_ _]__,__np.ndarray_ _]_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **virtual_time** (_float_)
  * **suspend_mobject_updating** (_bool_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


_original__init__(_function_ , _mobject_ , _virtual_time=1_ , _suspend_mobject_updating=False_ , _rate_func= <function linear>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **function** (_Callable_ _[__[__np.ndarray_ _]__,__np.ndarray_ _]_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **virtual_time** (_float_)
  * **suspend_mobject_updating** (_bool_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/movement.html#PhaseFlow.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next SmoothedVectorizedHomotopy ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.SmoothedVectorizedHomotopy.html>) [ Previous MoveAlongPath ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.MoveAlongPath.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [PhaseFlow](https://docs.manim.community/en/stable/reference/<#>)
    * `[PhaseFlow`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow>)
      * `[PhaseFlow._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow._original__init__>)
      * `[PhaseFlow.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.PhaseFlow.interpolate_mobject>)


