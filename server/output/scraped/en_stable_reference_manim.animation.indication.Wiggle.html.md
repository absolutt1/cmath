# Wiggle[¶](https://docs.manim.community/en/stable/reference/<#wiggle> "Link to this heading")
Qualified name: `manim.animation.indication.Wiggle`
_class_ Wiggle(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#Wiggle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Wiggle> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Wiggle a Mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to wiggle.
  * **scale_value** (_float_) – The factor by which the mobject will be temporarily scaled.
  * **rotation_angle** (_float_) – The wiggle angle.
  * **n_wiggles** (_int_) – The number of wiggles.
  * **scale_about_point** (_np.ndarray_ _|__None_) – The point about which the mobject gets scaled.
  * **rotate_about_point** (_np.ndarray_ _|__None_) – The point around which the mobject gets rotated.
  * **run_time** (_float_) – The duration of the animation


Examples
Example: ApplyingWaves [¶](https://docs.manim.community/en/stable/reference/<#applyingwaves>)
```
frommanimimport *
classApplyingWaves(Scene):
  defconstruct(self):
    tex = Tex("Wiggle").scale(3)
    self.play(Wiggle(tex))
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`get_rotate_about_point`  
---  
`get_scale_about_point`  
`interpolate_submobject`  
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _scale_value =1.1_, _rotation_angle =0.06283185307179587_, _n_wiggles =6_, _scale_about_point =None_, _rotate_about_point =None_, _run_time =2_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Wiggle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **scale_value** (_float_)
  * **rotation_angle** (_float_)
  * **n_wiggles** (_int_)
  * **scale_about_point** (_ndarray_ _|__None_)
  * **rotate_about_point** (_ndarray_ _|__None_)
  * **run_time** (_float_)


Return type:
    
None
[ Next movement ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.html>) [ Previous ShowPassingFlashWithThinningStrokeWidth ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Wiggle](https://docs.manim.community/en/stable/reference/<#>)
    * `[Wiggle`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Wiggle>)
      * `[Wiggle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Wiggle._original__init__>)


