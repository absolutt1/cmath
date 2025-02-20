# MultiCamera[¶](https://docs.manim.community/en/stable/reference/<#multicamera> "Link to this heading")
Qualified name: `manim.camera.multi\_camera.MultiCamera`
_class_ MultiCamera(_image_mobjects_from_cameras =None_, _allow_cameras_to_capture_their_own_display =False_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera> "Link to this definition")
    
Bases: `[MovingCamera`](https://docs.manim.community/en/stable/reference/<manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera> "manim.camera.moving_camera.MovingCamera")
Camera Object that allows for multiple perspectives.
Initialises the MultiCamera
Parameters:
    
  * **image_mobjects_from_cameras** ([_ImageMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject> "manim.mobject.types.image_mobject.ImageMobject") _|__None_)
  * **kwargs** – Any valid keyword arguments of MovingCamera.


Methods
`[add_image_mobject_from_camera`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera> "manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera") | Adds an ImageMobject that's been obtained from the camera into the list `self.image_mobject_from_cameras`  
---|---  
`[capture_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.capture_mobjects> "manim.camera.multi_camera.MultiCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`.  
`[get_mobjects_indicating_movement`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement> "manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement") | Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving  
`[reset`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.reset> "manim.camera.multi_camera.MultiCamera.reset") | Resets the MultiCamera.  
`[update_sub_cameras`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.update_sub_cameras> "manim.camera.multi_camera.MultiCamera.update_sub_cameras") | Reshape sub_camera pixel_arrays  
Attributes
`background_color`  
---  
`background_opacity`  
`frame_center` | Returns the centerpoint of the frame in cartesian coordinates.  
`frame_height` | Returns the height of the frame.  
`frame_width` | Returns the width of the frame  
add_image_mobject_from_camera(_image_mobject_from_camera_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera.add_image_mobject_from_camera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera> "Link to this definition")
    
Adds an ImageMobject that’s been obtained from the camera into the list `self.image_mobject_from_cameras`
Parameters:
    
**image_mobject_from_camera** ([_ImageMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject> "manim.mobject.types.image_mobject.ImageMobject")) – The ImageMobject to add to self.image_mobject_from_cameras
capture_mobjects(_mobjects_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera.capture_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.capture_mobjects> "Link to this definition")
    
Capture mobjects by printing them on `pixel_array`.
This is the essential function that converts the contents of a Scene into an array, which is then converted to an image or video.
Parameters:
    
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes
For a list of classes that can currently be rendered, see `display_funcs()`.
get_mobjects_indicating_movement()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera.get_mobjects_indicating_movement>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement> "Link to this definition")
    
Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving
Return type:
    
list
reset()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera.reset>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.reset> "Link to this definition")
    
Resets the MultiCamera.
Returns:
    
The reset MultiCamera
Return type:
    
[MultiCamera](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera> "manim.camera.multi_camera.MultiCamera")
update_sub_cameras()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/multi_camera.html#MultiCamera.update_sub_cameras>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.update_sub_cameras> "Link to this definition")
    
Reshape sub_camera pixel_arrays
[ Next three_d_camera ](https://docs.manim.community/en/stable/reference/<manim.camera.three_d_camera.html>) [ Previous multi_camera ](https://docs.manim.community/en/stable/reference/<manim.camera.multi_camera.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MultiCamera](https://docs.manim.community/en/stable/reference/<#>)
    * `[MultiCamera`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera>)
      * `[MultiCamera.add_image_mobject_from_camera()`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera>)
      * `[MultiCamera.capture_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.capture_mobjects>)
      * `[MultiCamera.get_mobjects_indicating_movement()`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement>)
      * `[MultiCamera.reset()`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.reset>)
      * `[MultiCamera.update_sub_cameras()`](https://docs.manim.community/en/stable/reference/<#manim.camera.multi_camera.MultiCamera.update_sub_cameras>)


