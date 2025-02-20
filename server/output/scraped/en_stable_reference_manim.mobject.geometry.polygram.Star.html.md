# Star[¶](https://docs.manim.community/en/stable/reference/<#star> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Star`
_class_ Star(_n =5_, _*_ , _outer_radius =1_, _inner_radius =None_, _density =2_, _start_angle =1.5707963267948966_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Star>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star> "Link to this definition")
    
Bases: `[Polygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon")
A regular polygram without the intersecting lines.
Parameters:
    
  * **n** (_int_) – How many points on the `[Star`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star> "manim.mobject.geometry.polygram.Star").
  * **outer_radius** (_float_) – The radius of the circle that the outer vertices are placed on.
  * **inner_radius** (_float_ _|__None_) – 
The radius of the circle that the inner vertices are placed on.
If unspecified, the inner radius will be calculated such that the edges of the `[Star`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star> "manim.mobject.geometry.polygram.Star") perfectly follow the edges of its `[RegularPolygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram> "manim.mobject.geometry.polygram.RegularPolygram") counterpart.
  * **density** (_int_) – 
The density of the `[Star`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star> "manim.mobject.geometry.polygram.Star"). Only used if `inner_radius` is unspecified.
See `[RegularPolygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram> "manim.mobject.geometry.polygram.RegularPolygram") for more information.
  * **start_angle** (_float_ _|__None_) – The angle the vertices start at; the rotation of the `[Star`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star> "manim.mobject.geometry.polygram.Star").
  * **kwargs** (_Any_) – Forwardeds to the parent constructor.


Raises:
    
**ValueError** – If `inner_radius` is unspecified and `density` is not in the range `[1, n/2)`.
Examples
Example: StarExample [¶](https://docs.manim.community/en/stable/reference/<#starexample>)
```
frommanimimport *
classStarExample(Scene):
  defconstruct(self):
    pentagram = RegularPolygram(5, radius=2)
    star = Star(outer_radius=2, color=RED)
    self.add(pentagram)
    self.play(Create(star), run_time=3)
    self.play(FadeOut(star), run_time=2)

```
Copy to clipboard
Make interactive
Example: DifferentDensitiesExample [¶](https://docs.manim.community/en/stable/reference/<#differentdensitiesexample>)
![../_images/DifferentDensitiesExample-1.png](https://docs.manim.community/en/stable/_images/DifferentDensitiesExample-1.png)
```
frommanimimport *
classDifferentDensitiesExample(Scene):
  defconstruct(self):
    density_2 = Star(7, outer_radius=2, density=2, color=RED)
    density_3 = Star(7, outer_radius=2, density=3, color=PURPLE)
    self.add(VGroup(density_2, density_3).arrange(RIGHT))

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
_original__init__(_n =5_, _*_ , _outer_radius =1_, _inner_radius =None_, _density =2_, _start_angle =1.5707963267948966_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **n** (_int_)
  * **outer_radius** (_float_)
  * **inner_radius** (_float_ _|__None_)
  * **density** (_int_)
  * **start_angle** (_float_ _|__None_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Triangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Triangle.html>) [ Previous Square ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Square.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Star](https://docs.manim.community/en/stable/reference/<#>)
    * `[Star`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star>)
      * `[Star._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Star._original__init__>)


