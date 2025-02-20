# Circle[¶](https://docs.manim.community/en/stable/reference/<#circle> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.Circle`
_class_ Circle(_radius =None_, _color =ManimColor('#FC6255')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Circle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle> "Link to this definition")
    
Bases: `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc")
A circle.
Parameters:
    
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the shape.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc")
  * **radius** (_float_ _|__None_)


Examples
Example: CircleExample [¶](https://docs.manim.community/en/stable/reference/<#circleexample>)
![../_images/CircleExample-1.png](https://docs.manim.community/en/stable/_images/CircleExample-1.png)
```
frommanimimport *
classCircleExample(Scene):
  defconstruct(self):
    circle_1 = Circle(radius=1.0)
    circle_2 = Circle(radius=1.5, color=GREEN)
    circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)
    circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
    self.add(circle_group)

```
Copy to clipboard
Make interactive
Methods
`[from_three_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.from_three_points> "manim.mobject.geometry.arc.Circle.from_three_points") | Returns a circle passing through the specified three points.  
---|---  
`[point_at_angle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.point_at_angle> "manim.mobject.geometry.arc.Circle.point_at_angle") | Returns the position of a point on the circle.  
`[surround`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.surround> "manim.mobject.geometry.arc.Circle.surround") | Modifies a circle so that it surrounds a given mobject.  
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
_original__init__(_radius =None_, _color =ManimColor('#FC6255')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **radius** (_float_ _|__None_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **kwargs** (_Any_)


Return type:
    
None
_static_ from_three_points(_p1_ , _p2_ , _p3_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Circle.from_three_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.from_three_points> "Link to this definition")
    
Returns a circle passing through the specified three points.
Example
Example: CircleFromPointsExample [¶](https://docs.manim.community/en/stable/reference/<#circlefrompointsexample>)
![../_images/CircleFromPointsExample-1.png](https://docs.manim.community/en/stable/_images/CircleFromPointsExample-1.png)
```
frommanimimport *
classCircleFromPointsExample(Scene):
  defconstruct(self):
    circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
    dots = VGroup(
      Dot(LEFT),
      Dot(LEFT + UP),
      Dot(UP * 2),
    )
    self.add(NumberPlane(), circle, dots)

```
Copy to clipboard
Make interactive
Parameters:
    
  * **p1** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **p2** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **p3** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


Return type:
    
[Circle](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")
point_at_angle(_angle_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Circle.point_at_angle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.point_at_angle> "Link to this definition")
    
Returns the position of a point on the circle.
Parameters:
    
**angle** (_float_) – The angle of the point along the circle in radians.
Returns:
    
The location of the point along the circle’s circumference.
Return type:
    
`numpy.ndarray`
Examples
Example: PointAtAngleExample [¶](https://docs.manim.community/en/stable/reference/<#pointatangleexample>)
![../_images/PointAtAngleExample-1.png](https://docs.manim.community/en/stable/_images/PointAtAngleExample-1.png)
```
frommanimimport *
classPointAtAngleExample(Scene):
  defconstruct(self):
    circle = Circle(radius=2.0)
    p1 = circle.point_at_angle(PI/2)
    p2 = circle.point_at_angle(270*DEGREES)
    s1 = Square(side_length=0.25).move_to(p1)
    s2 = Square(side_length=0.25).move_to(p2)
    self.add(circle, s1, s2)

```
Copy to clipboard
Make interactive
surround(_mobject_ , _dim_to_match =0_, _stretch =False_, _buffer_factor =1.2_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Circle.surround>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.surround> "Link to this definition")
    
Modifies a circle so that it surrounds a given mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject that the circle will be surrounding.
  * **dim_to_match** (_int_)
  * **buffer_factor** (_float_) – Scales the circle with respect to the mobject. A buffer_factor < 1 makes the circle smaller than the mobject.
  * **stretch** (_bool_) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`


Return type:
    
Self
Examples
Example: CircleSurround [¶](https://docs.manim.community/en/stable/reference/<#circlesurround>)
![../_images/CircleSurround-1.png](https://docs.manim.community/en/stable/_images/CircleSurround-1.png)
```
frommanimimport *
classCircleSurround(Scene):
  defconstruct(self):
    triangle1 = Triangle()
    circle1 = Circle().surround(triangle1)
    group1 = Group(triangle1,circle1) # treat the two mobjects as one
    line2 = Line()
    circle2 = Circle().surround(line2, buffer_factor=2.0)
    group2 = Group(line2,circle2)
    # buffer_factor < 1, so the circle is smaller than the square
    square3 = Square()
    circle3 = Circle().surround(square3, buffer_factor=0.5)
    group3 = Group(square3, circle3)
    group = Group(group1, group2, group3).arrange(buff=1)
    self.add(group)

```
Copy to clipboard
Make interactive
[ Next CubicBezier ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.CubicBezier.html>) [ Previous ArcPolygonFromArcs ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.ArcPolygonFromArcs.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Circle](https://docs.manim.community/en/stable/reference/<#>)
    * `[Circle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle>)
      * `[Circle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle._original__init__>)
      * `[Circle.from_three_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.from_three_points>)
      * `[Circle.point_at_angle()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.point_at_angle>)
      * `[Circle.surround()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Circle.surround>)


