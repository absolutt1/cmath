# LabeledPolygram[¶](https://docs.manim.community/en/stable/reference/<#labeledpolygram> "Link to this heading")
Qualified name: `manim.mobject.geometry.labeled.LabeledPolygram`
_class_ LabeledPolygram(_* vertex_groups_, _label_ , _precision =0.01_, _label_config =None_, _box_config =None_, _frame_config =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/labeled.html#LabeledPolygram>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledPolygram> "Link to this definition")
    
Bases: `[Polygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram")
Constructs a polygram containing a label box at its pole of inaccessibility.
Parameters:
    
  * **vertex_groups** ([_Point3DLike_Array_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")) – Vertices passed to the `[Polygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram") constructor.
  * **label** (_str_ _|_[_Tex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex") _|_[_MathTex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") _|_[_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text")) – Label that will be displayed on the Polygram.
  * **precision** (_float_) – The precision used by the PolyLabel algorithm.
  * **label_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – A dictionary containing the configuration for the label. This is only applied if `label` is of type `str`.
  * **box_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – A dictionary containing the configuration for the background box.
  * **frame_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – 
A dictionary containing the configuration for the frame.
Note
The PolyLabel Algorithm expects each vertex group to form a closed ring. If the input is open, `[LabeledPolygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledPolygram> "manim.mobject.geometry.labeled.LabeledPolygram") will attempt to close it. This may cause the polygon to intersect itself leading to unexpected results.
Tip
Make sure the precision corresponds to the scale of your inputs! For instance, if the bounding box of your polygon stretches from 0 to 10,000, a precision of 1.0 or 10.0 should be sufficient.
  * **kwargs** (_Any_)


Examples
Example: LabeledPolygramExample [¶](https://docs.manim.community/en/stable/reference/<#labeledpolygramexample>)
![../_images/LabeledPolygramExample-1.png](https://docs.manim.community/en/stable/_images/LabeledPolygramExample-1.png)
```
frommanimimport *
classLabeledPolygramExample(Scene):
  defconstruct(self):
    # Define Rings
    ring1 = [
      [-3.8, -2.4, 0], [-2.4, -2.5, 0], [-1.3, -1.6, 0], [-0.2, -1.7, 0],
      [1.7, -2.5, 0], [2.9, -2.6, 0], [3.5, -1.5, 0], [4.9, -1.4, 0],
      [4.5, 0.2, 0], [4.7, 1.6, 0], [3.5, 2.4, 0], [1.1, 2.5, 0],
      [-0.1, 0.9, 0], [-1.2, 0.5, 0], [-1.6, 0.7, 0], [-1.4, 1.9, 0],
      [-2.6, 2.6, 0], [-4.4, 1.2, 0], [-4.9, -0.8, 0], [-3.8, -2.4, 0]
    ]
    ring2 = [
      [0.2, -1.2, 0], [0.9, -1.2, 0], [1.4, -2.0, 0], [2.1, -1.6, 0],
      [2.2, -0.5, 0], [1.4, 0.0, 0], [0.4, -0.2, 0], [0.2, -1.2, 0]
    ]
    ring3 = [[-2.7, 1.4, 0], [-2.3, 1.7, 0], [-2.8, 1.9, 0], [-2.7, 1.4, 0]]
    # Create Polygons (for reference)
    p1 = Polygon(*ring1, fill_opacity=0.75)
    p2 = Polygon(*ring2, fill_color=BLACK, fill_opacity=1)
    p3 = Polygon(*ring3, fill_color=BLACK, fill_opacity=1)
    # Create Labeled Polygram
    polygram = LabeledPolygram(
      *[ring1, ring2, ring3],
      label=Text('Pole', font='sans-serif'),
      precision=0.01,
    )
    # Display Circle (for reference)
    circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)
    self.add(p1, p2, p3)
    self.add(polygram)
    self.add(circle)

```
Copy to clipboard
Make interactive
Example: LabeledCountryExample [¶](https://docs.manim.community/en/stable/reference/<#labeledcountryexample>)
![../_images/LabeledCountryExample-1.png](https://docs.manim.community/en/stable/_images/LabeledCountryExample-1.png)
```
frommanimimport *
importrequests
importjson
classLabeledCountryExample(Scene):
  defconstruct(self):
    # Fetch JSON data and process arcs
    data = requests.get('https://cdn.jsdelivr.net/npm/us-atlas@3/nation-10m.json').json()
    arcs, transform = data['arcs'], data['transform']
    sarcs = [np.cumsum(arc, axis=0) * transform['scale'] + transform['translate'] for arc in arcs]
    ssarcs = sorted(sarcs, key=len, reverse=True)[:1]
    # Compute Bounding Box
    points = np.concatenate(ssarcs)
    mins, maxs = np.min(points, axis=0), np.max(points, axis=0)
    # Build Axes
    ax = Axes(
      x_range=[mins[0], maxs[0], maxs[0] - mins[0]], x_length=10,
      y_range=[mins[1], maxs[1], maxs[1] - mins[1]], y_length=7,
      tips=False
    )
    # Adjust Coordinates
    array = [[ax.c2p(*point) for point in sarc] for sarc in ssarcs]
    # Add Polygram
    polygram = LabeledPolygram(
      *array,
      label=Text('USA', font='sans-serif'),
      precision=0.01,
      fill_color=BLUE,
      stroke_width=0,
      fill_opacity=0.75
    )
    # Display Circle (for reference)
    circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)
    self.add(ax)
    self.add(polygram)
    self.add(circle)

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
_original__init__(_* vertex_groups_, _label_ , _precision =0.01_, _label_config =None_, _box_config =None_, _frame_config =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledPolygram._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vertex_groups** ([_Point3DLike_Array_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array"))
  * **label** (_str_ _|_[_Tex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex") _|_[_MathTex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") _|_[_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))
  * **precision** (_float_)
  * **label_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **box_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **frame_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next line ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.html>) [ Previous LabeledLine ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.LabeledLine.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LabeledPolygram](https://docs.manim.community/en/stable/reference/<#>)
    * `[LabeledPolygram`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledPolygram>)
      * `[LabeledPolygram._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledPolygram._original__init__>)


