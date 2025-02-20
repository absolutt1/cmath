# OldMultiCamera[¶](https://docs.manim.community/en/stable/reference/<#oldmulticamera> "Link to this heading")
Qualified name: `manim.camera.mapping\_camera.OldMultiCamera`
_class_ OldMultiCamera(_* cameras_with_start_positions_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#OldMultiCamera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera> "Link to this definition")
    
Bases: `[Camera`](https://docs.manim.community/en/stable/reference/<manim.camera.camera.Camera.html#manim.camera.camera.Camera> "manim.camera.camera.Camera")
Methods
`[capture_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects> "manim.camera.mapping_camera.OldMultiCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`.  
---|---  
`[init_background`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.init_background> "manim.camera.mapping_camera.OldMultiCamera.init_background") | Initialize the background.  
`[set_background`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_background> "manim.camera.mapping_camera.OldMultiCamera.set_background") | Sets the background to the passed pixel_array after converting to valid RGB values.  
`[set_pixel_array`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array> "manim.camera.mapping_camera.OldMultiCamera.set_pixel_array") | Sets the pixel array of the camera to the passed pixel array.  
Attributes
`background_color`  
---  
`background_opacity`  
capture_mobjects(_mobjects_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#OldMultiCamera.capture_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects> "Link to this definition")
    
Capture mobjects by printing them on `pixel_array`.
This is the essential function that converts the contents of a Scene into an array, which is then converted to an image or video.
Parameters:
    
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes
For a list of classes that can currently be rendered, see `display_funcs()`.
init_background()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#OldMultiCamera.init_background>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.init_background> "Link to this definition")
    
Initialize the background. If self.background_image is the path of an image the image is set as background; else, the default background color fills the background.
set_background(_pixel_array_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#OldMultiCamera.set_background>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_background> "Link to this definition")
    
Sets the background to the passed pixel_array after converting to valid RGB values.
Parameters:
    
  * **pixel_array** – The pixel array to set the background to.
  * **convert_from_floats** – Whether or not to convert floats values to proper RGB valid ones, by default False


set_pixel_array(_pixel_array_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#OldMultiCamera.set_pixel_array>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array> "Link to this definition")
    
Sets the pixel array of the camera to the passed pixel array.
Parameters:
    
  * **pixel_array** – The pixel array to convert and then set as the camera’s pixel array.
  * **convert_from_floats** – Whether or not to convert float values to proper RGB values, by default False


[ Next SplitScreenCamera ](https://docs.manim.community/en/stable/reference/<manim.camera.mapping_camera.SplitScreenCamera.html>) [ Previous MappingCamera ](https://docs.manim.community/en/stable/reference/<manim.camera.mapping_camera.MappingCamera.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [OldMultiCamera](https://docs.manim.community/en/stable/reference/<#>)
    * `[OldMultiCamera`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera>)
      * `[OldMultiCamera.capture_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects>)
      * `[OldMultiCamera.init_background()`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.init_background>)
      * `[OldMultiCamera.set_background()`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_background>)
      * `[OldMultiCamera.set_pixel_array()`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array>)


