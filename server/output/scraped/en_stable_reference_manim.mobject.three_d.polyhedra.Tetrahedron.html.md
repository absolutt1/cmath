# Tetrahedron[¶](https://docs.manim.community/en/stable/reference/<#tetrahedron> "Link to this heading")
Qualified name: `manim.mobject.three\_d.polyhedra.Tetrahedron`
_class_ Tetrahedron(_edge_length =1_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/polyhedra.html#Tetrahedron>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Tetrahedron> "Link to this definition")
    
Bases: `[Polyhedron`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron> "manim.mobject.three_d.polyhedra.Polyhedron")
A tetrahedron, one of the five platonic solids. It has 4 faces, 6 edges, and 4 vertices.
Parameters:
    
**edge_length** (_float_) – The length of an edge between any two vertices.
Examples
Example: TetrahedronScene [¶](https://docs.manim.community/en/stable/reference/<#tetrahedronscene>)
![../_images/TetrahedronScene-1.png](https://docs.manim.community/en/stable/_images/TetrahedronScene-1.png)
```
frommanimimport *
classTetrahedronScene(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
    obj = Tetrahedron()
    self.add(obj)

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
_original__init__(_edge_length =1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Tetrahedron._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**edge_length** (_float_)
[ Next three_d_utils ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_d_utils.html>) [ Previous Polyhedron ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.polyhedra.Polyhedron.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Tetrahedron](https://docs.manim.community/en/stable/reference/<#>)
    * `[Tetrahedron`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Tetrahedron>)
      * `[Tetrahedron._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Tetrahedron._original__init__>)


