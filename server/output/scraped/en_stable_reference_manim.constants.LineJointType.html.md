
# LineJointType[¶](https://docs.manim.community/en/stable/reference/<#linejointtype> "Link to this heading")
Qualified name: `manim.constants.LineJointType`
_class_ LineJointType(_value_ , _names= <not given>_, _*values_ , _module=None_ , _qualname=None_ , _type=None_ , _start=1_ , _boundary=None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/constants.html#LineJointType>)[¶](https://docs.manim.community/en/stable/reference/<#manim.constants.LineJointType> "Link to this definition")
    
Bases: `Enum`
Collection of available line joint types.
See the example below for a visual illustration of the different joint types.
Examples
Example: LineJointVariants [¶](https://docs.manim.community/en/stable/reference/<#linejointvariants>)
![../_images/LineJointVariants-1.png](https://docs.manim.community/en/stable/_images/LineJointVariants-1.png)
```
frommanimimport *
classLineJointVariants(Scene):
  defconstruct(self):
    mob = VMobject(stroke_width=20, color=GREEN).set_points_as_corners([
      np.array([-2, 0, 0]),
      np.array([0, 0, 0]),
      np.array([-2, 1, 0]),
    ])
    lines = VGroup(*[mob.copy() for _ in range(len(LineJointType))])
    for line, joint_type in zip(lines, LineJointType):
      line.joint_type = joint_type
    lines.arrange(RIGHT, buff=1)
    self.add(lines)
    for line in lines:
      label = Text(line.joint_type.name).next_to(line, DOWN)
      self.add(label)

```
Copy to clipboard
Make interactive
Attributes
`AUTO`  
---  
`ROUND`  
`BEVEL`  
`MITER`  
[ Next QualityDict ](https://docs.manim.community/en/stable/reference/<manim.constants.QualityDict.html>) [ Previous CapStyleType ](https://docs.manim.community/en/stable/reference/<manim.constants.CapStyleType.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LineJointType](https://docs.manim.community/en/stable/reference/<#>)
    * `[LineJointType`](https://docs.manim.community/en/stable/reference/<#manim.constants.LineJointType>)


