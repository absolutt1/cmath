# MappingCamera[¶](https://docs.manim.community/en/stable/reference/<#mappingcamera> "Link to this heading")
Qualified name: `manim.camera.mapping\_camera.MappingCamera`
_class_ MappingCamera(_mapping_func= <function MappingCamera.<lambda>>_, _min_num_curves=50_ , _allow_object_intrusion=False_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#MappingCamera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.MappingCamera> "Link to this definition")
    
Bases: `[Camera`](https://docs.manim.community/en/stable/reference/<manim.camera.camera.Camera.html#manim.camera.camera.Camera> "manim.camera.camera.Camera")
Camera object that allows mapping between objects.
Methods
`[capture_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.MappingCamera.capture_mobjects> "manim.camera.mapping_camera.MappingCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`.  
---|---  
`points_to_pixel_coords`  
Attributes
`background_color`  
---  
`background_opacity`  
capture_mobjects(_mobjects_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/mapping_camera.html#MappingCamera.capture_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.MappingCamera.capture_mobjects> "Link to this definition")
    
Capture mobjects by printing them on `pixel_array`.
This is the essential function that converts the contents of a Scene into an array, which is then converted to an image or video.
Parameters:
    
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes
For a list of classes that can currently be rendered, see `display_funcs()`.
[ Next OldMultiCamera ](https://docs.manim.community/en/stable/reference/<manim.camera.mapping_camera.OldMultiCamera.html>) [ Previous mapping_camera ](https://docs.manim.community/en/stable/reference/<manim.camera.mapping_camera.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MappingCamera](https://docs.manim.community/en/stable/reference/<#>)
    * `[MappingCamera`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.MappingCamera>)
      * `[MappingCamera.capture_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.camera.mapping_camera.MappingCamera.capture_mobjects>)


