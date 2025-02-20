
# HSV[¶](https://docs.manim.community/en/stable/reference/<#hsv> "Link to this heading")
Qualified name: `manim.utils.color.core.HSV`
_class_ HSV(_hsv_ , _alpha =1.0_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/color/core.html#HSV>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV> "Link to this definition")
    
Bases: `[ManimColor`](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor")
HSV Color Space
Methods
Attributes
`h`  
---  
`hue`  
`s`  
`saturation`  
`v`  
`value`  
Parameters:
    
  * **hsv** ([_HSV_Array_Float_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.HSV_Array_Float> "manim.typing.HSV_Array_Float") _|_[_HSV_Tuple_Float_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.HSV_Tuple_Float> "manim.typing.HSV_Tuple_Float") _|_[_HSVA_Array_Float_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.HSVA_Array_Float> "manim.typing.HSVA_Array_Float") _|_[_HSVA_Tuple_Float_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.HSVA_Tuple_Float> "manim.typing.HSVA_Tuple_Float"))
  * **alpha** (_float_)


_classmethod_ _from_internal(_value_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/color/core.html#HSV._from_internal>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._from_internal> "Link to this definition")
    
This method is intended to be overwritten by custom color space classes which are subtypes of `[ManimColor`](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor").
The method constructs a new object of the given class by transforming the value in the internal format `[r,g,b,a]` into a format which the constructor of the custom class can understand. Look at `[HSV`](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV> "manim.utils.color.core.HSV") for an example.
Parameters:
    
**value** ([_ManimColorInternal_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.ManimColorInternal> "manim.typing.ManimColorInternal"))
Return type:
    
_Self_
_property_ _internal_space _: ndarray[tuple[int,...],dtype[_ScalarType_co]]_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._internal_space> "Link to this definition")
    
This is a readonly property which is a custom representation for color space operations. It is used for operators and can be used when implementing a custom color space.
_property_ _internal_value _:[ ManimColorInternal](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.ManimColorInternal> "manim.typing.ManimColorInternal")_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._internal_value> "Link to this definition")
    
Return the internal value of the current `[ManimColor`](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor") as an `[r,g,b,a]` float array.
Returns:
    
Internal color representation.
Return type:
    
[ManimColorInternal](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.ManimColorInternal> "manim.typing.ManimColorInternal")
[ Next ManimColor ](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html>) [ Previous core ](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [HSV](https://docs.manim.community/en/stable/reference/<#>)
    * `[HSV`](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV>)
      * `[HSV._from_internal()`](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._from_internal>)
      * `[HSV._internal_space`](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._internal_space>)
      * `[HSV._internal_value`](https://docs.manim.community/en/stable/reference/<#manim.utils.color.core.HSV._internal_value>)


