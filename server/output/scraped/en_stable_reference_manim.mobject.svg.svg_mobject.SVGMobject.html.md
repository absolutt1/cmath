# SVGMobject[¶](https://docs.manim.community/en/stable/reference/<#svgmobject> "Link to this heading")
Qualified name: `manim.mobject.svg.svg\_mobject.SVGMobject`
_class_ SVGMobject(_file_name =None_, _should_center =True_, _height =2_, _width =None_, _color =None_, _opacity =None_, _fill_color =None_, _fill_opacity =None_, _stroke_color =None_, _stroke_opacity =None_, _stroke_width =None_, _svg_default =None_, _path_string_config =None_, _use_svg_cache =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A vectorized mobject created from importing an SVG file.
Parameters:
    
  * **file_name** (_str_ _|__os.PathLike_ _|__None_) – The path to the SVG file.
  * **should_center** (_bool_) – Whether or not the mobject should be centered after being imported.
  * **height** (_float_ _|__None_) – The target height of the mobject, set to 2 Manim units by default. If the height and width are both set to `None`, the mobject is imported without being scaled.
  * **width** (_float_ _|__None_) – The target width of the mobject, set to `None` by default. If the height and the width are both set to `None`, the mobject is imported without being scaled.
  * **color** (_str_ _|__None_) – The color (both fill and stroke color) of the mobject. If `None` (the default), the colors set in the SVG file are used.
  * **opacity** (_float_ _|__None_) – The opacity (both fill and stroke opacity) of the mobject. If `None` (the default), the opacity set in the SVG file is used.
  * **fill_color** (_str_ _|__None_) – The fill color of the mobject. If `None` (the default), the fill colors set in the SVG file are used.
  * **fill_opacity** (_float_ _|__None_) – The fill opacity of the mobject. If `None` (the default), the fill opacities set in the SVG file are used.
  * **stroke_color** (_str_ _|__None_) – The stroke color of the mobject. If `None` (the default), the stroke colors set in the SVG file are used.
  * **stroke_opacity** (_float_ _|__None_) – The stroke opacity of the mobject. If `None` (the default), the stroke opacities set in the SVG file are used.
  * **stroke_width** (_float_ _|__None_) – The stroke width of the mobject. If `None` (the default), the stroke width values set in the SVG file are used.
  * **svg_default** (_dict_ _|__None_) – A dictionary in which fallback values for unspecified properties of elements in the SVG file are defined. If `None` (the default), `color`, `opacity`, `fill_color` `fill_opacity`, `stroke_color`, and `stroke_opacity` are set to `None`, and `stroke_width` is set to 0.
  * **path_string_config** (_dict_ _|__None_) – A dictionary with keyword arguments passed to `[VMobjectFromSVGPath`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath> "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath") used for importing path elements. If `None` (the default), no additional arguments are passed.
  * **use_svg_cache** (_bool_) – If True (default), the svg inputs (e.g. file_name, settings) will be used as a key and a copy of the created mobject will be saved using that key to be quickly retrieved if the same inputs need be processed later. For large SVGs which are used only once, this can be omitted to improve performance.
  * **kwargs** – Further arguments passed to the parent class.


Methods
`[apply_style_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject") | Apply SVG style information to the converted mobject.  
---|---  
`[ellipse_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject") | Convert an ellipse or circle element to a vectorized mobject.  
`[generate_config_style_dict`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict> "manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict") | Generate a dictionary holding the default style information.  
`[generate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject") | Parse the SVG and translate its elements to submobjects.  
`[get_file_path`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path> "manim.mobject.svg.svg_mobject.SVGMobject.get_file_path") | Search for an existing file based on the specified file name.  
`[get_mobjects_from`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from> "manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from") | Convert the elements of the SVG to a list of mobjects.  
`[handle_transform`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform> "manim.mobject.svg.svg_mobject.SVGMobject.handle_transform") | Apply SVG transformations to the converted mobject.  
`[init_svg_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject") | Checks whether the SVG has already been imported and generates it if not.  
`[line_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject") | Convert a line element to a vectorized mobject.  
`[modify_xml_tree`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree> "manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree") | Modifies the SVG element tree to include default style information.  
`[move_into_position`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position> "manim.mobject.svg.svg_mobject.SVGMobject.move_into_position") | Scale and move the generated mobject into position.  
`[path_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject") | Convert a path element to a vectorized mobject.  
`[polygon_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject") | Convert a polygon element to a vectorized mobject.  
`[polyline_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject") | Convert a polyline element to a vectorized mobject.  
`[rect_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject") | Convert a rectangle element to a vectorized mobject.  
`[text_to_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject") | Convert a text element to a vectorized mobject.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`[hash_seed`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed> "manim.mobject.svg.svg_mobject.SVGMobject.hash_seed") | A unique hash representing the result of the generated mobject points.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_file_name =None_, _should_center =True_, _height =2_, _width =None_, _color =None_, _opacity =None_, _fill_color =None_, _fill_opacity =None_, _stroke_color =None_, _stroke_opacity =None_, _stroke_width =None_, _svg_default =None_, _path_string_config =None_, _use_svg_cache =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **file_name** (_str_ _|__PathLike_ _|__None_)
  * **should_center** (_bool_)
  * **height** (_float_ _|__None_)
  * **width** (_float_ _|__None_)
  * **color** (_str_ _|__None_)
  * **opacity** (_float_ _|__None_)
  * **fill_color** (_str_ _|__None_)
  * **fill_opacity** (_float_ _|__None_)
  * **stroke_color** (_str_ _|__None_)
  * **stroke_opacity** (_float_ _|__None_)
  * **stroke_width** (_float_ _|__None_)
  * **svg_default** (_dict_ _|__None_)
  * **path_string_config** (_dict_ _|__None_)
  * **use_svg_cache** (_bool_)


_static_ apply_style_to_mobject(_mob_ , _shape_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.apply_style_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject> "Link to this definition")
    
Apply SVG style information to the converted mobject.
Parameters:
    
  * **mob** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The converted mobject.
  * **shape** (_GraphicObject_) – The parsed SVG element.


Return type:
    
[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
_static_ ellipse_to_mobject(_ellipse_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.ellipse_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject> "Link to this definition")
    
Convert an ellipse or circle element to a vectorized mobject.
Parameters:
    
**ellipse** (_Ellipse_ _|__Circle_) – The parsed SVG ellipse or circle.
Return type:
    
[_Circle_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")
generate_config_style_dict()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.generate_config_style_dict>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict> "Link to this definition")
    
Generate a dictionary holding the default style information.
Return type:
    
dict[str, str]
generate_mobject()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.generate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject> "Link to this definition")
    
Parse the SVG and translate its elements to submobjects.
Return type:
    
None
get_file_path()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.get_file_path>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path> "Link to this definition")
    
Search for an existing file based on the specified file name.
Return type:
    
_Path_
get_mobjects_from(_svg_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.get_mobjects_from>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from> "Link to this definition")
    
Convert the elements of the SVG to a list of mobjects.
Parameters:
    
**svg** (_SVG_) – The parsed SVG file.
Return type:
    
list[[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")]
_static_ handle_transform(_mob_ , _matrix_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.handle_transform>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform> "Link to this definition")
    
Apply SVG transformations to the converted mobject.
Parameters:
    
  * **mob** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The converted mobject.
  * **matrix** (_Matrix_) – The transformation matrix determined from the SVG transformation.


Return type:
    
[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
_property_ hash_seed _: tuple_[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed> "Link to this definition")
    
A unique hash representing the result of the generated mobject points.
Used as keys in the `SVG_HASH_TO_MOB_MAP` caching dictionary.
init_svg_mobject(_use_svg_cache_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.init_svg_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject> "Link to this definition")
    
Checks whether the SVG has already been imported and generates it if not.
See also
`[SVGMobject.generate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject> "manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject")
Parameters:
    
**use_svg_cache** (_bool_)
Return type:
    
None
_static_ line_to_mobject(_line_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.line_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject> "Link to this definition")
    
Convert a line element to a vectorized mobject.
Parameters:
    
**line** (_Line_) – The parsed SVG line.
Return type:
    
[_Line_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
modify_xml_tree(_element_tree_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.modify_xml_tree>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree> "Link to this definition")
    
Modifies the SVG element tree to include default style information.
Parameters:
    
**element_tree** (_ElementTree_) – The parsed element tree from the SVG file.
Return type:
    
_ElementTree_
move_into_position()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.move_into_position>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position> "Link to this definition")
    
Scale and move the generated mobject into position.
Return type:
    
None
path_to_mobject(_path_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.path_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject> "Link to this definition")
    
Convert a path element to a vectorized mobject.
Parameters:
    
**path** (_Path_) – The parsed SVG path.
Return type:
    
[_VMobjectFromSVGPath_](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath> "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath")
_static_ polygon_to_mobject(_polygon_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.polygon_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject> "Link to this definition")
    
Convert a polygon element to a vectorized mobject.
Parameters:
    
**polygon** (_Polygon_) – The parsed SVG polygon.
Return type:
    
[_Polygon_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon")
polyline_to_mobject(_polyline_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.polyline_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject> "Link to this definition")
    
Convert a polyline element to a vectorized mobject.
Parameters:
    
**polyline** (_Polyline_) – The parsed SVG polyline.
Return type:
    
[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
_static_ rect_to_mobject(_rect_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.rect_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject> "Link to this definition")
    
Convert a rectangle element to a vectorized mobject.
Parameters:
    
**rect** (_Rect_) – The parsed SVG rectangle.
Return type:
    
[_Rectangle_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle")
_static_ text_to_mobject(_text_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.text_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject> "Link to this definition")
    
Convert a text element to a vectorized mobject.
Warning
Not yet implemented.
Parameters:
    
**text** (_Text_) – The parsed SVG text.
[ Next VMobjectFromSVGPath ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html>) [ Previous svg_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SVGMobject](https://docs.manim.community/en/stable/reference/<#>)
    * `[SVGMobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject>)
      * `[SVGMobject._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject._original__init__>)
      * `[SVGMobject.apply_style_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject>)
      * `[SVGMobject.ellipse_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject>)
      * `[SVGMobject.generate_config_style_dict()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict>)
      * `[SVGMobject.generate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject>)
      * `[SVGMobject.get_file_path()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path>)
      * `[SVGMobject.get_mobjects_from()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from>)
      * `[SVGMobject.handle_transform()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform>)
      * `[SVGMobject.hash_seed`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed>)
      * `[SVGMobject.init_svg_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject>)
      * `[SVGMobject.line_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject>)
      * `[SVGMobject.modify_xml_tree()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree>)
      * `[SVGMobject.move_into_position()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position>)
      * `[SVGMobject.path_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject>)
      * `[SVGMobject.polygon_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject>)
      * `[SVGMobject.polyline_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject>)
      * `[SVGMobject.rect_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject>)
      * `[SVGMobject.text_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject>)


