# AbstractImageMobject[¶](https://docs.manim.community/en/stable/reference/<#abstractimagemobject> "Link to this heading")
Qualified name: `manim.mobject.types.image\_mobject.AbstractImageMobject`
_class_ AbstractImageMobject(_scale_to_resolution_ , _pixel_array_dtype ='uint8'_, _resampling_algorithm =Resampling.BICUBIC_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject> "Link to this definition")
    
Bases: `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Automatically filters out black pixels
Parameters:
    
  * **scale_to_resolution** (_int_) – At this resolution the image is placed pixel by pixel onto the screen, so it will look the sharpest and best. This is a custom parameter of ImageMobject so that rendering a scene with e.g. the `--quality low` or `--quality medium` flag for faster rendering won’t effect the position of the image on the screen.
  * **pixel_array_dtype** (_str_)
  * **resampling_algorithm** (_Resampling_)
  * **kwargs** (_Any_)


Methods
`get_pixel_array`  
---  
`[reset_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points> "manim.mobject.types.image_mobject.AbstractImageMobject.reset_points") | Sets `points` to be the four image corners.  
`[set_color`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_color> "manim.mobject.types.image_mobject.AbstractImageMobject.set_color") | Condition is function which takes in one arguments, (x, y, z).  
`[set_resampling_algorithm`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm> "manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm") | Sets the interpolation method for upscaling the image.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`depth` | The depth of the mobject.  
`height` | The height of the mobject.  
`width` | The width of the mobject.  
_original__init__(_scale_to_resolution_ , _pixel_array_dtype ='uint8'_, _resampling_algorithm =Resampling.BICUBIC_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **scale_to_resolution** (_int_)
  * **pixel_array_dtype** (_str_)
  * **resampling_algorithm** (_Resampling_)
  * **kwargs** (_Any_)


Return type:
    
None
reset_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.reset_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points> "Link to this definition")
    
Sets `points` to be the four image corners.
Return type:
    
None
set_color(_color_ , _alpha =None_, _family =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.set_color>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_color> "Link to this definition")
    
Condition is function which takes in one arguments, (x, y, z). Here it just recurses to submobjects, but in subclasses this should be further implemented based on the the inner workings of color
set_resampling_algorithm(_resampling_algorithm_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.set_resampling_algorithm>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm> "Link to this definition")
    
Sets the interpolation method for upscaling the image. By default the image is interpolated using bicubic algorithm. This method lets you change it. Interpolation is done internally using Pillow, and the function besides the string constants describing the algorithm accepts the Pillow integer constants.
Parameters:
    
**resampling_algorithm** (_int_) – 
An integer constant described in the Pillow library, or one from the RESAMPLING_ALGORITHMS global dictionary, under the following keys:
  * ’bicubic’ or ‘cubic’
  * ’nearest’ or ‘none’
  * ’box’
  * ’bilinear’ or ‘linear’
  * ’hamming’
  * ’lanczos’ or ‘antialias’


Return type:
    
Self
[ Next ImageMobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.image_mobject.ImageMobject.html>) [ Previous image_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.image_mobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [AbstractImageMobject](https://docs.manim.community/en/stable/reference/<#>)
    * `[AbstractImageMobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject>)
      * `[AbstractImageMobject._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject._original__init__>)
      * `[AbstractImageMobject.reset_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points>)
      * `[AbstractImageMobject.set_color()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_color>)
      * `[AbstractImageMobject.set_resampling_algorithm()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm>)


