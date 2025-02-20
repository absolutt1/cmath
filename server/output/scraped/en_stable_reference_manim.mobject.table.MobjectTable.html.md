# MobjectTable[¶](https://docs.manim.community/en/stable/reference/<#mobjecttable> "Link to this heading")
Qualified name: `manim.mobject.table.MobjectTable`
_class_ MobjectTable(_table_ , _element_to_mobject= <function MobjectTable.<lambda>>_, _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/table.html#MobjectTable>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.MobjectTable> "Link to this definition")
    
Bases: `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table")
A specialized `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") mobject for use with `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
Examples
Example: MobjectTableExample [¶](https://docs.manim.community/en/stable/reference/<#mobjecttableexample>)
![../_images/MobjectTableExample-1.png](https://docs.manim.community/en/stable/_images/MobjectTableExample-1.png)
```
frommanimimport *
classMobjectTableExample(Scene):
  defconstruct(self):
    cross = VGroup(
      Line(UP + LEFT, DOWN + RIGHT),
      Line(UP + RIGHT, DOWN + LEFT),
    )
    a = Circle().set_color(RED).scale(0.5)
    b = cross.set_color(BLUE).scale(0.5)
    t0 = MobjectTable(
      [[a.copy(),b.copy(),a.copy()],
      [b.copy(),a.copy(),a.copy()],
      [a.copy(),b.copy(),b.copy()]]
    )
    line = Line(
      t0.get_corner(DL), t0.get_corner(UR)
    ).set_color(RED)
    self.add(t0, line)

```
Copy to clipboard
Make interactive
Special case of `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") with `element_to_mobject` set to an identity function. Here, every item in `table` must already be of type `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
Parameters:
    
  * **table** (_Iterable_ _[__Iterable_ _[_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]__]_) – A 2D array or list of lists. Content of the table must be of type `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **element_to_mobject** (_Callable_ _[__[_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]__,_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]_) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `lambda m : m` to return itself.
  * **kwargs** – Additional arguments to be passed to `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table").


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
_original__init__(_table_ , _element_to_mobject= <function MobjectTable.<lambda>>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.MobjectTable._original__init__> "Link to this definition")
    
Special case of `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") with `element_to_mobject` set to an identity function. Here, every item in `table` must already be of type `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
Parameters:
    
  * **table** (_Iterable_ _[__Iterable_ _[_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]__]_) – A 2D array or list of lists. Content of the table must be of type `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **element_to_mobject** (_Callable_ _[__[_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]__,_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]_) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `lambda m : m` to return itself.
  * **kwargs** – Additional arguments to be passed to `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table").


[ Next Table ](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html>) [ Previous MathTable ](https://docs.manim.community/en/stable/reference/<manim.mobject.table.MathTable.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MobjectTable](https://docs.manim.community/en/stable/reference/<#>)
    * `[MobjectTable`](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.MobjectTable>)
      * `[MobjectTable._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.MobjectTable._original__init__>)


