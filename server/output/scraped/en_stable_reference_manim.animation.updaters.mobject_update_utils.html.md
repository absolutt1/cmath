# mobject_update_utils[¶](https://docs.manim.community/en/stable/reference/<#module-manim.animation.updaters.mobject_update_utils> "Link to this heading")
Utility functions for continuous animation of mobjects.
Functions
always(_method_ , _* args_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#always>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always> "Link to this definition")
    
Parameters:
    
**method** (_Callable_)
Return type:
    
[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
always_redraw(_func_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#always_redraw>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_redraw> "Link to this definition")
    
Redraw the mobject constructed by a function every frame.
This function returns a mobject with an attached updater that continuously regenerates the mobject according to the specified function.
Parameters:
    
**func** (_Callable_ _[__[__]__,_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – A function without (required) input arguments that returns a mobject.
Return type:
    
[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: TangentAnimation [¶](https://docs.manim.community/en/stable/reference/<#tangentanimation>)
```
frommanimimport *
classTangentAnimation(Scene):
  defconstruct(self):
    ax = Axes()
    sine = ax.plot(np.sin, color=RED)
    alpha = ValueTracker(0)
    point = always_redraw(
      lambda: Dot(
        sine.point_from_proportion(alpha.get_value()),
        color=BLUE
      )
    )
    tangent = always_redraw(
      lambda: TangentLine(
        sine,
        alpha=alpha.get_value(),
        color=YELLOW,
        length=4
      )
    )
    self.add(ax, sine, point, tangent)
    self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)

```
Copy to clipboard
Make interactive
always_rotate(_mobject_ , _rate =0.3490658503988659_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#always_rotate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_rotate> "Link to this definition")
    
A mobject which is continuously rotated at a certain rate.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be rotated.
  * **rate** (_float_) – The angle which the mobject is rotated by over one second.
  * **kwags** – Further arguments to be passed to `[Mobject.rotate()`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate> "manim.mobject.mobject.Mobject.rotate").


Return type:
    
[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: SpinningTriangle [¶](https://docs.manim.community/en/stable/reference/<#spinningtriangle>)
```
frommanimimport *
classSpinningTriangle(Scene):
  defconstruct(self):
    tri = Triangle().set_fill(opacity=1).set_z_index(2)
    sq = Square().to_edge(LEFT)
    # will keep spinning while there is an animation going on
    always_rotate(tri, rate=2*PI, about_point=ORIGIN)
    self.add(tri, sq)
    self.play(sq.animate.to_edge(RIGHT), rate_func=linear, run_time=1)

```
Copy to clipboard
Make interactive
always_shift(_mobject_ , _direction =array([1., 0., 0.])_, _rate =0.1_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#always_shift>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_shift> "Link to this definition")
    
A mobject which is continuously shifted along some direction at a certain rate.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to shift.
  * **direction** (_ndarray_ _[__float64_ _]_) – The direction to shift. The vector is normalized, the specified magnitude is not relevant.
  * **rate** (_float_) – Length in Manim units which the mobject travels in one second along the specified direction.


Return type:
    
[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: ShiftingSquare [¶](https://docs.manim.community/en/stable/reference/<#shiftingsquare>)
```
frommanimimport *
classShiftingSquare(Scene):
  defconstruct(self):
    sq = Square().set_fill(opacity=1)
    tri = Triangle()
    VGroup(sq, tri).arrange(LEFT)
    # construct a square which is continuously
    # shifted to the right
    always_shift(sq, RIGHT, rate=5)
    self.add(sq)
    self.play(tri.animate.set_fill(opacity=1))

```
Copy to clipboard
Make interactive
assert_is_mobject_method(_method_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#assert_is_mobject_method>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.assert_is_mobject_method> "Link to this definition")
    
Parameters:
    
**method** (_Callable_)
Return type:
    
None
cycle_animation(_animation_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#cycle_animation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.cycle_animation> "Link to this definition")
    
Parameters:
    
**animation** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
Return type:
    
[Mobject](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
f_always(_method_ , _* arg_generators_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#f_always>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.f_always> "Link to this definition")
    
More functional version of always, where instead of taking in args, it takes in functions which output the relevant arguments.
Parameters:
    
**method** (_Callable_ _[__[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]__,__None_ _]_)
Return type:
    
[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
turn_animation_into_updater(_animation_ , _cycle =False_, _delay =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/updaters/mobject_update_utils.html#turn_animation_into_updater>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.turn_animation_into_updater> "Link to this definition")
    
Add an updater to the animation’s mobject which applies the interpolation and update functions of the animation
If cycle is True, this repeats over and over. Otherwise, the updater will be popped upon completion
The `delay` parameter is the delay (in seconds) before the animation starts..
Examples
Example: WelcomeToManim [¶](https://docs.manim.community/en/stable/reference/<#welcometomanim>)
```
frommanimimport *
classWelcomeToManim(Scene):
  defconstruct(self):
    words = Text("Welcome to")
    banner = ManimBanner().scale(0.5)
    VGroup(words, banner).arrange(DOWN)
    turn_animation_into_updater(Write(words, run_time=0.9))
    self.add(words)
    self.wait(0.5)
    self.play(banner.expand(), run_time=0.5)

```
Copy to clipboard
Make interactive
Parameters:
    
  * **animation** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **cycle** (_bool_)
  * **delay** (_float_)


Return type:
    
[Mobject](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
[ Next update ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.update.html>) [ Previous updaters ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [mobject_update_utils](https://docs.manim.community/en/stable/reference/<#>)
    * `[always()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always>)
    * `[always_redraw()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_redraw>)
    * `[always_rotate()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_rotate>)
    * `[always_shift()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.always_shift>)
    * `[assert_is_mobject_method()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.assert_is_mobject_method>)
    * `[cycle_animation()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.cycle_animation>)
    * `[f_always()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.f_always>)
    * `[turn_animation_into_updater()`](https://docs.manim.community/en/stable/reference/<#manim.animation.updaters.mobject_update_utils.turn_animation_into_updater>)


