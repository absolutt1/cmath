# VMobjectFromSVGPath[¶](https://docs.manim.community/en/stable/reference/<#vmobjectfromsvgpath> "Link to this heading")
Qualified name: `manim.mobject.svg.svg\_mobject.VMobjectFromSVGPath`
_class_ VMobjectFromSVGPath(_path_obj_ , _long_lines =False_, _should_subdivide_sharp_curves =False_, _should_remove_null_curves =False_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#VMobjectFromSVGPath>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A vectorized mobject representing an SVG path.
Note
The `long_lines`, `should_subdivide_sharp_curves`, and `should_remove_null_curves` keyword arguments are only respected with the OpenGL renderer.
Parameters:
    
  * **path_obj** (_se.Path_) – A parsed SVG path object.
  * **long_lines** (_bool_) – Whether or not straight lines in the vectorized mobject are drawn in one or two segments.
  * **should_subdivide_sharp_curves** (_bool_) – Whether or not to subdivide subcurves further in case two segments meet at an angle that is sharper than a given threshold.
  * **should_remove_null_curves** (_bool_) – Whether or not to remove subcurves of length 0.
  * **kwargs** – Further keyword arguments are passed to the parent class.


Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points> "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`handle_commands`  
`init_points`  
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
_original__init__(_path_obj_ , _long_lines =False_, _should_subdivide_sharp_curves =False_, _should_remove_null_curves =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **path_obj** (_Path_)
  * **long_lines** (_bool_)
  * **should_subdivide_sharp_curves** (_bool_)
  * **should_remove_null_curves** (_bool_)


generate_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
[ Next table ](https://docs.manim.community/en/stable/reference/<manim.mobject.table.html>) [ Previous SVGMobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.SVGMobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [VMobjectFromSVGPath](https://docs.manim.community/en/stable/reference/<#>)
    * `[VMobjectFromSVGPath`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath>)
      * `[VMobjectFromSVGPath._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath._original__init__>)
      * `[VMobjectFromSVGPath.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points>)


