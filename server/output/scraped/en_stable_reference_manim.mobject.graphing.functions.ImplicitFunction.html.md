# ImplicitFunction[¶](https://docs.manim.community/en/stable/reference/<#implicitfunction> "Link to this heading")
Qualified name: `manim.mobject.graphing.functions.ImplicitFunction`
_class_ ImplicitFunction(_func_ , _x_range =None_, _y_range =None_, _min_depth =5_, _max_quads =1500_, _use_smoothing =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/functions.html#ImplicitFunction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
An implicit function.
Parameters:
    
  * **func** (_Callable_ _[__[__float_ _,__float_ _]__,__float_ _]_) – The implicit function in the form `f(x, y) = 0`.
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The x min and max of the function.
  * **y_range** (_Sequence_ _[__float_ _]__|__None_) – The y min and max of the function.
  * **min_depth** (_int_) – The minimum depth of the function to calculate.
  * **max_quads** (_int_) – The maximum number of quads to use.
  * **use_smoothing** (_bool_) – Whether or not to smoothen the curves.
  * **kwargs** – Additional parameters to pass into `VMobject`


Note
A small `min_depth` d means that some small details might be ignored if they don’t cross an edge of one of the 4d uniform quads.
The value of `max_quads` strongly corresponds to the quality of the curve, but a higher number of quads may take longer to render.
Examples
Example: ImplicitFunctionExample [¶](https://docs.manim.community/en/stable/reference/<#implicitfunctionexample>)
![../_images/ImplicitFunctionExample-1.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-1.png)
```
frommanimimport *
classImplicitFunctionExample(Scene):
  defconstruct(self):
    graph = ImplicitFunction(
      lambda x, y: x * y ** 2 - x ** 2 * y - 2,
      color=YELLOW
    )
    self.add(NumberPlane(), graph)

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.generate_points> "manim.mobject.graphing.functions.ImplicitFunction.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`[init_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.init_points> "manim.mobject.graphing.functions.ImplicitFunction.init_points") | Initializes `points` and therefore the shape.  
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
_original__init__(_func_ , _x_range =None_, _y_range =None_, _min_depth =5_, _max_quads =1500_, _use_smoothing =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction._original__init__> "Link to this definition")
    
An implicit function.
Parameters:
    
  * **func** (_Callable_ _[__[__float_ _,__float_ _]__,__float_ _]_) – The implicit function in the form `f(x, y) = 0`.
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The x min and max of the function.
  * **y_range** (_Sequence_ _[__float_ _]__|__None_) – The y min and max of the function.
  * **min_depth** (_int_) – The minimum depth of the function to calculate.
  * **max_quads** (_int_) – The maximum number of quads to use.
  * **use_smoothing** (_bool_) – Whether or not to smoothen the curves.
  * **kwargs** – Additional parameters to pass into `VMobject`


Note
A small `min_depth` d means that some small details might be ignored if they don’t cross an edge of one of the 4d uniform quads.
The value of `max_quads` strongly corresponds to the quality of the curve, but a higher number of quads may take longer to render.
Examples
Example: ImplicitFunctionExample [¶](https://docs.manim.community/en/stable/reference/<#implicitfunctionexample>)
![../_images/ImplicitFunctionExample-2.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-2.png)
```
frommanimimport *
classImplicitFunctionExample(Scene):
  defconstruct(self):
    graph = ImplicitFunction(
      lambda x, y: x * y ** 2 - x ** 2 * y - 2,
      color=YELLOW
    )
    self.add(NumberPlane(), graph)

```
Copy to clipboard
Make interactive
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/functions.html#ImplicitFunction.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
init_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.init_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
[ Next ParametricFunction ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.ParametricFunction.html>) [ Previous FunctionGraph ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.FunctionGraph.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ImplicitFunction](https://docs.manim.community/en/stable/reference/<#>)
    * `[ImplicitFunction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction>)
      * `[ImplicitFunction._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction._original__init__>)
      * `[ImplicitFunction.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.generate_points>)
      * `[ImplicitFunction.init_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ImplicitFunction.init_points>)


