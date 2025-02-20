# Broadcast[¶](https://docs.manim.community/en/stable/reference/<#broadcast> "Link to this heading")
Qualified name: `manim.animation.specialized.Broadcast`
_class_ Broadcast(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/specialized.html#Broadcast>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.specialized.Broadcast> "Link to this definition")
    
Bases: `[LaggedStart`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart> "manim.animation.composition.LaggedStart")
Broadcast a mobject starting from an `initial_width`, up to the actual size of the mobject.
Parameters:
    
  * **mobject** – The mobject to be broadcast.
  * **focal_point** (_Sequence_ _[__float_ _]_) – The center of the broadcast, by default ORIGIN.
  * **n_mobs** (_int_) – The number of mobjects that emerge from the focal point, by default 5.
  * **initial_opacity** (_float_) – The starting stroke opacity of the mobjects emitted from the broadcast, by default 1.
  * **final_opacity** (_float_) – The final stroke opacity of the mobjects emitted from the broadcast, by default 0.
  * **initial_width** (_float_) – The initial width of the mobjects, by default 0.0.
  * **remover** (_bool_) – Whether the mobjects should be removed from the scene after the animation, by default True.
  * **lag_ratio** (_float_) – The time between each iteration of the mobject, by default 0.2.
  * **run_time** (_float_) – The total duration of the animation, by default 3.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[LaggedStart`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart> "manim.animation.composition.LaggedStart").


Examples
Example: BroadcastExample [¶](https://docs.manim.community/en/stable/reference/<#broadcastexample>)
```
frommanimimport *
classBroadcastExample(Scene):
  defconstruct(self):
    mob = Circle(radius=4, color=TEAL_A)
    self.play(Broadcast(mob))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _focal_point =array([0., 0., 0.])_, _n_mobs =5_, _initial_opacity =1_, _final_opacity =0_, _initial_width =0.0_, _remover =True_, _lag_ratio =0.2_, _run_time =3_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.specialized.Broadcast._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **focal_point** (_Sequence_ _[__float_ _]_)
  * **n_mobs** (_int_)
  * **initial_opacity** (_float_)
  * **final_opacity** (_float_)
  * **initial_width** (_float_)
  * **remover** (_bool_)
  * **lag_ratio** (_float_)
  * **run_time** (_float_)
  * **kwargs** (_Any_)


[ Next speedmodifier ](https://docs.manim.community/en/stable/reference/<manim.animation.speedmodifier.html>) [ Previous specialized ](https://docs.manim.community/en/stable/reference/<manim.animation.specialized.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Broadcast](https://docs.manim.community/en/stable/reference/<#>)
    * `[Broadcast`](https://docs.manim.community/en/stable/reference/<#manim.animation.specialized.Broadcast>)
      * `[Broadcast._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.specialized.Broadcast._original__init__>)


