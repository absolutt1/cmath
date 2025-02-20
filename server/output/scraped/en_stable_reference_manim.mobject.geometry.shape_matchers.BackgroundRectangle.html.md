# BackgroundRectangle[¶](https://docs.manim.community/en/stable/reference/<#backgroundrectangle> "Link to this heading")
Qualified name: `manim.mobject.geometry.shape\_matchers.BackgroundRectangle`
_class_ BackgroundRectangle(_* mobjects_, _color =None_, _stroke_width =0_, _stroke_opacity =0_, _fill_opacity =0.75_, _buff =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle> "Link to this definition")
    
Bases: `[SurroundingRectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle> "manim.mobject.geometry.shape_matchers.SurroundingRectangle")
A background rectangle. Its default color is the background color of the scene.
Examples
Example: ExampleBackgroundRectangle [¶](https://docs.manim.community/en/stable/reference/<#examplebackgroundrectangle>)
![../_images/ExampleBackgroundRectangle-1.png](https://docs.manim.community/en/stable/_images/ExampleBackgroundRectangle-1.png)
```
frommanimimport *
classExampleBackgroundRectangle(Scene):
  defconstruct(self):
    circle = Circle().shift(LEFT)
    circle.set_stroke(color=GREEN, width=20)
    triangle = Triangle().shift(2 * RIGHT)
    triangle.set_fill(PINK, opacity=0.5)
    backgroundRectangle1 = BackgroundRectangle(circle, color=WHITE, fill_opacity=0.15)
    backgroundRectangle2 = BackgroundRectangle(triangle, color=WHITE, fill_opacity=0.15)
    self.add(backgroundRectangle1)
    self.add(backgroundRectangle2)
    self.add(circle)
    self.add(triangle)
    self.play(Rotate(backgroundRectangle1, PI / 4))
    self.play(Rotate(backgroundRectangle2, PI / 2))

```
Copy to clipboard
Make interactive
Methods
`[get_fill_color`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color> "manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color") | If there are multiple colors (for gradient) this returns the first one  
---|---  
`[pointwise_become_partial`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial> "manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial") | Given a 2nd `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") `vmobject`, a lower bound `a` and an upper bound `b`, modify this `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")'s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`.  
`set_style`  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **stroke_width** (_float_)
  * **stroke_opacity** (_float_)
  * **fill_opacity** (_float_)
  * **buff** (_float_)
  * **kwargs** (_Any_)


_original__init__(_* mobjects_, _color =None_, _stroke_width =0_, _stroke_opacity =0_, _fill_opacity =0.75_, _buff =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **stroke_width** (_float_)
  * **stroke_opacity** (_float_)
  * **fill_opacity** (_float_)
  * **buff** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
get_fill_color()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle.get_fill_color>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color> "Link to this definition")
    
If there are multiple colors (for gradient) this returns the first one
Return type:
    
[_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor")
pointwise_become_partial(_mobject_ , _a_ , _b_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle.pointwise_become_partial>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial> "Link to this definition")
    
Given a 2nd `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") `vmobject`, a lower bound `a` and an upper bound `b`, modify this `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")’s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`.
Parameters:
    
  * **vmobject** – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") that will serve as a model.
  * **a** (_Any_) – The lower bound for `t`.
  * **b** (_float_) – The upper bound for `t`
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


Returns:
    
The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") itself, after the transformation.
Return type:
    
`[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
Raises:
    
**TypeError** – If `vmobject` is not an instance of `VMobject`.
[ Next Cross ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.Cross.html>) [ Previous shape_matchers ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [BackgroundRectangle](https://docs.manim.community/en/stable/reference/<#>)
    * `[BackgroundRectangle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle>)
      * `[BackgroundRectangle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle._original__init__>)
      * `[BackgroundRectangle.get_fill_color()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color>)
      * `[BackgroundRectangle.pointwise_become_partial()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial>)


