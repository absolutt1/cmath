# AnnularSector[¶](https://docs.manim.community/en/stable/reference/<#annularsector> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.AnnularSector`
_class_ AnnularSector(_inner_radius =1_, _outer_radius =2_, _angle =1.5707963267948966_, _start_angle =0_, _fill_opacity =1_, _stroke_width =0_, _color =ManimColor('#FFFFFF')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#AnnularSector>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector> "Link to this definition")
    
Bases: `[Arc`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc> "manim.mobject.geometry.arc.Arc")
A sector of an annulus.
Parameters:
    
  * **inner_radius** (_float_) – The inside radius of the Annular Sector.
  * **outer_radius** (_float_) – The outside radius of the Annular Sector.
  * **angle** (_float_) – The clockwise angle of the Annular Sector.
  * **start_angle** (_float_) – The starting clockwise angle of the Annular Sector.
  * **fill_opacity** (_float_) – The opacity of the color filled in the Annular Sector.
  * **stroke_width** (_float_) – The stroke width of the Annular Sector.
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color filled into the Annular Sector.
  * **kwargs** (_Any_)


Examples
Example: AnnularSectorExample [¶](https://docs.manim.community/en/stable/reference/<#annularsectorexample>)
![../_images/AnnularSectorExample-1.png](https://docs.manim.community/en/stable/_images/AnnularSectorExample-1.png)
```
frommanimimport *
classAnnularSectorExample(Scene):
  defconstruct(self):
    # Changes background color to clearly visualize changes in fill_opacity.
    self.camera.background_color = WHITE
    # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
    s1 = AnnularSector(color=YELLOW).move_to(2 * UL)
    # Different inner_radius and outer_radius than the default.
    s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 * DEGREES, color=RED).move_to(2 * UR)
    # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
    s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 * DL)
    # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
    s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 * PI / 2, color=GREEN).move_to(2 * DR)
    self.add(s1, s2, s3, s4)

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.generate_points> "manim.mobject.geometry.arc.AnnularSector.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`[init_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.init_points> "manim.mobject.geometry.arc.AnnularSector.init_points") | Initializes `points` and therefore the shape.  
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
_original__init__(_inner_radius =1_, _outer_radius =2_, _angle =1.5707963267948966_, _start_angle =0_, _fill_opacity =1_, _stroke_width =0_, _color =ManimColor('#FFFFFF')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **inner_radius** (_float_)
  * **outer_radius** (_float_)
  * **angle** (_float_)
  * **start_angle** (_float_)
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **kwargs** (_Any_)


Return type:
    
None
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#AnnularSector.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
init_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.init_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
[ Next Annulus ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Annulus.html>) [ Previous AnnotationDot ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.AnnotationDot.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [AnnularSector](https://docs.manim.community/en/stable/reference/<#>)
    * `[AnnularSector`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector>)
      * `[AnnularSector._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector._original__init__>)
      * `[AnnularSector.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.generate_points>)
      * `[AnnularSector.init_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.AnnularSector.init_points>)


