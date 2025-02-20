# Dodecahedron[¶](https://docs.manim.community/en/stable/reference/<#dodecahedron> "Link to this heading")
Qualified name: `manim.mobject.three\_d.polyhedra.Dodecahedron`
_class_ Dodecahedron(_edge_length =1_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/polyhedra.html#Dodecahedron>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Dodecahedron> "Link to this definition")
    
Bases: `[Polyhedron`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron> "manim.mobject.three_d.polyhedra.Polyhedron")
A dodecahedron, one of the five platonic solids. It has 12 faces, 30 edges and 20 vertices.
Parameters:
    
**edge_length** (_float_) – The length of an edge between any two vertices.
Examples
Example: DodecahedronScene [¶](https://docs.manim.community/en/stable/reference/<#dodecahedronscene>)
![../_images/DodecahedronScene-1.png](https://docs.manim.community/en/stable/_images/DodecahedronScene-1.png)
```
frommanimimport *
classDodecahedronScene(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
    obj = Dodecahedron()
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
_original__init__(_edge_length =1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Dodecahedron._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**edge_length** (_float_)
[ Next Icosahedron ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.polyhedra.Icosahedron.html>) [ Previous ConvexHull3D ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.polyhedra.ConvexHull3D.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Dodecahedron](https://docs.manim.community/en/stable/reference/<#>)
    * `[Dodecahedron`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Dodecahedron>)
      * `[Dodecahedron._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.polyhedra.Dodecahedron._original__init__>)


