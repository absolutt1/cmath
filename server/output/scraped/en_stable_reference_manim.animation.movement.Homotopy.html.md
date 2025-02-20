# Homotopy[¶](https://docs.manim.community/en/stable/reference/<#homotopy> "Link to this heading")
Qualified name: `manim.animation.movement.Homotopy`
_class_ Homotopy(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/movement.html#Homotopy>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.Homotopy> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
A Homotopy.
This is an animation transforming the points of a mobject according to the specified transformation function. With the parameter t moving from 0 to 1 throughout the animation and (x,y,z) describing the coordinates of the point of a mobject, the function passed to the `homotopy` keyword argument should transform the tuple (x,y,z,t) to (x′,y′,z′), the coordinates the original point is transformed to at time t.
Parameters:
    
  * **homotopy** (_Callable_ _[__[__float_ _,__float_ _,__float_ _,__float_ _]__,__tuple_ _[__float_ _,__float_ _,__float_ _]__]_) – A function mapping (x,y,z,t) to (x′,y′,z′).
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject transformed under the given homotopy.
  * **run_time** (_float_) – The run time of the animation.
  * **apply_function_kwargs** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Keyword arguments propagated to `Mobject.apply_function()`.
  * **kwargs** – Further keyword arguments passed to the parent class.


Examples
Example: HomotopyExample [¶](https://docs.manim.community/en/stable/reference/<#homotopyexample>)
```
frommanimimport *
classHomotopyExample(Scene):
  defconstruct(self):
    square = Square()
    defhomotopy(x, y, z, t):
      if t <= 0.25:
        progress = t / 0.25
        return (x, y + progress * 0.2 * np.sin(x), z)
      else:
        wave_progress = (t - 0.25) / 0.75
        return (x, y + 0.2 * np.sin(x + 10 * wave_progress), z)
    self.play(Homotopy(homotopy, square, rate_func= linear, run_time=2))

```
Copy to clipboard
Make interactive
Methods
`function_at_time_t`  
---  
`interpolate_submobject`  
Attributes
`run_time`  
---  
_original__init__(_homotopy_ , _mobject_ , _run_time =3_, _apply_function_kwargs =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.Homotopy._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **homotopy** (_Callable_ _[__[__float_ _,__float_ _,__float_ _,__float_ _]__,__tuple_ _[__float_ _,__float_ _,__float_ _]__]_)
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **run_time** (_float_)
  * **apply_function_kwargs** (_dict_ _[__str_ _,__Any_ _]__|__None_)


Return type:
    
None
[ Next MoveAlongPath ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.MoveAlongPath.html>) [ Previous ComplexHomotopy ](https://docs.manim.community/en/stable/reference/<manim.animation.movement.ComplexHomotopy.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Homotopy](https://docs.manim.community/en/stable/reference/<#>)
    * `[Homotopy`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.Homotopy>)
      * `[Homotopy._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.movement.Homotopy._original__init__>)


