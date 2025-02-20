# ApplyWave[¶](https://docs.manim.community/en/stable/reference/<#applywave> "Link to this heading")
Qualified name: `manim.animation.indication.ApplyWave`
_class_ ApplyWave(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#ApplyWave>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ApplyWave> "Link to this definition")
    
Bases: `[Homotopy`](https://docs.manim.community/en/stable/reference/<manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy> "manim.animation.movement.Homotopy")
Send a wave through the Mobject distorting it temporarily.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be distorted.
  * **direction** (_np.ndarray_) – The direction in which the wave nudges points of the shape
  * **amplitude** (_float_) – The distance points of the shape get shifted
  * **wave_func** (_Callable_ _[__[__float_ _]__,__float_ _]_) – The function defining the shape of one wave flank.
  * **time_width** (_float_) – The length of the wave relative to the width of the mobject.
  * **ripples** (_int_) – The number of ripples of the wave
  * **run_time** (_float_) – The duration of the animation.


Examples
Example: ApplyingWaves [¶](https://docs.manim.community/en/stable/reference/<#applyingwaves>)
```
frommanimimport *
classApplyingWaves(Scene):
  defconstruct(self):
    tex = Tex("WaveWaveWaveWaveWave").scale(2)
    self.play(ApplyWave(tex))
    self.play(ApplyWave(
      tex,
      direction=RIGHT,
      time_width=0.5,
      amplitude=0.3
    ))
    self.play(ApplyWave(
      tex,
      rate_func=linear,
      ripples=4
    ))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _direction=array([0._ , _1._ , _0.])_ , _amplitude=0.2_ , _wave_func= <function smooth>_, _time_width=1_ , _ripples=1_ , _run_time=2_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ApplyWave._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **direction** (_ndarray_)
  * **amplitude** (_float_)
  * **wave_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **time_width** (_float_)
  * **ripples** (_int_)
  * **run_time** (_float_)


Return type:
    
None
[ Next Blink ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Blink.html>) [ Previous indication ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ApplyWave](https://docs.manim.community/en/stable/reference/<#>)
    * `[ApplyWave`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ApplyWave>)
      * `[ApplyWave._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ApplyWave._original__init__>)


