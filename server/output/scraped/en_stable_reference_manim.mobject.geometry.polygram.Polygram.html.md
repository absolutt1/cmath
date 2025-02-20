# Polygram[¶](https://docs.manim.community/en/stable/reference/<#polygram> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Polygram`
_class_ Polygram(_* vertex_groups_, _color =ManimColor('#58C4DD')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Polygram>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A generalized `[Polygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon"), allowing for disconnected sets of edges.
Parameters:
    
  * **vertex_groups** ([_Point3DLike_Array_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")) – 
The groups of vertices making up the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
The first vertex in each group is repeated to close the shape. Each point must be 3-dimensional: `[x,y,z]`
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
  * **kwargs** (_Any_) – Forwarded to the parent constructor.


Examples
Example: PolygramExample [¶](https://docs.manim.community/en/stable/reference/<#polygramexample>)
```
frommanimimport *
importnumpyasnp
classPolygramExample(Scene):
  defconstruct(self):
    hexagram = Polygram(
      [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
      [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
    )
    self.add(hexagram)
    dot = Dot()
    self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
    self.remove(dot)
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`[get_vertex_groups`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertex_groups> "manim.mobject.geometry.polygram.Polygram.get_vertex_groups") | Gets the vertex groups of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").  
---|---  
`[get_vertices`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertices> "manim.mobject.geometry.polygram.Polygram.get_vertices") | Gets the vertices of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").  
`[round_corners`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.round_corners> "manim.mobject.geometry.polygram.Polygram.round_corners") | Rounds off the corners of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").  
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
_original__init__(_* vertex_groups_, _color =ManimColor('#58C4DD')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vertex_groups** ([_Point3DLike_Array_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array"))
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **kwargs** (_Any_)


get_vertex_groups()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Polygram.get_vertex_groups>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertex_groups> "Link to this definition")
    
Gets the vertex groups of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
Returns:
    
The vertex groups of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
Return type:
    
`numpy.ndarray`
Examples
```
>>> poly = Polygram([ORIGIN, RIGHT, UP], [LEFT, LEFT + UP, 2 * LEFT])
>>> poly.get_vertex_groups()
array([[[ 0., 0., 0.],
    [ 1., 0., 0.],
    [ 0., 1., 0.]],
    [[-1., 0., 0.],
    [-1., 1., 0.],
    [-2., 0., 0.]]])

```
Copy to clipboard
get_vertices()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Polygram.get_vertices>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertices> "Link to this definition")
    
Gets the vertices of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
Returns:
    
The vertices of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
Return type:
    
`numpy.ndarray`
Examples
```
>>> sq = Square()
>>> sq.get_vertices()
array([[ 1., 1., 0.],
    [-1., 1., 0.],
    [-1., -1., 0.],
    [ 1., -1., 0.]])

```
Copy to clipboard
round_corners(_radius =0.5_, _evenly_distribute_anchors =False_, _components_per_rounded_corner =2_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Polygram.round_corners>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.round_corners> "Link to this definition")
    
Rounds off the corners of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
Parameters:
    
  * **radius** (_float_ _|__list_ _[__float_ _]_) – The curvature of the corners of the `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram").
  * **evenly_distribute_anchors** (_bool_) – Break long line segments into proportionally-sized segments.
  * **components_per_rounded_corner** (_int_) – The number of points used to represent the rounded corner curve.


Return type:
    
Self
See also
`RoundedRectangle`
Note
If radius is supplied as a single value, then the same radius will be applied to all corners. If radius is a list, then the individual values will be applied sequentially, with the first corner receiving radius[0], the second corner receiving radius[1], etc. The radius list will be repeated as necessary.
The components_per_rounded_corner value is provided so that the fidelity of the rounded corner may be fine-tuned as needed. 2 is an appropriate value for most shapes, however a larger value may be need if the rounded corner is particularly large. 2 is the minimum number allowed, representing the start and end of the curve. 3 will result in a start, middle, and end point, meaning 2 curves will be generated.
The option to evenly_distribute_anchors is provided so that the line segments (the part part of each line remaining after rounding off the corners) can be subdivided to a density similar to that of the average density of the rounded corners. This may be desirable in situations in which an even distribution of curves is desired for use in later transformation animations. Be aware, though, that enabling this option can result in an an object containing significantly more points than the original, especially when the rounded corner curves are small.
Examples
Example: PolygramRoundCorners [¶](https://docs.manim.community/en/stable/reference/<#polygramroundcorners>)
![../_images/PolygramRoundCorners-1.png](https://docs.manim.community/en/stable/_images/PolygramRoundCorners-1.png)
```
frommanimimport *
classPolygramRoundCorners(Scene):
  defconstruct(self):
    star = Star(outer_radius=2)
    shapes = VGroup(star)
    shapes.add(star.copy().round_corners(radius=0.1))
    shapes.add(star.copy().round_corners(radius=0.25))
    shapes.arrange(RIGHT)
    self.add(shapes)

```
Copy to clipboard
Make interactive
[ Next Rectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html>) [ Previous Polygon ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Polygram](https://docs.manim.community/en/stable/reference/<#>)
    * `[Polygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram>)
      * `[Polygram._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram._original__init__>)
      * `[Polygram.get_vertex_groups()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertex_groups>)
      * `[Polygram.get_vertices()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.get_vertices>)
      * `[Polygram.round_corners()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygram.round_corners>)


