
# zoomed_scene[¶](https://docs.manim.community/en/stable/reference/<#module-manim.scene.zoomed_scene> "Link to this heading")
A scene supporting zooming in on a specified section.
Examples
Example: UseZoomedScene [¶](https://docs.manim.community/en/stable/reference/<#usezoomedscene>)
```
frommanimimport *
classUseZoomedScene(ZoomedScene):
  defconstruct(self):
    dot = Dot().set_color(GREEN)
    self.add(dot)
    self.wait(1)
    self.activate_zooming(animate=False)
    self.wait(1)
    self.play(dot.animate.shift(LEFT))

```
Copy to clipboard
Make interactive
Example: ChangingZoomScale [¶](https://docs.manim.community/en/stable/reference/<#changingzoomscale>)
```
frommanimimport *
classChangingZoomScale(ZoomedScene):
  def__init__(self, **kwargs):
    ZoomedScene.__init__(
      self,
      zoom_factor=0.3,
      zoomed_display_height=1,
      zoomed_display_width=3,
      image_frame_stroke_width=20,
      zoomed_camera_config={
        "default_frame_stroke_width": 3,
      },
      **kwargs
    )
  defconstruct(self):
    dot = Dot().set_color(GREEN)
    sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
    self.add(dot, sq)
    self.wait(1)
    self.activate_zooming(animate=False)
    self.wait(1)
    self.play(dot.animate.shift(LEFT * 0.3))
    self.play(self.zoomed_camera.frame.animate.scale(4))
    self.play(self.zoomed_camera.frame.animate.shift(0.5 * DOWN))

```
Copy to clipboard
Make interactive
Classes
`[ZoomedScene`](https://docs.manim.community/en/stable/reference/<manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene> "manim.scene.zoomed_scene.ZoomedScene") | This is a Scene with special configurations made for when a particular part of the scene must be zoomed in on and displayed separately.  
---|---  
[ Next ZoomedScene ](https://docs.manim.community/en/stable/reference/<manim.scene.zoomed_scene.ZoomedScene.html>) [ Previous VectorScene ](https://docs.manim.community/en/stable/reference/<manim.scene.vector_space_scene.VectorScene.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
