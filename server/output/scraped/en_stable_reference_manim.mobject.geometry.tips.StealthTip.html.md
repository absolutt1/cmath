# StealthTip[¶](https://docs.manim.community/en/stable/reference/<#stealthtip> "Link to this heading")
Qualified name: `manim.mobject.geometry.tips.StealthTip`
_class_ StealthTip(_fill_opacity =1_, _stroke_width =3_, _length =0.175_, _start_angle =3.141592653589793_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/tips.html#StealthTip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip> "Link to this definition")
    
Bases: `[ArrowTip`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip")
‘Stealth’ fighter / kite arrow shape.
Naming is inspired by the corresponding [TikZ arrow shape](https://docs.manim.community/en/stable/reference/<https:/tikz.dev/tikz-arrows#sec-16.3>).
Methods
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`base` | The base point of the arrow tip.  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`[length`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip.length> "manim.mobject.geometry.tips.StealthTip.length") | The length of the arrow tip.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`tip_angle` | The angle of the arrow tip.  
`tip_point` | The tip point of the arrow tip.  
`vector` | The vector pointing from the base point to the tip point.  
`width` | The width of the mobject.  
Parameters:
    
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **length** (_float_)
  * **start_angle** (_float_)
  * **kwargs** (_Any_)


_original__init__(_fill_opacity =1_, _stroke_width =3_, _length =0.175_, _start_angle =3.141592653589793_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **length** (_float_)
  * **start_angle** (_float_)
  * **kwargs** (_Any_)


_property_ length _: float_[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip.length> "Link to this definition")
    
The length of the arrow tip.
In this case, the length is computed as the height of the triangle encompassing the stealth tip (otherwise, the tip is scaled too large).
[ Next graph ](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.html>) [ Previous ArrowTriangleTip ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTriangleTip.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [StealthTip](https://docs.manim.community/en/stable/reference/<#>)
    * `[StealthTip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip>)
      * `[StealthTip._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip._original__init__>)
      * `[StealthTip.length`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.tips.StealthTip.length>)


