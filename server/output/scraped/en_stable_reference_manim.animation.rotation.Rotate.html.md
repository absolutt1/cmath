# Rotate[¶](https://docs.manim.community/en/stable/reference/<#rotate> "Link to this heading")
Qualified name: `manim.animation.rotation.Rotate`
_class_ Rotate(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/rotation.html#Rotate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotate> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Animation that rotates a Mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be rotated.
  * **angle** (_float_) – The rotation angle.
  * **axis** (_np.ndarray_) – The rotation axis as a numpy vector.
  * **about_point** (_Sequence_ _[__float_ _]__|__None_) – The rotation center.
  * **about_edge** (_Sequence_ _[__float_ _]__|__None_) – If `about_point` is `None`, this argument specifies the direction of the bounding box point to be taken as the rotation center.


Examples
Example: UsingRotate [¶](https://docs.manim.community/en/stable/reference/<#usingrotate>)
```
frommanimimport *
classUsingRotate(Scene):
  defconstruct(self):
    self.play(
      Rotate(
        Square(side_length=0.5).shift(UP * 2),
        angle=2*PI,
        about_point=ORIGIN,
        rate_func=linear,
      ),
      Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
      )

```
Copy to clipboard
Make interactive
Methods
`create_target`  
---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _angle =3.141592653589793_, _axis =array([0., 0., 1.])_, _about_point =None_, _about_edge =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotate._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **angle** (_float_)
  * **axis** (_np.ndarray_)
  * **about_point** (_Sequence_ _[__float_ _]__|__None_)
  * **about_edge** (_Sequence_ _[__float_ _]__|__None_)


Return type:
    
None
[ Next Rotating ](https://docs.manim.community/en/stable/reference/<manim.animation.rotation.Rotating.html>) [ Previous rotation ](https://docs.manim.community/en/stable/reference/<manim.animation.rotation.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Rotate](https://docs.manim.community/en/stable/reference/<#>)
    * `[Rotate`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotate>)
      * `[Rotate._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.rotation.Rotate._original__init__>)


