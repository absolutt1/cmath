# fading[¶](https://docs.manim.community/en/stable/reference/<#module-manim.animation.fading> "Link to this heading")
Fading in and out of view.
Example: Fading [¶](https://docs.manim.community/en/stable/reference/<#fading>)
```
frommanimimport *
classFading(Scene):
  defconstruct(self):
    tex_in = Tex("Fade", "In").scale(3)
    tex_out = Tex("Fade", "Out").scale(3)
    self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
    self.play(ReplacementTransform(tex_in, tex_out))
    self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

```
Copy to clipboard
Make interactive
Classes
`[FadeIn`](https://docs.manim.community/en/stable/reference/<manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn> "manim.animation.fading.FadeIn") | Fade in `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") s.  
---|---  
`[FadeOut`](https://docs.manim.community/en/stable/reference/<manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut> "manim.animation.fading.FadeOut") | Fade out `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") s.  
[ Next FadeIn ](https://docs.manim.community/en/stable/reference/<manim.animation.fading.FadeIn.html>) [ Previous Write ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Write.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
