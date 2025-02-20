# ValueTracker[¶](https://docs.manim.community/en/stable/reference/<#valuetracker> "Link to this heading")
Qualified name: `manim.mobject.value\_tracker.ValueTracker`
_class_ ValueTracker(_value =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ValueTracker>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker> "Link to this definition")
    
Bases: `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
A mobject that can be used for tracking (real-valued) parameters. Useful for animating parameter changes.
Not meant to be displayed. Instead the position encodes some number, often one which another animation or continual_animation uses for its update function, and by treating it as a mobject it can still be animated and manipulated just like anything else.
This value changes continuously when animated using the `animate` syntax.
Examples
Example: ValueTrackerExample [¶](https://docs.manim.community/en/stable/reference/<#valuetrackerexample>)
```
frommanimimport *
classValueTrackerExample(Scene):
  defconstruct(self):
    number_line = NumberLine()
    pointer = Vector(DOWN)
    label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))
    tracker = ValueTracker(0)
    pointer.add_updater(
      lambda m: m.next_to(
            number_line.n2p(tracker.get_value()),
            UP
          )
    )
    self.add(number_line, pointer,label)
    tracker += 1.5
    self.wait(1)
    tracker -= 4
    self.wait(0.5)
    self.play(tracker.animate.set_value(5))
    self.wait(0.5)
    self.play(tracker.animate.set_value(3))
    self.play(tracker.animate.increment_value(-2))
    self.wait(0.5)

```
Copy to clipboard
Make interactive
Note
You can also link ValueTrackers to updaters. In this case, you have to make sure that the ValueTracker is added to the scene by `add`
Example: ValueTrackerExample [¶](https://docs.manim.community/en/stable/reference/<#valuetrackerexample>)
```
frommanimimport *
classValueTrackerExample(Scene):
  defconstruct(self):
    tracker = ValueTracker(0)
    label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
    self.add(label)
    self.add(tracker)
    tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
    self.wait(2)

```
Copy to clipboard
Make interactive
Methods
`[get_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.get_value> "manim.mobject.value_tracker.ValueTracker.get_value") | Get the current value of this ValueTracker.  
---|---  
`[increment_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.increment_value> "manim.mobject.value_tracker.ValueTracker.increment_value") | Increments (adds) a scalar value to the ValueTracker  
`[interpolate`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.interpolate> "manim.mobject.value_tracker.ValueTracker.interpolate") | Turns self into an interpolation between mobject1 and mobject2.  
`[set_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.set_value> "manim.mobject.value_tracker.ValueTracker.set_value") | Sets a new scalar value to the ValueTracker  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`depth` | The depth of the mobject.  
`height` | The height of the mobject.  
`width` | The width of the mobject.  
_original__init__(_value =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
get_value()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ValueTracker.get_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.get_value> "Link to this definition")
    
Get the current value of this ValueTracker.
Return type:
    
float
increment_value(_d_value_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ValueTracker.increment_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.increment_value> "Link to this definition")
    
Increments (adds) a scalar value to the ValueTracker
Parameters:
    
**d_value** (_float_)
interpolate(_mobject1_ , _mobject2_ , _alpha_ , _path_func= <function interpolate>_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ValueTracker.interpolate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.interpolate> "Link to this definition")
    
Turns self into an interpolation between mobject1 and mobject2.
set_value(_value_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ValueTracker.set_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.set_value> "Link to this definition")
    
Sets a new scalar value to the ValueTracker
Parameters:
    
**value** (_float_)
[ Next vector_field ](https://docs.manim.community/en/stable/reference/<manim.mobject.vector_field.html>) [ Previous ComplexValueTracker ](https://docs.manim.community/en/stable/reference/<manim.mobject.value_tracker.ComplexValueTracker.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ValueTracker](https://docs.manim.community/en/stable/reference/<#>)
    * `[ValueTracker`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker>)
      * `[ValueTracker._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker._original__init__>)
      * `[ValueTracker.get_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.get_value>)
      * `[ValueTracker.increment_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.increment_value>)
      * `[ValueTracker.interpolate()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.interpolate>)
      * `[ValueTracker.set_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ValueTracker.set_value>)


