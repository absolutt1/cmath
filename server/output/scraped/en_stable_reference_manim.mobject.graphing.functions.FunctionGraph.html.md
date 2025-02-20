# FunctionGraph[¶](https://docs.manim.community/en/stable/reference/<#functiongraph> "Link to this heading")
Qualified name: `manim.mobject.graphing.functions.FunctionGraph`
_class_ FunctionGraph(_function_ , _x_range =None_, _color =ManimColor('#FFFF00')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/functions.html#FunctionGraph>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.FunctionGraph> "Link to this definition")
    
Bases: `[ParametricFunction`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction> "manim.mobject.graphing.functions.ParametricFunction")
A `[ParametricFunction`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction> "manim.mobject.graphing.functions.ParametricFunction") that spans the length of the scene by default.
Examples
Example: ExampleFunctionGraph [¶](https://docs.manim.community/en/stable/reference/<#examplefunctiongraph>)
![../_images/ExampleFunctionGraph-1.png](https://docs.manim.community/en/stable/_images/ExampleFunctionGraph-1.png)
```
frommanimimport *
classExampleFunctionGraph(Scene):
  defconstruct(self):
    cos_func = FunctionGraph(
      lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
      color=RED,
    )
    sin_func_1 = FunctionGraph(
      lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
      color=BLUE,
    )
    sin_func_2 = FunctionGraph(
      lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
      x_range=[-4, 4],
      color=GREEN,
    ).move_to([0, 1, 0])
    self.add(cos_func, sin_func_1, sin_func_2)

```
Copy to clipboard
Make interactive
Methods
`get_function`  
---  
`get_point_from_function`  
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
_original__init__(_function_ , _x_range =None_, _color =ManimColor('#FFFF00')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.FunctionGraph._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next ImplicitFunction ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.ImplicitFunction.html>) [ Previous functions ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [FunctionGraph](https://docs.manim.community/en/stable/reference/<#>)
    * `[FunctionGraph`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.FunctionGraph>)
      * `[FunctionGraph._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.FunctionGraph._original__init__>)


