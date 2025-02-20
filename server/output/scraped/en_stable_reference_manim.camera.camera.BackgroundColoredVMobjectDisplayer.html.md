# BackgroundColoredVMobjectDisplayer[¶](https://docs.manim.community/en/stable/reference/<#backgroundcoloredvmobjectdisplayer> "Link to this heading")
Qualified name: `manim.camera.camera.BackgroundColoredVMobjectDisplayer`
_class_ BackgroundColoredVMobjectDisplayer(_camera_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer> "Link to this definition")
    
Bases: `object`
Auxiliary class that handles displaying vectorized mobjects with a set background image.
Parameters:
    
**camera** ([_Camera_](https://docs.manim.community/en/stable/reference/<manim.camera.camera.Camera.html#manim.camera.camera.Camera> "manim.camera.camera.Camera")) – Camera object to use.
Methods
`[display`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display> "manim.camera.camera.BackgroundColoredVMobjectDisplayer.display") | Displays the colored VMobjects.  
---|---  
`[get_background_array`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array> "manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array") | Gets the background array that has the passed file_name.  
`reset_pixel_array`  
`[resize_background_array`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array> "manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array") | Resizes the pixel array representing the background.  
`[resize_background_array_to_match`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match> "manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match") | Resizes the background array to match the passed pixel array.  
display(_* cvmobjects_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.display>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display> "Link to this definition")
    
Displays the colored VMobjects.
Parameters:
    
***cvmobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobjects
Returns:
    
The pixel array with the cvmobjects displayed.
Return type:
    
np.array
get_background_array(_image_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.get_background_array>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array> "Link to this definition")
    
Gets the background array that has the passed file_name.
Parameters:
    
**image** (_Image_ _|__Path_ _|__str_) – The background image or its file name.
Returns:
    
The pixel array of the image.
Return type:
    
np.ndarray
resize_background_array(_background_array_ , _new_width_ , _new_height_ , _mode ='RGBA'_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.resize_background_array>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array> "Link to this definition")
    
Resizes the pixel array representing the background.
Parameters:
    
  * **background_array** (_ndarray_) – The pixel
  * **new_width** (_float_) – The new width of the background
  * **new_height** (_float_) – The new height of the background
  * **mode** (_str_) – The PIL image mode, by default “RGBA”


Returns:
    
The numpy pixel array of the resized background.
Return type:
    
np.array
resize_background_array_to_match(_background_array_ , _pixel_array_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.resize_background_array_to_match>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match> "Link to this definition")
    
Resizes the background array to match the passed pixel array.
Parameters:
    
  * **background_array** (_ndarray_) – The prospective pixel array.
  * **pixel_array** (_ndarray_) – The pixel array whose width and height should be matched.


Returns:
    
The resized background array.
Return type:
    
np.array
[ Next Camera ](https://docs.manim.community/en/stable/reference/<manim.camera.camera.Camera.html>) [ Previous camera ](https://docs.manim.community/en/stable/reference/<manim.camera.camera.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [BackgroundColoredVMobjectDisplayer](https://docs.manim.community/en/stable/reference/<#>)
    * `[BackgroundColoredVMobjectDisplayer`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer>)
      * `[BackgroundColoredVMobjectDisplayer.display()`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display>)
      * `[BackgroundColoredVMobjectDisplayer.get_background_array()`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array>)
      * `[BackgroundColoredVMobjectDisplayer.resize_background_array()`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array>)
      * `[BackgroundColoredVMobjectDisplayer.resize_background_array_to_match()`](https://docs.manim.community/en/stable/reference/<#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match>)


