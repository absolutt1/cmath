# LayoutFunction[¶](https://docs.manim.community/en/stable/reference/<#layoutfunction> "Link to this heading")
Qualified name: `manim.mobject.graph.LayoutFunction`
_class_ LayoutFunction(_* args_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graph.html#LayoutFunction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.LayoutFunction> "Link to this definition")
    
Bases: `Protocol`
A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`.
Note
The layout function must be a pure function, i.e., it must not modify the graph passed to it.
Examples
Here is an example that arranges nodes in an n x m grid in sorted order.
Example: CustomLayoutExample [¶](https://docs.manim.community/en/stable/reference/<#customlayoutexample>)
![../_images/CustomLayoutExample-1.png](https://docs.manim.community/en/stable/_images/CustomLayoutExample-1.png)
```
frommanimimport *
classCustomLayoutExample(Scene):
  defconstruct(self):
    importnumpyasnp
    importnetworkxasnx
    # create custom layout
    defcustom_layout(
      graph: nx.Graph,
      scale: float | tuple[float, float, float] = 2,
      n: int | None = None,
      *args: Any,
      **kwargs: Any,
    ):
      nodes = sorted(list(graph))
      height = len(nodes) // n
      return {
        node: (scale * np.array([
          (i % n) - (n-1)/2,
          -(i // n) + height/2,
          0
        ])) for i, node in enumerate(graph)
      }
    # draw graph
    n = 4
    graph = Graph(
      [i for i in range(4 * 2 - 1)],
      [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (4, 5), (5, 6)],
      labels=True,
      layout=custom_layout,
      layout_config={'n': n}
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
Several automatic layouts are provided by manim, and can be used by passing their name as the `layout` parameter to `change_layout()`. Alternatively, a custom layout function can be passed to `change_layout()` as the `layout` parameter. Such a function must adhere to the `[LayoutFunction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.LayoutFunction> "manim.mobject.graph.LayoutFunction") protocol.
The `[LayoutFunction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.LayoutFunction> "manim.mobject.graph.LayoutFunction") s provided by manim are illustrated below:
  * Circular Layout: places the vertices on a circle


Example: CircularLayout [¶](https://docs.manim.community/en/stable/reference/<#circularlayout>)
![../_images/CircularLayout-1.png](https://docs.manim.community/en/stable/_images/CircularLayout-1.png)
```
frommanimimport *
classCircularLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="circular",
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Kamada Kawai Layout: tries to place the vertices such that the given distances between them are respected


Example: KamadaKawaiLayout [¶](https://docs.manim.community/en/stable/reference/<#kamadakawailayout>)
![../_images/KamadaKawaiLayout-1.png](https://docs.manim.community/en/stable/_images/KamadaKawaiLayout-1.png)
```
frommanimimport *
classKamadaKawaiLayout(Scene):
  defconstruct(self):
    fromcollectionsimport defaultdict
    distances: dict[int, dict[int, float]] = defaultdict(dict)
    # set desired distances
    distances[1][2] = 1 # distance between vertices 1 and 2 is 1
    distances[2][3] = 1 # distance between vertices 2 and 3 is 1
    distances[3][4] = 2 # etc
    distances[4][5] = 3
    distances[5][6] = 5
    distances[6][1] = 8
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
      layout="kamada_kawai",
      layout_config={"dist": distances},
      layout_scale=4,
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Partite Layout: places vertices into distinct partitions


Example: PartiteLayout [¶](https://docs.manim.community/en/stable/reference/<#partitelayout>)
![../_images/PartiteLayout-1.png](https://docs.manim.community/en/stable/_images/PartiteLayout-1.png)
```
frommanimimport *
classPartiteLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="partite",
      layout_config={"partitions": [[1,2],[3,4],[5,6]]},
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Planar Layout: places vertices such that edges do not cross


Example: PlanarLayout [¶](https://docs.manim.community/en/stable/reference/<#planarlayout>)
![../_images/PlanarLayout-1.png](https://docs.manim.community/en/stable/_images/PlanarLayout-1.png)
```
frommanimimport *
classPlanarLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="planar",
      layout_scale=4,
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Random Layout: randomly places vertices


Example: RandomLayout [¶](https://docs.manim.community/en/stable/reference/<#randomlayout>)
![../_images/RandomLayout-1.png](https://docs.manim.community/en/stable/_images/RandomLayout-1.png)
```
frommanimimport *
classRandomLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="random",
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Shell Layout: places vertices in concentric circles


Example: ShellLayout [¶](https://docs.manim.community/en/stable/reference/<#shelllayout>)
![../_images/ShellLayout-1.png](https://docs.manim.community/en/stable/_images/ShellLayout-1.png)
```
frommanimimport *
classShellLayout(Scene):
  defconstruct(self):
    nlist = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
    graph = Graph(
      [1, 2, 3, 4, 5, 6, 7, 8, 9],
      [(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3), (8, 3), (8, 1), (9, 1)],
      layout="shell",
      layout_config={"nlist": nlist},
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Spectral Layout: places vertices using the eigenvectors of the graph Laplacian (clusters nodes which are an approximation of the ratio cut)


Example: SpectralLayout [¶](https://docs.manim.community/en/stable/reference/<#spectrallayout>)
![../_images/SpectralLayout-1.png](https://docs.manim.community/en/stable/_images/SpectralLayout-1.png)
```
frommanimimport *
classSpectralLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="spectral",
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Sprial Layout: places vertices in a spiraling pattern


Example: SpiralLayout [¶](https://docs.manim.community/en/stable/reference/<#spirallayout>)
![../_images/SpiralLayout-1.png](https://docs.manim.community/en/stable/_images/SpiralLayout-1.png)
```
frommanimimport *
classSpiralLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="spiral",
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Spring Layout: places nodes according to the Fruchterman-Reingold force-directed algorithm (attempts to minimize edge length while maximizing node separation)


Example: SpringLayout [¶](https://docs.manim.community/en/stable/reference/<#springlayout>)
![../_images/SpringLayout-1.png](https://docs.manim.community/en/stable/_images/SpringLayout-1.png)
```
frommanimimport *
classSpringLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6],
      [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
      layout="spring",
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
  * Tree Layout: places vertices into a tree with a root node and branches (can only be used with legal trees)


Example: TreeLayout [¶](https://docs.manim.community/en/stable/reference/<#treelayout>)
![../_images/TreeLayout-1.png](https://docs.manim.community/en/stable/_images/TreeLayout-1.png)
```
frommanimimport *
classTreeLayout(Scene):
  defconstruct(self):
    graph = Graph(
      [1, 2, 3, 4, 5, 6, 7],
      [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)],
      layout="tree",
      layout_config={"root_vertex": 1},
      labels=True
    )
    self.add(graph)

```
Copy to clipboard
Make interactive
Methods
[ Next graphing ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.html>) [ Previous Graph ](https://docs.manim.community/en/stable/reference/<manim.mobject.graph.Graph.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LayoutFunction](https://docs.manim.community/en/stable/reference/<#>)
    * `[LayoutFunction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graph.LayoutFunction>)


