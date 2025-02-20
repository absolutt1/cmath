# Intersection[¶](https://docs.manim.community/en/stable/reference/<#intersection> "Link to this heading")
Qualified name: `manim.mobject.geometry.boolean\_ops.Intersection`
_class_ Intersection(_* vmobjects_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/boolean_ops.html#Intersection>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Intersection> "Link to this definition")
    
Bases: `_BooleanOps`
Find the intersection of two `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") s. This keeps the parts covered by both `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") s.
Parameters:
    
  * **vmobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") to find the intersection.
  * **kwargs** (_Any_)


Raises:
    
**ValueError** – If less the 2 `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") are passed.
Example
Example: IntersectionExample [¶](https://docs.manim.community/en/stable/reference/<#intersectionexample>)
![../_images/IntersectionExample-2.png](https://docs.manim.community/en/stable/_images/IntersectionExample-2.png)
```
frommanimimport *
classIntersectionExample(Scene):
  defconstruct(self):
    sq = Square(color=RED, fill_opacity=1)
    sq.move_to([-2, 0, 0])
    cr = Circle(color=BLUE, fill_opacity=1)
    cr.move_to([-1.3, 0.7, 0])
    un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
    un.move_to([1.5, 0, 0])
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
_original__init__(_* vmobjects_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Intersection._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Union ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Union.html>) [ Previous Exclusion ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Exclusion.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Intersection](https://docs.manim.community/en/stable/reference/<#>)
    * `[Intersection`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Intersection>)
      * `[Intersection._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Intersection._original__init__>)


