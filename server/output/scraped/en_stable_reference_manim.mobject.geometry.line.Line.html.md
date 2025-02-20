# Line[¶](https://docs.manim.community/en/stable/reference/<#line> "Link to this heading")
Qualified name: `manim.mobject.geometry.line.Line`
_class_ Line(_start =array([-1., 0., 0.])_, _end =array([1., 0., 0.])_, _buff =0_, _path_arc =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line> "Link to this definition")
    
Bases: `[TipableVMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject> "manim.mobject.geometry.arc.TipableVMobject")
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.generate_points> "manim.mobject.geometry.line.Line.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`get_angle`  
`[get_projection`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.get_projection> "manim.mobject.geometry.line.Line.get_projection") | Returns the projection of a point onto a line.  
`get_slope`  
`get_unit_vector`  
`get_vector`  
`[init_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.init_points> "manim.mobject.geometry.line.Line.init_points") | Initializes `points` and therefore the shape.  
`[put_start_and_end_on`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.put_start_and_end_on> "manim.mobject.geometry.line.Line.put_start_and_end_on") | Sets starts and end coordinates of a line.  
`set_angle`  
`set_length`  
`set_path_arc`  
`[set_points_by_ends`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.set_points_by_ends> "manim.mobject.geometry.line.Line.set_points_by_ends") | Sets the points of the line based on its start and end points.  
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
    
  * **start** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **end** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **buff** (_float_)
  * **path_arc** (_float_ _|__None_)
  * **kwargs** (_Any_)


_original__init__(_start =array([-1., 0., 0.])_, _end =array([1., 0., 0.])_, _buff =0_, _path_arc =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **start** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **end** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **buff** (_float_)
  * **path_arc** (_float_ _|__None_)
  * **kwargs** (_Any_)


Return type:
    
None
_pointify(_mob_or_point_ , _direction =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line._pointify>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line._pointify> "Link to this definition")
    
Transforms a mobject into its corresponding point. Does nothing if a point is passed.
`direction` determines the location of the point along its bounding box in that direction.
Parameters:
    
  * **mob_or_point** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The mobject or point.
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") _|__None_) – The direction.


Return type:
    
[Point3D](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
get_projection(_point_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line.get_projection>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.get_projection> "Link to this definition")
    
Returns the projection of a point onto a line.
Parameters:
    
**point** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The point to which the line is projected.
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
init_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.init_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
put_start_and_end_on(_start_ , _end_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line.put_start_and_end_on>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.put_start_and_end_on> "Link to this definition")
    
Sets starts and end coordinates of a line.
Examples
Example: LineExample [¶](https://docs.manim.community/en/stable/reference/<#lineexample>)
```
frommanimimport *
classLineExample(Scene):
  defconstruct(self):
    d = VGroup()
    for i in range(0,10):
      d.add(Dot())
    d.arrange_in_grid(buff=1)
    self.add(d)
    l= Line(d[0], d[1])
    self.add(l)
    self.wait()
    l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
    self.wait()
    l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
    self.wait()

```
Copy to clipboard
Make interactive
Parameters:
    
  * **start** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **end** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))


Return type:
    
Self
set_points_by_ends(_start_ , _end_ , _buff =0_, _path_arc =0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Line.set_points_by_ends>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.set_points_by_ends> "Link to this definition")
    
Sets the points of the line based on its start and end points. Unlike `[put_start_and_end_on()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.put_start_and_end_on> "manim.mobject.geometry.line.Line.put_start_and_end_on"), this method respects self.buff and Mobject bounding boxes.
Parameters:
    
  * **start** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The start point or Mobject of the line.
  * **end** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The end point or Mobject of the line.
  * **buff** (_float_) – The empty space between the start and end of the line, by default 0.
  * **path_arc** (_float_) – The angle of a circle spanned by this arc, by default 0 which is a straight line.


Return type:
    
None
[ Next RightAngle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.RightAngle.html>) [ Previous Elbow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Elbow.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Line](https://docs.manim.community/en/stable/reference/<#>)
    * `[Line`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line>)
      * `[Line._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line._original__init__>)
      * `[Line._pointify()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line._pointify>)
      * `[Line.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.generate_points>)
      * `[Line.get_projection()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.get_projection>)
      * `[Line.init_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.init_points>)
      * `[Line.put_start_and_end_on()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.put_start_and_end_on>)
      * `[Line.set_points_by_ends()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Line.set_points_by_ends>)


