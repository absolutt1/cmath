# Dot[¶](https://docs.manim.community/en/stable/reference/<#dot> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.Dot`
_class_ Dot(_point =array([0., 0., 0.])_, _radius =0.08_, _stroke_width =0_, _fill_opacity =1.0_, _color =ManimColor('#FFFFFF')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Dot>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Dot> "Link to this definition")
    
Bases: `[Circle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")
A circle with a very small radius.
Parameters:
    
  * **point** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The location of the dot.
  * **radius** (_float_) – The radius of the dot.
  * **stroke_width** (_float_) – The thickness of the outline of the dot.
  * **fill_opacity** (_float_) – The opacity of the dot’s fill_colour
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the dot.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Circle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")


Examples
Example: DotExample [¶](https://docs.manim.community/en/stable/reference/<#dotexample>)
![../_images/DotExample-1.png](https://docs.manim.community/en/stable/_images/DotExample-1.png)
```
frommanimimport *
classDotExample(Scene):
  defconstruct(self):
    dot1 = Dot(point=LEFT, radius=0.08)
    dot2 = Dot(point=ORIGIN)
    dot3 = Dot(point=RIGHT)
    self.add(dot1,dot2,dot3)

```
Copy to clipboard
Make interactive
Methods
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
_original__init__(_point =array([0., 0., 0.])_, _radius =0.08_, _stroke_width =0_, _fill_opacity =1.0_, _color =ManimColor('#FFFFFF')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Dot._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **point** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **radius** (_float_)
  * **stroke_width** (_float_)
  * **fill_opacity** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Ellipse ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Ellipse.html>) [ Previous CurvedDoubleArrow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.CurvedDoubleArrow.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Dot](https://docs.manim.community/en/stable/reference/<#>)
    * `[Dot`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Dot>)
      * `[Dot._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Dot._original__init__>)


