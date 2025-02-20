# Exclusion[¶](https://docs.manim.community/en/stable/reference/<#exclusion> "Link to this heading")
Qualified name: `manim.mobject.geometry.boolean\_ops.Exclusion`
_class_ Exclusion(_subject_ , _clip_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/boolean_ops.html#Exclusion>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Exclusion> "Link to this definition")
    
Bases: `_BooleanOps`
Find the XOR between two `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"). This creates a new `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") consisting of the region covered by exactly one of them.
Parameters:
    
  * **subject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The 1st `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").
  * **clip** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The 2nd `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
  * **kwargs** (_Any_)


Example
Example: IntersectionExample [¶](https://docs.manim.community/en/stable/reference/<#intersectionexample>)
![../_images/IntersectionExample-1.png](https://docs.manim.community/en/stable/_images/IntersectionExample-1.png)
```
frommanimimport *
classIntersectionExample(Scene):
  defconstruct(self):
    sq = Square(color=RED, fill_opacity=1)
    sq.move_to([-2, 0, 0])
    cr = Circle(color=BLUE, fill_opacity=1)
    cr.move_to([-1.3, 0.7, 0])
    un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
    un.move_to([1.5, 0.4, 0])
    self.add(sq, cr, un)

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
_original__init__(_subject_ , _clip_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Exclusion._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **subject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **clip** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Intersection ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Intersection.html>) [ Previous Difference ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Difference.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Exclusion](https://docs.manim.community/en/stable/reference/<#>)
    * `[Exclusion`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Exclusion>)
      * `[Exclusion._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Exclusion._original__init__>)


