# MoveAlongPath[¶](https://docs.manim.community/en/stable/reference/<#movealongpath> "Link to this heading")
Qualified name: `manim.animation.movement.MoveAlongPath`
_class_ MoveAlongPath(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/movement.html#MoveAlongPath>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Make one mobject move along the path of another mobject.
Example: MoveAlongPathExample [¶](https://docs.manim.community/en/stable/reference/<#movealongpathexample>)
```
frommanimimport *
classMoveAlongPathExample(Scene):
  defconstruct(self):
    d1 = Dot().set_color(ORANGE)
    l1 = Line(LEFT, RIGHT)
    l2 = VMobject()
    self.add(d1, l1, l2)
    l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
    self.play(MoveAlongPath(d1, l1), rate_func=linear)

```
Copy to clipboard
Make interactive
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath.interpolate_mobject> "manim.animation.movement.MoveAlongPath.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **path** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **suspend_mobject_updating** (_bool_ _|__None_)


_original__init__(_mobject_ , _path_ , _suspend_mobject_updating =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **path** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **suspend_mobject_updating** (_bool_ _|__None_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/movement.html#MoveAlongPath.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next PhaseFlow ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.PhaseFlow.html>) [ Previous Homotopy ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.Homotopy.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MoveAlongPath](https://docs.manim.community/en/stable/reference/<#>)
    * `[MoveAlongPath`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath>)
      * `[MoveAlongPath._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath._original__init__>)
      * `[MoveAlongPath.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.MoveAlongPath.interpolate_mobject>)


