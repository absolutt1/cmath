# DiGraph[¶](https://docs.manim.community/en/stable/reference/<#digraph> "Link to this heading")
Qualified name: `manim.mobject.graph.DiGraph`
_class_ DiGraph(_vertices_ , _edges_ , _labels=False_ , _label_fill_color=ManimColor('#000000')_ , _layout='spring'_ , _layout_scale=2_ , _layout_config=None_ , _vertex_type= <class 'manim.mobject.geometry.arc.Dot'>_, _vertex_config=None_ , _vertex_mobjects=None_ , _edge_type= <class 'manim.mobject.geometry.line.Line'>_, _partitions=None_ , _root_vertex=None_ , _edge_config=None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graph.html#DiGraph>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph> "Link to this definition")
    
Bases: `[GenericGraph`](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph> "manim.mobject.graph.GenericGraph")
A directed graph.
Note
In contrast to undirected graphs, the order in which vertices in a given edge are specified is relevant here.
See also
`[GenericGraph`](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph> "manim.mobject.graph.GenericGraph")
Parameters:
    
  * **vertices** (_Sequence_ _[__Hashable_ _]_) – A list of vertices. Must be hashable elements.
  * **edges** (_Sequence_ _[__tuple_ _[__Hashable_ _,__Hashable_ _]__]_) – A list of edges, specified as tuples `(u, v)` where both `u` and `v` are vertices. The edge is directed from `u` to `v`.
  * **labels** (_bool_ _|__dict_) – Controls whether or not vertices are labeled. If `False` (the default), the vertices are not labeled; if `True` they are labeled using their names (as specified in `vertices`) via `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex"). Alternatively, custom labels can be specified by passing a dictionary whose keys are the vertices, and whose values are the corresponding vertex labels (rendered via, e.g., `[Text`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") or `[Tex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex")).
  * **label_fill_color** (_str_) – Sets the fill color of the default labels generated when `labels` is set to `True`. Has no effect for other values of `labels`.
  * **layout** (_LayoutName_ _|__dict_ _[__Hashable_ _,_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _]__|_[_LayoutFunction_](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction> "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`, `"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"` for automatic vertex positioning using `networkx` (see [their documentation](https://docs.manim.community/en/stable/reference/<https:/networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout>) for more details), or a dictionary specifying a coordinate (value) for each vertex (key) for manual positioning.
  * **layout_config** (_dict_ _|__None_) – Only for automatically generated layouts. A dictionary whose entries are passed as keyword arguments to the automatic layout algorithm specified via `layout` of `networkx`. The `tree` layout also accepts a special parameter `vertex_spacing` passed as a keyword argument inside the `layout_config` dictionary. Passing a tuple `(space_x, space_y)` as this argument overrides the value of `layout_scale` and ensures that vertices are arranged in a way such that the centers of siblings in the same layer are at least `space_x` units apart horizontally, and neighboring layers are spaced `space_y` units vertically.
  * **layout_scale** (_float_ _|__tuple_ _[__float_ _,__float_ _,__float_ _]_) – The scale of automatically generated layouts: the vertices will be arranged such that the coordinates are located within the interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)` causing the first coordinate to be in the interval `[-scale_x, scale_x]`, and the second in `[-scale_y, scale_y]`. Default: 2.
  * **vertex_type** (_type_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – The mobject class used for displaying vertices in the scene.
  * **vertex_config** (_dict_ _|__None_) – Either a dictionary containing keyword arguments to be passed to the class specified via `vertex_type`, or a dictionary whose keys are the vertices, and whose values are dictionaries containing keyword arguments for the mobject related to the corresponding vertex.
  * **vertex_mobjects** (_dict_ _|__None_) – A dictionary whose keys are the vertices, and whose values are mobjects to be used as vertices. Passing vertices here overrides all other configuration options for a vertex.
  * **edge_type** (_type_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – The mobject class used for displaying edges in the scene.
  * **edge_config** (_dict_ _|__None_) – Either a dictionary containing keyword arguments to be passed to the class specified via `edge_type`, or a dictionary whose keys are the edges, and whose values are dictionaries containing keyword arguments for the mobject related to the corresponding edge. You can further customize the tip by adding a `tip_config` dictionary for global styling, or by adding the dict to a specific `edge_config`.
  * **partitions** (_Sequence_ _[__Sequence_ _[__Hashable_ _]__]__|__None_)
  * **root_vertex** (_Hashable_ _|__None_)


Examples
Example: MovingDiGraph [¶](https://docs.manim.community/en/stable/reference/<#movingdigraph>)
```
frommanimimport *
classMovingDiGraph(Scene):
  defconstruct(self):
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
    g = DiGraph(vertices, edges)
    self.add(g)
    self.play(
      g[1].animate.move_to([1, 1, 1]),
      g[2].animate.move_to([-1, 1, 2]),
      g[3].animate.move_to([1, -1, -1]),
      g[4].animate.move_to([-1, -1, 0]),
    )
    self.wait()

```
Copy to clipboard
Make interactive
You can customize the edges and arrow tips globally or locally.
Example: CustomDiGraph [¶](https://docs.manim.community/en/stable/reference/<#customdigraph>)
```
frommanimimport *
classCustomDiGraph(Scene):
  defconstruct(self):
    vertices = [i for i in range(5)]
    edges = [
      (0, 1),
      (1, 2),
      (3, 2),
      (3, 4),
    ]
    edge_config = {
      "stroke_width": 2,
      "tip_config": {
        "tip_shape": ArrowSquareTip,
        "tip_length": 0.15,
      },
      (3, 4): {
        "color": RED,
        "tip_config": {"tip_length": 0.25, "tip_width": 0.25}
      },
    }
    g = DiGraph(
      vertices,
      edges,
      labels=True,
      layout="circular",
      edge_config=edge_config,
    ).scale(1.4)
    self.play(Create(g))
    self.wait()

```
Copy to clipboard
Make interactive
Since this implementation respects the labels boundary you can also use it for an undirected moving graph with labels.
Example: UndirectedMovingDiGraph [¶](https://docs.manim.community/en/stable/reference/<#undirectedmovingdigraph>)
```
frommanimimport *
classUndirectedMovingDiGraph(Scene):
  defconstruct(self):
    vertices = [i for i in range(5)]
    edges = [
      (0, 1),
      (1, 2),
      (3, 2),
      (3, 4),
    ]
    edge_config = {
      "stroke_width": 2,
      "tip_config": {"tip_length": 0, "tip_width": 0},
      (3, 4): {"color": RED},
    }
    g = DiGraph(
      vertices,
      edges,
      labels=True,
      layout="circular",
      edge_config=edge_config,
    ).scale(1.4)
    self.play(Create(g))
    self.wait()
    self.play(
      g[1].animate.move_to([1, 1, 1]),
      g[2].animate.move_to([-1, 1, 2]),
      g[3].animate.move_to([-1.5, -1.5, -1]),
      g[4].animate.move_to([1, -2, -1]),
    )
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`[update_edges`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph.update_edges> "manim.mobject.graph.DiGraph.update_edges") | Updates the edges to stick at their corresponding vertices.  
---|---  
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
_static_ _empty_networkx_graph()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graph.html#DiGraph._empty_networkx_graph>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._empty_networkx_graph> "Link to this definition")
    
Return an empty networkx graph for the given graph type.
Return type:
    
_DiGraph_
_original__init__(_vertices_ , _edges_ , _labels=False_ , _label_fill_color=ManimColor('#000000')_ , _layout='spring'_ , _layout_scale=2_ , _layout_config=None_ , _vertex_type= <class 'manim.mobject.geometry.arc.Dot'>_, _vertex_config=None_ , _vertex_mobjects=None_ , _edge_type= <class 'manim.mobject.geometry.line.Line'>_, _partitions=None_ , _root_vertex=None_ , _edge_config=None_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vertices** (_Sequence_ _[__Hashable_ _]_)
  * **edges** (_Sequence_ _[__tuple_ _[__Hashable_ _,__Hashable_ _]__]_)
  * **labels** (_bool_ _|__dict_)
  * **label_fill_color** (_str_)
  * **layout** (_Literal_ _[__'circular'__,__'kamada_kawai'__,__'partite'__,__'planar'__,__'random'__,__'shell'__,__'spectral'__,__'spiral'__,__'spring'__,__'tree'__]__|__dict_ _[__~collections.abc.Hashable_ _,__~manim.typing.Point3DLike_ _]__|__~manim.mobject.graph.LayoutFunction_)
  * **layout_scale** (_float_ _|__tuple_ _[__float_ _,__float_ _,__float_ _]_)
  * **layout_config** (_dict_ _|__None_)
  * **vertex_type** (_type_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_)
  * **vertex_config** (_dict_ _|__None_)
  * **vertex_mobjects** (_dict_ _|__None_)
  * **edge_type** (_type_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_)
  * **partitions** (_Sequence_ _[__Sequence_ _[__Hashable_ _]__]__|__None_)
  * **root_vertex** (_Hashable_ _|__None_)
  * **edge_config** (_dict_ _|__None_)


Return type:
    
None
_populate_edge_dict(_edges_ , _edge_type_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graph.html#DiGraph._populate_edge_dict>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._populate_edge_dict> "Link to this definition")
    
Helper method for populating the edges of the graph.
Parameters:
    
  * **edges** (_list_ _[__tuple_ _[__Hashable_ _,__Hashable_ _]__]_)
  * **edge_type** (_type_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_)


update_edges(_graph_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graph.html#DiGraph.update_edges>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph.update_edges> "Link to this definition")
    
Updates the edges to stick at their corresponding vertices.
Arrow tips need to be repositioned since otherwise they can be deformed.
[ Next GenericGraph ](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.GenericGraph.html>) [ Previous graph ](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DiGraph](https://docs.manim.community/en/stable/reference/<#>)
    * `[DiGraph`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph>)
      * `[DiGraph._empty_networkx_graph()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._empty_networkx_graph>)
      * `[DiGraph._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._original__init__>)
      * `[DiGraph._populate_edge_dict()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph._populate_edge_dict>)
      * `[DiGraph.update_edges()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.DiGraph.update_edges>)


