# Union[¶](https://docs.manim.community/en/stable/reference/<#union> "Link to this heading")
Qualified name: `manim.mobject.geometry.boolean\_ops.Union`
_class_ Union(_* vmobjects_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/boolean_ops.html#Union>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Union> "Link to this definition")
    
Bases: `_BooleanOps`
Union of two or more `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") s. This returns the common region of the `VMobject` s.
Parameters:
    
  * **vmobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") s to find the union of.
  * **kwargs** (_Any_)


Raises:
    
**ValueError** – If less than 2 `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") s are passed.
Example
Example: UnionExample [¶](https://docs.manim.community/en/stable/reference/<#unionexample>)
![../_images/UnionExample-1.png](https://docs.manim.community/en/stable/_images/UnionExample-1.png)
```
frommanimimport *
classUnionExample(Scene):
  defconstruct(self):
    sq = Square(color=RED, fill_opacity=1)
    sq.move_to([-2, 0, 0])
    cr = Circle(color=BLUE, fill_opacity=1)
    cr.move_to([-1.3, 0.7, 0])
    un = Union(sq, cr, color=GREEN, fill_opacity=1)
    un.move_to([1.5, 0.3, 0])
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
_original__init__(_* vmobjects_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Union._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next labeled ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.html>) [ Previous Intersection ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Intersection.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Union](https://docs.manim.community/en/stable/reference/<#>)
    * `[Union`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Union>)
      * `[Union._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.boolean_ops.Union._original__init__>)


