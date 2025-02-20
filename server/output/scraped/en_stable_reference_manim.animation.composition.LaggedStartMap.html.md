# LaggedStartMap[¶](https://docs.manim.community/en/stable/reference/<#laggedstartmap> "Link to this heading")
Qualified name: `manim.animation.composition.LaggedStartMap`
_class_ LaggedStartMap(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/composition.html#LaggedStartMap>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStartMap> "Link to this definition")
    
Bases: `[LaggedStart`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart> "manim.animation.composition.LaggedStart")
Plays a series of `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") while mapping a function to submobjects.
Parameters:
    
  * **AnimationClass** (_Callable_ _[__...__,_[_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") _]_) – `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") to apply to mobject.
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") whose submobjects the animation, and optionally the function, are to be applied.
  * **arg_creator** (_Callable_ _[__[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]__,__str_ _]_) – Function which will be applied to `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **run_time** (_float_) – The duration of the animation in seconds.


Examples
Example: LaggedStartMapExample [¶](https://docs.manim.community/en/stable/reference/<#laggedstartmapexample>)
```
frommanimimport *
classLaggedStartMapExample(Scene):
  defconstruct(self):
    title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
    dots = VGroup(
      *[Dot(radius=0.16) for _ in range(35)]
      ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
    self.add(dots, title)
    # Animate yellow ripple effect
    for mob in dots, title:
      self.play(LaggedStartMap(
        ApplyMethod, mob,
        lambda m : (m.set_color, YELLOW),
        lag_ratio = 0.1,
        rate_func = there_and_back,
        run_time = 2
      ))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_AnimationClass_ , _mobject_ , _arg_creator =None_, _run_time =2_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStartMap._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **AnimationClass** (_Callable_ _[__[__...__]__,_[_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") _]_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **arg_creator** (_Callable_ _[__[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]__,__str_ _]_)
  * **run_time** (_float_)


Return type:
    
None
[ Next Succession ](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html>) [ Previous LaggedStart ](https://docs.manim.community/en/stable/reference/<manim.animation.composition.LaggedStart.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LaggedStartMap](https://docs.manim.community/en/stable/reference/<#>)
    * `[LaggedStartMap`](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStartMap>)
      * `[LaggedStartMap._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStartMap._original__init__>)


