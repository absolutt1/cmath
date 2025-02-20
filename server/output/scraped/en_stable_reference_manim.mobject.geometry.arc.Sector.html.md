# Sector[¶](https://docs.manim.community/en/stable/reference/<#sector> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.Sector`
_class_ Sector(_radius =1_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Sector>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Sector> "Link to this definition")
    
Bases: `[AnnularSector`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector> "manim.mobject.geometry.arc.AnnularSector")
A sector of a circle.
Examples
Example: ExampleSector [¶](https://docs.manim.community/en/stable/reference/<#examplesector>)
![../_images/ExampleSector-1.png](https://docs.manim.community/en/stable/_images/ExampleSector-1.png)
```
frommanimimport *
classExampleSector(Scene):
  defconstruct(self):
    sector = Sector(radius=2)
    sector2 = Sector(radius=2.5, angle=60*DEGREES).move_to([-3, 0, 0])
    sector.set_color(RED)
    sector2.set_color(PINK)
    self.add(sector, sector2)

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
Parameters:
    
  * **radius** (_float_)
  * **kwargs** (_Any_)


_original__init__(_radius =1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Sector._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **radius** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next TipableVMobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.TipableVMobject.html>) [ Previous LabeledDot ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.LabeledDot.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Sector](https://docs.manim.community/en/stable/reference/<#>)
    * `[Sector`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Sector>)
      * `[Sector._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Sector._original__init__>)


