# DashedLine[¶](https://docs.manim.community/en/stable/reference/<#dashedline> "Link to this heading")
Qualified name: `manim.mobject.geometry.line.DashedLine`
_class_ DashedLine(_* args_, _dash_length =0.05_, _dashed_ratio =0.5_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine> "Link to this definition")
    
Bases: `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
A dashed `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line").
Parameters:
    
  * **args** (_Any_) – Arguments to be passed to `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
  * **dash_length** (_float_) – The length of each individual dash of the line.
  * **dashed_ratio** (_float_) – The ratio of dash space to empty space. Range of 0-1.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")


See also
`[DashedVMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject> "manim.mobject.types.vectorized_mobject.DashedVMobject")
Examples
Example: DashedLineExample [¶](https://docs.manim.community/en/stable/reference/<#dashedlineexample>)
![../_images/DashedLineExample-1.png](https://docs.manim.community/en/stable/_images/DashedLineExample-1.png)
```
frommanimimport *
classDashedLineExample(Scene):
  defconstruct(self):
    # dash_length increased
    dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
    # normal
    dashed_2 = DashedLine(config.left_side, config.right_side)
    # dashed_ratio decreased
    dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
    self.add(dashed_1, dashed_2, dashed_3)

```
Copy to clipboard
Make interactive
Methods
`[get_end`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_end> "manim.mobject.geometry.line.DashedLine.get_end") | Returns the end point of the line.  
---|---  
`[get_first_handle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_first_handle> "manim.mobject.geometry.line.DashedLine.get_first_handle") | Returns the point of the first handle.  
`[get_last_handle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_last_handle> "manim.mobject.geometry.line.DashedLine.get_last_handle") | Returns the point of the last handle.  
`[get_start`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_start> "manim.mobject.geometry.line.DashedLine.get_start") | Returns the start point of the line.  
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
_calculate_num_dashes()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine._calculate_num_dashes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine._calculate_num_dashes> "Link to this definition")
    
Returns the number of dashes in the dashed line.
Examples
```
>>> DashedLine()._calculate_num_dashes()
20

```
Copy to clipboard
Return type:
    
int
_original__init__(_* args_, _dash_length =0.05_, _dashed_ratio =0.5_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **args** (_Any_)
  * **dash_length** (_float_)
  * **dashed_ratio** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
get_end()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine.get_end>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_end> "Link to this definition")
    
Returns the end point of the line.
Examples
```
>>> DashedLine().get_end()
array([1., 0., 0.])

```
Copy to clipboard
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
get_first_handle()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine.get_first_handle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_first_handle> "Link to this definition")
    
Returns the point of the first handle.
Examples
```
>>> DashedLine().get_first_handle()
array([-0.98333333, 0.    , 0.    ])

```
Copy to clipboard
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
get_last_handle()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine.get_last_handle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_last_handle> "Link to this definition")
    
Returns the point of the last handle.
Examples
```
>>> DashedLine().get_last_handle()
array([0.98333333, 0.    , 0.    ])

```
Copy to clipboard
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
get_start()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#DashedLine.get_start>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_start> "Link to this definition")
    
Returns the start point of the line.
Examples
```
>>> DashedLine().get_start()
array([-1., 0., 0.])

```
Copy to clipboard
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
[ Next DoubleArrow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.DoubleArrow.html>) [ Previous Arrow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DashedLine](https://docs.manim.community/en/stable/reference/<#>)
    * `[DashedLine`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine>)
      * `[DashedLine._calculate_num_dashes()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine._calculate_num_dashes>)
      * `[DashedLine._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine._original__init__>)
      * `[DashedLine.get_end()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_end>)
      * `[DashedLine.get_first_handle()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_first_handle>)
      * `[DashedLine.get_last_handle()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_last_handle>)
      * `[DashedLine.get_start()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.DashedLine.get_start>)


