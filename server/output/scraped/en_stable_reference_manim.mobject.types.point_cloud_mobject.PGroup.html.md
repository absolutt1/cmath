# PGroup[¶](https://docs.manim.community/en/stable/reference/<#pgroup> "Link to this heading")
Qualified name: `manim.mobject.types.point\_cloud\_mobject.PGroup`
_class_ PGroup(_* pmobs_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/point_cloud_mobject.html#PGroup>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PGroup> "Link to this definition")
    
Bases: `[PMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject> "manim.mobject.types.point_cloud_mobject.PMobject")
A group for several point mobjects.
Examples
Example: PgroupExample [¶](https://docs.manim.community/en/stable/reference/<#pgroupexample>)
![../_images/PgroupExample-1.png](https://docs.manim.community/en/stable/_images/PgroupExample-1.png)
```
frommanimimport *
classPgroupExample(Scene):
  defconstruct(self):
    p1 = PointCloudDot(radius=1, density=20, color=BLUE)
    p1.move_to(4.5 * LEFT)
    p2 = PointCloudDot()
    p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
    p3.move_to(4.5 * RIGHT)
    pList = PGroup(p1, p2, p3)
    self.add(pList)

```
Copy to clipboard
Make interactive
Methods
`fade_to`  
---  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`depth` | The depth of the mobject.  
`height` | The height of the mobject.  
`width` | The width of the mobject.  
Parameters:
    
  * **pmobs** (_Any_)
  * **kwargs** (_Any_)


_original__init__(_* pmobs_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PGroup._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **pmobs** (_Any_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next PMobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.point_cloud_mobject.PMobject.html>) [ Previous Mobject2D ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.point_cloud_mobject.Mobject2D.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [PGroup](https://docs.manim.community/en/stable/reference/<#>)
    * `[PGroup`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PGroup>)
      * `[PGroup._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PGroup._original__init__>)


