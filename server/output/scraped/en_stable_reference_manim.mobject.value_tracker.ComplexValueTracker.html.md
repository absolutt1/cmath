# ComplexValueTracker[¶](https://docs.manim.community/en/stable/reference/<#complexvaluetracker> "Link to this heading")
Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`
_class_ ComplexValueTracker(_value =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ComplexValueTracker>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker> "Link to this definition")
    
Bases: `[ValueTracker`](https://docs.manim.community/en/stable/reference/<manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker> "manim.mobject.value_tracker.ValueTracker")
Tracks a complex-valued parameter.
When the value is set through `animate`, the value will take a straight path from the source point to the destination point.
Examples
Example: ComplexValueTrackerExample [¶](https://docs.manim.community/en/stable/reference/<#complexvaluetrackerexample>)
```
frommanimimport *
classComplexValueTrackerExample(Scene):
  defconstruct(self):
    tracker = ComplexValueTracker(-2+1j)
    dot = Dot().add_updater(
      lambda x: x.move_to(tracker.points)
    )
    self.add(NumberPlane(), dot)
    self.play(tracker.animate.set_value(3+2j))
    self.play(tracker.animate.set_value(tracker.get_value() * 1j))
    self.play(tracker.animate.set_value(tracker.get_value() - 2j))
    self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

```
Copy to clipboard
Make interactive
Methods
`[get_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.get_value> "manim.mobject.value_tracker.ComplexValueTracker.get_value") | Get the current value of this value tracker as a complex number.  
---|---  
`[set_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.set_value> "manim.mobject.value_tracker.ComplexValueTracker.set_value") | Sets a new complex value to the ComplexValueTracker  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`depth` | The depth of the mobject.  
`height` | The height of the mobject.  
`width` | The width of the mobject.  
_original__init__(_value =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
get_value()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ComplexValueTracker.get_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.get_value> "Link to this definition")
    
Get the current value of this value tracker as a complex number.
The value is internally stored as a points array [a, b, 0]. This can be accessed directly to represent the value geometrically, see the usage example.
set_value(_z_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/value_tracker.html#ComplexValueTracker.set_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.set_value> "Link to this definition")
    
Sets a new complex value to the ComplexValueTracker
[ Next ValueTracker ](https://docs.manim.community/en/stable/reference/<manim.mobject.value_tracker.ValueTracker.html>) [ Previous value_tracker ](https://docs.manim.community/en/stable/reference/<manim.mobject.value_tracker.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ComplexValueTracker](https://docs.manim.community/en/stable/reference/<#>)
    * `[ComplexValueTracker`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker>)
      * `[ComplexValueTracker._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker._original__init__>)
      * `[ComplexValueTracker.get_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.get_value>)
      * `[ComplexValueTracker.set_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.value_tracker.ComplexValueTracker.set_value>)


