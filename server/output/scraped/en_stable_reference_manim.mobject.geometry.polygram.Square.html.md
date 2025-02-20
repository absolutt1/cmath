# Square[¶](https://docs.manim.community/en/stable/reference/<#square> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Square`
_class_ Square(_side_length =2.0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Square>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Square> "Link to this definition")
    
Bases: `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle")
A rectangle with equal side lengths.
Parameters:
    
  * **side_length** (_float_) – The length of the sides of the square.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle").


Examples
Example: SquareExample [¶](https://docs.manim.community/en/stable/reference/<#squareexample>)
![../_images/SquareExample-1.png](https://docs.manim.community/en/stable/_images/SquareExample-1.png)
```
frommanimimport *
classSquareExample(Scene):
  defconstruct(self):
    square_1 = Square(side_length=2.0).shift(DOWN)
    square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
    square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
    self.add(square_1, square_2, square_3)

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
`side_length`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_side_length =2.0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Square._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **side_length** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Star ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Star.html>) [ Previous RoundedRectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RoundedRectangle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Square](https://docs.manim.community/en/stable/reference/<#>)
    * `[Square`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Square>)
      * `[Square._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Square._original__init__>)


