# ParametricFunction[¶](https://docs.manim.community/en/stable/reference/<#parametricfunction> "Link to this heading")
Qualified name: `manim.mobject.graphing.functions.ParametricFunction`
_class_ ParametricFunction(_function_ , _t_range=(0_ , _1)_ , _scaling= <manim.mobject.graphing.scale.LinearBase object>_, _dt=1e-08_ , _discontinuities=None_ , _use_smoothing=True_ , _use_vectorized=False_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/functions.html#ParametricFunction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A parametric curve.
Parameters:
    
  * **function** (_Callable_ _[__[__float_ _]__,_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _]_) – The function to be plotted in the form of `(lambda t: (x(t), y(t), z(t)))`
  * **t_range** (_tuple_ _[__float_ _,__float_ _]__|__tuple_ _[__float_ _,__float_ _,__float_ _]_) – Determines the length that the function spans in the form of (t_min, t_max, step=0.01). By default `[0, 1]`
  * **scaling** (__ScaleBase_) – Scaling class applied to the points of the function. Default of `[LinearBase`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase> "manim.mobject.graphing.scale.LinearBase").
  * **use_smoothing** (_bool_) – Whether to interpolate between the points of the function after they have been created. (Will have odd behaviour with a low number of points)
  * **use_vectorized** (_bool_) – Whether to pass in the generated t value array to the function as `[t_0, t_1, ...]`. Only use this if your function supports it. Output should be a numpy array of shape `[[x_0, x_1, ...], [y_0, y_1, ...], [z_0, z_1, ...]]` but `z` can also be 0 if the Axes is 2D
  * **discontinuities** (_Iterable_ _[__float_ _]__|__None_) – Values of t at which the function experiences discontinuity.
  * **dt** (_float_) – The left and right tolerance for the discontinuities.


Examples
Example: PlotParametricFunction [¶](https://docs.manim.community/en/stable/reference/<#plotparametricfunction>)
![../_images/PlotParametricFunction-1.png](https://docs.manim.community/en/stable/_images/PlotParametricFunction-1.png)
```
frommanimimport *
classPlotParametricFunction(Scene):
  deffunc(self, t):
    return (np.sin(2 * t), np.sin(3 * t), 0)
  defconstruct(self):
    func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
    self.add(func.scale(3))

```
Copy to clipboard
Make interactive
Example: ThreeDParametricSpring [¶](https://docs.manim.community/en/stable/reference/<#threedparametricspring>)
![../_images/ThreeDParametricSpring-1.png](https://docs.manim.community/en/stable/_images/ThreeDParametricSpring-1.png)
```
frommanimimport *
classThreeDParametricSpring(ThreeDScene):
  defconstruct(self):
    curve1 = ParametricFunction(
      lambda u: (
        1.2 * np.cos(u),
        1.2 * np.sin(u),
        u * 0.05
      ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
    ).set_shade_in_3d(True)
    axes = ThreeDAxes()
    self.add(axes, curve1)
    self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
    self.wait()

```
Copy to clipboard
Make interactive
Attention
If your function has discontinuities, you’ll have to specify the location of the discontinuities manually. See the following example for guidance.
Example: DiscontinuousExample [¶](https://docs.manim.community/en/stable/reference/<#discontinuousexample>)
![../_images/DiscontinuousExample-1.png](https://docs.manim.community/en/stable/_images/DiscontinuousExample-1.png)
```
frommanimimport *
classDiscontinuousExample(Scene):
  defconstruct(self):
    ax1 = NumberPlane((-3, 3), (-4, 4))
    ax2 = NumberPlane((-3, 3), (-4, 4))
    VGroup(ax1, ax2).arrange()
    discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
    incorrect = ax1.plot(discontinuous_function, color=RED)
    correct = ax2.plot(
      discontinuous_function,
      discontinuities=[-2, 2], # discontinuous points
      dt=0.1, # left and right tolerance of discontinuity
      color=GREEN,
    )
    self.add(ax1, ax2, incorrect, correct)

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.generate_points> "manim.mobject.graphing.functions.ParametricFunction.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`get_function`  
`get_point_from_function`  
`[init_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.init_points> "manim.mobject.graphing.functions.ParametricFunction.init_points") | Initializes `points` and therefore the shape.  
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
_original__init__(_function_ , _t_range=(0_ , _1)_ , _scaling= <manim.mobject.graphing.scale.LinearBase object>_, _dt=1e-08_ , _discontinuities=None_ , _use_smoothing=True_ , _use_vectorized=False_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **function** (_Callable_ _[__[__float_ _]__,_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _]_)
  * **t_range** (_tuple_ _[__float_ _,__float_ _]__|__tuple_ _[__float_ _,__float_ _,__float_ _]_)
  * **scaling** (__ScaleBase_)
  * **dt** (_float_)
  * **discontinuities** (_Iterable_ _[__float_ _]__|__None_)
  * **use_smoothing** (_bool_)
  * **use_vectorized** (_bool_)


generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/functions.html#ParametricFunction.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
Self
init_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.init_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
Self
[ Next number_line ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.html>) [ Previous ImplicitFunction ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.ImplicitFunction.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ParametricFunction](https://docs.manim.community/en/stable/reference/<#>)
    * `[ParametricFunction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction>)
      * `[ParametricFunction._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction._original__init__>)
      * `[ParametricFunction.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.generate_points>)
      * `[ParametricFunction.init_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.functions.ParametricFunction.init_points>)


