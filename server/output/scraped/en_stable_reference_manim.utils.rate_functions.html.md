
# rate_functions[¶](https://docs.manim.community/en/stable/reference/<#module-manim.utils.rate_functions> "Link to this heading")
A selection of rate functions, i.e., _speed curves_ for animations. Please find a standard list at <https://easings.net/>. Here is a picture for the non-standard ones
Example: RateFuncExample [¶](https://docs.manim.community/en/stable/reference/<#ratefuncexample>)
![../_images/RateFuncExample-1.png](https://docs.manim.community/en/stable/_images/RateFuncExample-1.png)
```
frommanimimport *
classRateFuncExample(Scene):
  defconstruct(self):
    x = VGroup()
    for k, v in rate_functions.__dict__.items():
      if "function" in str(v):
        if (
          not k.startswith("__")
          and not k.startswith("sqrt")
          and not k.startswith("bezier")
        ):
          try:
            rate_func = v
            plot = (
              ParametricFunction(
                lambda x: [x, rate_func(x), 0],
                t_range=[0, 1, .01],
                use_smoothing=False,
                color=YELLOW,
              )
              .stretch_to_fit_width(1.5)
              .stretch_to_fit_height(1)
            )
            plot_bg = SurroundingRectangle(plot).set_color(WHITE)
            plot_title = (
              Text(rate_func.__name__, weight=BOLD)
              .scale(0.5)
              .next_to(plot_bg, UP, buff=0.1)
            )
            x.add(VGroup(plot_bg, plot, plot_title))
          except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
            pass
    x.arrange_in_grid(cols=8)
    x.height = config.frame_height
    x.width = config.frame_width
    x.move_to(ORIGIN).scale(0.95)
    self.add(x)

```
Copy to clipboard
Make interactive
There are primarily 3 kinds of standard easing functions:
  1. Ease In - The animation has a smooth start.
  2. Ease Out - The animation has a smooth end.
  3. Ease In Out - The animation has a smooth start as well as smooth end.


Note
The standard functions are not exported, so to use them you do something like this: rate_func=rate_functions.ease_in_sine On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.
Example: RateFunctions1Example [¶](https://docs.manim.community/en/stable/reference/<#ratefunctions1example>)
```
frommanimimport *
classRateFunctions1Example(Scene):
  defconstruct(self):
    line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
    line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
    line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)
    dot1 = Dot().move_to(line1.get_left())
    dot2 = Dot().move_to(line2.get_left())
    dot3 = Dot().move_to(line3.get_left())
    label1 = Tex("Ease In").next_to(line1, RIGHT)
    label2 = Tex("Ease out").next_to(line2, RIGHT)
    label3 = Tex("Ease In Out").next_to(line3, RIGHT)
    self.play(
      FadeIn(VGroup(line1, line2, line3)),
      FadeIn(VGroup(dot1, dot2, dot3)),
      Write(VGroup(label1, label2, label3)),
    )
    self.play(
      MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
      MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
      MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
      run_time=7
    )
    self.wait()

```
Copy to clipboard
Make interactive
Classes
`[RateFunction`](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction")  
---  
Functions
double_smooth(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#double_smooth>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.double_smooth> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_back(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_back>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_back> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_bounce(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_bounce>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_bounce> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_circ(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_circ>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_circ> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_cubic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_cubic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_cubic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_elastic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_elastic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_elastic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_expo(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_expo>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_expo> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_back(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_back>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_back> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_bounce(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_bounce>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_bounce> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_circ(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_circ>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_circ> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_cubic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_cubic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_cubic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_elastic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_elastic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_elastic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_expo(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_expo>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_expo> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_quad(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_quad>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quad> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_quart(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_quart>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quart> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_quint(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_quint>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quint> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_out_sine(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_out_sine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_sine> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_quad(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_quad>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quad> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_quart(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_quart>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quart> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_quint(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_quint>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quint> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_in_sine(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_in_sine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_sine> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_back(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_back>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_back> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_bounce(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_bounce>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_bounce> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_circ(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_circ>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_circ> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_cubic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_cubic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_cubic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_elastic(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_elastic>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_elastic> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_expo(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_expo>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_expo> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_quad(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_quad>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quad> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_quart(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_quart>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quart> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_quint(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_quint>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quint> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
ease_out_sine(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#ease_out_sine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_sine> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
exponential_decay(_t_ , _half_life =0.1_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#exponential_decay>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.exponential_decay> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **half_life** (_float_)


Return type:
    
float
linear(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#linear>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.linear> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
lingering(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#lingering>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.lingering> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
not_quite_there(_func= <function smooth>_, _proportion=0.7_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#not_quite_there>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.not_quite_there> "Link to this definition")
    
Parameters:
    
  * **func** ([_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction"))
  * **proportion** (_float_)


Return type:
    
[_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction")
running_start(_t_ , _pull_factor =-0.5_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#running_start>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.running_start> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **pull_factor** (_float_)


Return type:
    
float
rush_from(_t_ , _inflection =10.0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#rush_from>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.rush_from> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **inflection** (_float_)


Return type:
    
float
rush_into(_t_ , _inflection =10.0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#rush_into>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.rush_into> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **inflection** (_float_)


Return type:
    
float
slow_into(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#slow_into>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.slow_into> "Link to this definition")
    
Parameters:
    
**t** (_float_)
Return type:
    
float
smooth(_t_ , _inflection =10.0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#smooth>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smooth> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **inflection** (_float_)


Return type:
    
float
smoothererstep(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#smoothererstep>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smoothererstep> "Link to this definition")
    
Implementation of the 3rd order SmoothStep sigmoid function. The 1st, 2nd and 3rd derivatives (speed, acceleration and jerk) are zero at the endpoints. <https://en.wikipedia.org/wiki/Smoothstep>
Parameters:
    
**t** (_float_)
Return type:
    
float
smootherstep(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#smootherstep>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smootherstep> "Link to this definition")
    
Implementation of the 2nd order SmoothStep sigmoid function. The 1st and 2nd derivatives (speed and acceleration) are zero at the endpoints. <https://en.wikipedia.org/wiki/Smoothstep>
Parameters:
    
**t** (_float_)
Return type:
    
float
smoothstep(_t_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#smoothstep>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smoothstep> "Link to this definition")
    
Implementation of the 1st order SmoothStep sigmoid function. The 1st derivative (speed) is zero at the endpoints. <https://en.wikipedia.org/wiki/Smoothstep>
Parameters:
    
**t** (_float_)
Return type:
    
float
squish_rate_func(_func_ , _a =0.4_, _b =0.6_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#squish_rate_func>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.squish_rate_func> "Link to this definition")
    
Parameters:
    
  * **func** ([_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction"))
  * **a** (_float_)
  * **b** (_float_)


Return type:
    
[_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction")
there_and_back(_t_ , _inflection =10.0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#there_and_back>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.there_and_back> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **inflection** (_float_)


Return type:
    
float
there_and_back_with_pause(_t_ , _pause_ratio =0.3333333333333333_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#there_and_back_with_pause>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.there_and_back_with_pause> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **pause_ratio** (_float_)


Return type:
    
float
unit_interval(_function_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#unit_interval>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.unit_interval> "Link to this definition")
    
Parameters:
    
**function** ([_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction"))
Return type:
    
[_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction")
wiggle(_t_ , _wiggles =2_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#wiggle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.wiggle> "Link to this definition")
    
Parameters:
    
  * **t** (_float_)
  * **wiggles** (_float_)


Return type:
    
float
zero(_function_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/rate_functions.html#zero>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.zero> "Link to this definition")
    
Parameters:
    
**function** ([_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction"))
Return type:
    
[_RateFunction_](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction> "manim.utils.rate_functions.RateFunction")
[ Next RateFunction ](https://docs.manim.community/en/stable/reference/<manim.utils.rate_functions.RateFunction.html>) [ Previous paths ](https://docs.manim.community/en/stable/reference/<manim.utils.paths.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [rate_functions](https://docs.manim.community/en/stable/reference/<#>)
    * `[double_smooth()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.double_smooth>)
    * `[ease_in_back()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_back>)
    * `[ease_in_bounce()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_bounce>)
    * `[ease_in_circ()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_circ>)
    * `[ease_in_cubic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_cubic>)
    * `[ease_in_elastic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_elastic>)
    * `[ease_in_expo()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_expo>)
    * `[ease_in_out_back()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_back>)
    * `[ease_in_out_bounce()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_bounce>)
    * `[ease_in_out_circ()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_circ>)
    * `[ease_in_out_cubic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_cubic>)
    * `[ease_in_out_elastic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_elastic>)
    * `[ease_in_out_expo()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_expo>)
    * `[ease_in_out_quad()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quad>)
    * `[ease_in_out_quart()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quart>)
    * `[ease_in_out_quint()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_quint>)
    * `[ease_in_out_sine()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_out_sine>)
    * `[ease_in_quad()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quad>)
    * `[ease_in_quart()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quart>)
    * `[ease_in_quint()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_quint>)
    * `[ease_in_sine()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_in_sine>)
    * `[ease_out_back()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_back>)
    * `[ease_out_bounce()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_bounce>)
    * `[ease_out_circ()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_circ>)
    * `[ease_out_cubic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_cubic>)
    * `[ease_out_elastic()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_elastic>)
    * `[ease_out_expo()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_expo>)
    * `[ease_out_quad()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quad>)
    * `[ease_out_quart()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quart>)
    * `[ease_out_quint()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_quint>)
    * `[ease_out_sine()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.ease_out_sine>)
    * `[exponential_decay()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.exponential_decay>)
    * `[linear()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.linear>)
    * `[lingering()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.lingering>)
    * `[not_quite_there()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.not_quite_there>)
    * `[running_start()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.running_start>)
    * `[rush_from()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.rush_from>)
    * `[rush_into()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.rush_into>)
    * `[slow_into()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.slow_into>)
    * `[smooth()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smooth>)
    * `[smoothererstep()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smoothererstep>)
    * `[smootherstep()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smootherstep>)
    * `[smoothstep()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.smoothstep>)
    * `[squish_rate_func()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.squish_rate_func>)
    * `[there_and_back()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.there_and_back>)
    * `[there_and_back_with_pause()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.there_and_back_with_pause>)
    * `[unit_interval()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.unit_interval>)
    * `[wiggle()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.wiggle>)
    * `[zero()`](https://docs.manim.community/en/stable/reference/<#manim.utils.rate_functions.zero>)


