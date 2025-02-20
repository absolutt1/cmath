
# typing[¶](https://docs.manim.community/en/stable/reference/<#module-manim.typing> "Link to this heading")
Custom type definitions used in Manim.
Note for developers
Around the source code there are multiple strings which look like this:
```
'''
[CATEGORY]
<category_name>
'''

```
Copy to clipboard
All type aliases defined under those strings will be automatically classified under that category.
If you need to define a new category, respect the format described above.
Type Aliases
### Primitive data types[¶](https://docs.manim.community/en/stable/reference/<#primitive_data_types> "Link to this heading")
_class_ ManimFloat[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimFloat> "Link to this definition")
    
```
np.float64

```
Copy to clipboard
A double-precision floating-point value (64 bits, or 8 bytes), according to the IEEE 754 standard.
_class_ ManimInt[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt> "Link to this definition")
    
```
np.int64

```
Copy to clipboard
A long integer (64 bits, or 8 bytes).
It can take values between −263 and +263−1, which expressed in base 10 is a range between around −9.223⋅1018 and +9.223⋅1018.
### Color types[¶](https://docs.manim.community/en/stable/reference/<#color_types> "Link to this heading")
_class_ ManimColorDType[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorDType> "Link to this definition")
```
[ManimFloat](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimFloat> "manim.typing.ManimFloat")
```

Data type used in `[ManimColorInternal`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorInternal> "manim.typing.ManimColorInternal"): a double-precision float between 0 and 1.
_class_ RGB_Array_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Float> "Link to this definition")
```
NDArray[[ManimColorDType](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorDType> "manim.typing.ManimColorDType")]
```

`shape: (3,)`
A `numpy.ndarray` of 3 floats between 0 and 1, representing a color in RGB format.
Its components describe, in order, the intensity of Red, Green, and Blue in the represented color.
_class_ RGB_Tuple_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Float> "Link to this definition")
    
```
tuple[float, float, float]

```
Copy to clipboard
`shape: (3,)`
A tuple of 3 floats between 0 and 1, representing a color in RGB format.
Its components describe, in order, the intensity of Red, Green, and Blue in the represented color.
_class_ RGB_Array_Int[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Int> "Link to this definition")
```
NDArray[[ManimInt](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt> "manim.typing.ManimInt")]
```

`shape: (3,)`
A `numpy.ndarray` of 3 integers between 0 and 255, representing a color in RGB format.
Its components describe, in order, the intensity of Red, Green, and Blue in the represented color.
_class_ RGB_Tuple_Int[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Int> "Link to this definition")
    
```
tuple[int, int, int]

```
Copy to clipboard
`shape: (3,)`
A tuple of 3 integers between 0 and 255, representing a color in RGB format.
Its components describe, in order, the intensity of Red, Green, and Blue in the represented color.
_class_ RGBA_Array_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Float> "Link to this definition")
```
NDArray[[ManimColorDType](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorDType> "manim.typing.ManimColorDType")]
```

`shape: (4,)`
A `numpy.ndarray` of 4 floats between 0 and 1, representing a color in RGBA format.
Its components describe, in order, the intensity of Red, Green, Blue and Alpha (opacity) in the represented color.
_class_ RGBA_Tuple_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Tuple_Float> "Link to this definition")
    
```
tuple[float, float, float, float]

```
Copy to clipboard
`shape: (4,)`
A tuple of 4 floats between 0 and 1, representing a color in RGBA format.
Its components describe, in order, the intensity of Red, Green, Blue and Alpha (opacity) in the represented color.
_class_ RGBA_Array_Int[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Int> "Link to this definition")
```
NDArray[[ManimInt](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt> "manim.typing.ManimInt")]
```

`shape: (4,)`
A `numpy.ndarray` of 4 integers between 0 and 255, representing a color in RGBA format.
Its components describe, in order, the intensity of Red, Green, Blue and Alpha (opacity) in the represented color.
_class_ RGBA_Tuple_Int[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Tuple_Int> "Link to this definition")
    
```
tuple[int, int, int, int]

```
Copy to clipboard
`shape: (4,)`
A tuple of 4 integers between 0 and 255, representing a color in RGBA format.
Its components describe, in order, the intensity of Red, Green, Blue and Alpha (opacity) in the represented color.
_class_ HSV_Array_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSV_Array_Float> "Link to this definition")
```
[RGB_Array_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Float> "manim.typing.RGB_Array_Float")
```

`shape: (3,)`
A `numpy.ndarray` of 3 floats between 0 and 1, representing a color in HSV (or HSB) format.
Its components describe, in order, the Hue, Saturation and Value (or Brightness) in the represented color.
_class_ HSV_Tuple_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSV_Tuple_Float> "Link to this definition")
```
[RGB_Tuple_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Float> "manim.typing.RGB_Tuple_Float")
```

`shape: (3,)`
A tuple of 3 floats between 0 and 1, representing a color in HSV (or HSB) format.
Its components describe, in order, the Hue, Saturation and Value (or Brightness) in the represented color.
_class_ HSVA_Array_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSVA_Array_Float> "Link to this definition")
```
[RGBA_Array_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Float> "manim.typing.RGBA_Array_Float")
```

`shape: (4,)`
A `numpy.ndarray` of 4 floats between 0 and 1, representing a color in HSVA (or HSBA) format.
Its components describe, in order, the Hue, Saturation and Value (or Brightness) in the represented color.
_class_ HSVA_Tuple_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSVA_Tuple_Float> "Link to this definition")
```
[RGBA_Tuple_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Tuple_Float> "manim.typing.RGBA_Tuple_Float")
```

`shape: (4,)`
A tuple of 4 floats between 0 and 1, representing a color in HSVA (or HSBA) format.
Its components describe, in order, the Hue, Saturation and Value (or Brightness) in the represented color.
_class_ HSL_Array_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSL_Array_Float> "Link to this definition")
```
[RGB_Array_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Float> "manim.typing.RGB_Array_Float")
```

`shape: (3,)`
A `numpy.ndarray` of 3 floats between 0 and 1, representing a color in HSL format.
Its components describe, in order, the Hue, Saturation and Lightness in the represented color.
_class_ HSL_Tuple_Float[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.HSL_Tuple_Float> "Link to this definition")
```
[RGB_Tuple_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Float> "manim.typing.RGB_Tuple_Float")
```

`shape: (3,)`
A `numpy.ndarray` of 3 floats between 0 and 1, representing a color in HSL format.
Its components describe, in order, the Hue, Saturation and Lightness in the represented color.
_class_ ManimColorInternal[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorInternal> "Link to this definition")
```
[RGBA_Array_Float](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Float> "manim.typing.RGBA_Array_Float")
```

`shape: (4,)`
Internal color representation used by `[ManimColor`](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"), following the RGBA format.
It is a `numpy.ndarray` consisting of 4 floats between 0 and 1, describing respectively the intensities of Red, Green, Blue and Alpha (opacity) in the represented color.
### Point types[¶](https://docs.manim.community/en/stable/reference/<#point_types> "Link to this heading")
_class_ PointDType[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "Link to this definition")
```
[ManimFloat](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimFloat> "manim.typing.ManimFloat")
```

Default type for arrays representing points: a double-precision floating point value.
_class_ Point2D[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (2,)`
A NumPy array representing a 2-dimensional point: `[float, float]`.
_class_ Point2DLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike> "Link to this definition")
```
[Point2D](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D> "manim.typing.Point2D") | tuple[float, float]
```

`shape: (2,)`
A 2-dimensional point: `[float, float]`.
This represents anything which can be converted to a :class:`[Point2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D> "manim.typing.Point2D") NumPy array.
Normally, a function or method which expects a `[Point2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D> "manim.typing.Point2D") as a parameter can handle being passed a `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") instead.
_class_ Point2D_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, 2)`
A NumPy array representing a sequence of `[Point2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D> "manim.typing.Point2D") objects: `[[float, float], ...]`.
_class_ Point2DLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike_Array> "Link to this definition")
```
[Point2D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D_Array> "manim.typing.Point2D_Array") | Sequence[[Point2DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike> "manim.typing.Point2DLike")]
```

`shape: (M, 2)`
An array of `[Point2DLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike> "manim.typing.Point2DLike") objects: `[[float, float], ...]`.
This represents anything which can be converted to a :class:`[Point2D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D_Array> "manim.typing.Point2D_Array") NumPy array.
Normally, a function or method which expects a `[Point2D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D_Array> "manim.typing.Point2D_Array") as a parameter can handle being passed a `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") instead.
Please refer to the documentation of the function you are using for further type information.
_class_ Point3D[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (3,)`
A NumPy array representing a 3-dimensional point: `[float, float, float]`.
_class_ Point3DLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "Link to this definition")
```
[Point3D](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") | tuple[float, float, float]
```

`shape: (3,)`
A 3-dimensional point: `[float, float, float]`.
This represents anything which can be converted to a :class:`[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") NumPy array.
_class_ Point3D_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, 3)`
A NumPy array representing a sequence of `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects: `[[float, float, float], ...]`.
_class_ Point3DLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") | Sequence[[Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike")]
```

`shape: (M, 3)`
An array of `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects: `[[float, float, float], ...]`.
This represents anything which can be converted to a :class:`[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ PointND[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (N,)`
A NumPy array representing an N-dimensional point: `[float, ...]`.
_class_ PointNDLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PointNDLike> "Link to this definition")
```
[PointND](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND> "manim.typing.PointND") | Sequence[float]
```

`shape: (N,)`
An N-dimensional point: `[float, ...]`.
This represents anything which can be converted to a :class:`[PointND`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND> "manim.typing.PointND") NumPy array.
_class_ PointND_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, N)`
A NumPy array representing a sequence of `[PointND`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND> "manim.typing.PointND") objects: `[[float, ...], ...]`.
_class_ PointNDLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PointNDLike_Array> "Link to this definition")
```
[PointND_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND_Array> "manim.typing.PointND_Array") | Sequence[[PointNDLike](https://docs.manim.community/en/stable/reference/<#manim.typing.PointNDLike> "manim.typing.PointNDLike")]
```

`shape: (M, N)`
An array of `[PointND`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND> "manim.typing.PointND") objects: `[[float, ...], ...]`.
This represents anything which can be converted to a :class:`[PointND_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND_Array> "manim.typing.PointND_Array") NumPy array.
Please refer to the documentation of the function you are using for further type information.
### Vector types[¶](https://docs.manim.community/en/stable/reference/<#vector_types> "Link to this heading")
_class_ Vector2D[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (2,)`
A 2-dimensional vector: `[float, float]`.
Normally, a function or method which expects a `[Vector2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D> "manim.typing.Vector2D") as a parameter can handle being passed a `[Vector3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D> "manim.typing.Vector3D") instead.
Caution
Do not confuse with the `[Vector`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector> "manim.mobject.geometry.line.Vector") or `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow") VMobjects!
_class_ Vector2D_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, 2)`
An array of `[Vector2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D> "manim.typing.Vector2D") objects: `[[float, float], ...]`.
Normally, a function or method which expects a `[Vector2D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D_Array> "manim.typing.Vector2D_Array") as a parameter can handle being passed a `[Vector3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D_Array> "manim.typing.Vector3D_Array") instead.
_class_ Vector3D[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (3,)`
A 3-dimensional vector: `[float, float, float]`.
Caution
Do not confuse with the `[Vector`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector> "manim.mobject.geometry.line.Vector") or `[Arrow3D`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D> "manim.mobject.three_d.three_dimensions.Arrow3D") VMobjects!
_class_ Vector3D_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, 3)`
An array of `[Vector3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D> "manim.typing.Vector3D") objects: `[[float, float, float], ...]`.
_class_ VectorND[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.VectorND> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape (N,)`
An N-dimensional vector: `[float, ...]`.
Caution
Do not confuse with the `[Vector`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector> "manim.mobject.geometry.line.Vector") VMobject! This type alias is named “VectorND” instead of “Vector” to avoid potential name collisions.
_class_ VectorND_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.VectorND_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape (M, N)`
An array of `[VectorND`](https://docs.manim.community/en/stable/reference/<#manim.typing.VectorND> "manim.typing.VectorND") objects: `[[float, ...], ...]`.
_class_ RowVector[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RowVector> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (1, N)`
A row vector: `[[float, ...]]`.
_class_ ColVector[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.ColVector> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (N, 1)`
A column vector: `[[float], [float], ...]`.
### Matrix types[¶](https://docs.manim.community/en/stable/reference/<#matrix_types> "Link to this heading")
_class_ MatrixMN[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.MatrixMN> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (M, N)`
A matrix: `[[float, ...], [float, ...], ...]`.
_class_ Zeros[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Zeros> "Link to this definition")
```
[MatrixMN](https://docs.manim.community/en/stable/reference/<#manim.typing.MatrixMN> "manim.typing.MatrixMN")
```

`shape: (M, N)`
A `[MatrixMN`](https://docs.manim.community/en/stable/reference/<#manim.typing.MatrixMN> "manim.typing.MatrixMN") filled with zeros, typically created with `numpy.zeros((M, N))`.
### Bézier types[¶](https://docs.manim.community/en/stable/reference/<#bézier_types> "Link to this heading")
_class_ QuadraticBezierPoints[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (3, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of three 3D control points for a single quadratic Bézier curve: `[[float, float, float], [float, float, float], [float, float, float]]`.
_class_ QuadraticBezierPointsLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike> "Link to this definition")
```
[QuadraticBezierPoints](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints> "manim.typing.QuadraticBezierPoints") | tuple[[Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike")]
```

`shape: (3, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of three 3D control points for a single quadratic Bézier curve: `[[float, float, float], [float, float, float], [float, float, float]]`.
This represents anything which can be converted to a :class:`[QuadraticBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints> "manim.typing.QuadraticBezierPoints") NumPy array.
_class_ QuadraticBezierPoints_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (N, 3, 3)`
A NumPy array containing N `[QuadraticBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints> "manim.typing.QuadraticBezierPoints") objects: `[[[float, float, float], [float, float, float], [float, float, float]], ...]`.
_class_ QuadraticBezierPointsLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike_Array> "Link to this definition")
```
[QuadraticBezierPoints_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints_Array> "manim.typing.QuadraticBezierPoints_Array") | Sequence[[QuadraticBezierPointsLike](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike> "manim.typing.QuadraticBezierPointsLike")]
```

`shape: (N, 3, 3)`
A sequence of N `[QuadraticBezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike> "manim.typing.QuadraticBezierPointsLike") objects: `[[[float, float, float], [float, float, float], [float, float, float]], ...]`.
This represents anything which can be converted to a :class:`[QuadraticBezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints_Array> "manim.typing.QuadraticBezierPoints_Array") NumPy array.
_class_ QuadraticBezierPath[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPath> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (3*N, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of 3N points, where each one of the N consecutive blocks of 3 points represents a quadratic Bézier curve: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ QuadraticBezierPathLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPathLike> "Link to this definition")
```
[Point3DLike_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")
```

`shape: (3*N, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of 3N points, where each one of the N consecutive blocks of 3 points represents a quadratic Bézier curve: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[QuadraticBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPath> "manim.typing.QuadraticBezierPath") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ QuadraticSpline[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticSpline> "Link to this definition")
```
[QuadraticBezierPath](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPath> "manim.typing.QuadraticBezierPath")
```

`shape: (3*N, 3)`
A special case of `[QuadraticBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPath> "manim.typing.QuadraticBezierPath") where all the N quadratic Bézier curves are connected, forming a quadratic spline: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ QuadraticSplineLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticSplineLike> "Link to this definition")
```
[QuadraticBezierPathLike](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPathLike> "manim.typing.QuadraticBezierPathLike")
```

`shape: (3*N, 3)`
A special case of `[QuadraticBezierPathLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPathLike> "manim.typing.QuadraticBezierPathLike") where all the N quadratic Bézier curves are connected, forming a quadratic spline: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[QuadraticSpline`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticSpline> "manim.typing.QuadraticSpline") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ CubicBezierPoints[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (4, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of four 3D control points for a single cubic Bézier curve: `[[float, float, float], [float, float, float], [float, float, float], [float, float, float]]`.
_class_ CubicBezierPointsLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike> "Link to this definition")
```
[CubicBezierPoints](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints> "manim.typing.CubicBezierPoints") | tuple[[Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike")]
```

`shape: (4, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of 4 control points for a single cubic Bézier curve: `[[float, float, float], [float, float, float], [float, float, float], [float, float, float]]`.
This represents anything which can be converted to a :class:`[CubicBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints> "manim.typing.CubicBezierPoints") NumPy array.
_class_ CubicBezierPoints_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (N, 4, 3)`
A NumPy array containing N `[CubicBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints> "manim.typing.CubicBezierPoints") objects: `[[[float, float, float], [float, float, float], [float, float, float], [float, float, float]], ...]`.
_class_ CubicBezierPointsLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike_Array> "Link to this definition")
```
[CubicBezierPoints_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints_Array> "manim.typing.CubicBezierPoints_Array") | Sequence[[CubicBezierPointsLike](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike> "manim.typing.CubicBezierPointsLike")]
```

`shape: (N, 4, 3)`
A sequence of N `[CubicBezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike> "manim.typing.CubicBezierPointsLike") objects: `[[[float, float, float], [float, float, float], [float, float, float], [float, float, float]], ...]`.
This represents anything which can be converted to a :class:`[CubicBezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints_Array> "manim.typing.CubicBezierPoints_Array") NumPy array.
_class_ CubicBezierPath[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (4*N, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of 4N points, where each one of the N consecutive blocks of 4 points represents a cubic Bézier curve: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ CubicBezierPathLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPathLike> "Link to this definition")
```
[Point3DLike_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")
```

`shape: (4*N, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of 4N points, where each one of the N consecutive blocks of 4 points represents a cubic Bézier curve: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[CubicBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath> "manim.typing.CubicBezierPath") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ CubicSpline[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicSpline> "Link to this definition")
```
[CubicBezierPath](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath> "manim.typing.CubicBezierPath")
```

`shape: (4*N, 3)`
A special case of `[CubicBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath> "manim.typing.CubicBezierPath") where all the N cubic Bézier curves are connected, forming a quadratic spline: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ CubicSplineLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicSplineLike> "Link to this definition")
```
[CubicBezierPathLike](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPathLike> "manim.typing.CubicBezierPathLike")
```

`shape: (4*N, 3)`
A special case of `[CubicBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath> "manim.typing.CubicBezierPath") where all the N cubic Bézier curves are connected, forming a quadratic spline: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[CubicSpline`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicSpline> "manim.typing.CubicSpline") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPoints[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (PPC, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of PPC control points (PPC: Points Per Curve=n+1) for a single n-th degree Bézier curve: `[[float, float, float], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPointsLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike> "Link to this definition")
```
[Point3DLike_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")
```

`shape: (PPC, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of PPC control points (PPC: Points Per Curve=n+1) for a single n-th degree Bézier curve: `[[float, float, float], ...]`.
This represents anything which can be converted to a :class:`[BezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints> "manim.typing.BezierPoints") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPoints_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints_Array> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")]
```

`shape: (N, PPC, 3)`
A NumPy array of N `[BezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints> "manim.typing.BezierPoints") objects containing PPC `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects each (PPC: Points Per Curve=n+1): `[[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPointsLike_Array[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike_Array> "Link to this definition")
```
[BezierPoints_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints_Array> "manim.typing.BezierPoints_Array") | Sequence[[BezierPointsLike](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike> "manim.typing.BezierPointsLike")]
```

`shape: (N, PPC, 3)`
A sequence of N `[BezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike> "manim.typing.BezierPointsLike") objects containing PPC `[Point3DLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike") objects each (PPC: Points Per Curve=n+1): `[[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[BezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints_Array> "manim.typing.BezierPoints_Array") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPath[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPath> "Link to this definition")
```
[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")
```

`shape: (PPC*N, 3)`
A `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") of PPC⋅N points, where each one of the N consecutive blocks of PPC control points (PPC: Points Per Curve=n+1) represents a Bézier curve of n-th degree: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ BezierPathLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPathLike> "Link to this definition")
```
[Point3DLike_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array")
```

`shape: (PPC*N, 3)`
A `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array> "manim.typing.Point3DLike_Array") of PPC⋅N points, where each one of the N consecutive blocks of PPC control points (PPC: Points Per Curve=n+1) represents a Bézier curve of n-th degree: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[BezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPath> "manim.typing.BezierPath") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ Spline[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.Spline> "Link to this definition")
```
[BezierPath](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPath> "manim.typing.BezierPath")
```

`shape: (PPC*N, 3)`
A special case of `[BezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPath> "manim.typing.BezierPath") where all the N Bézier curves consisting of PPC `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects (PPC: Points Per Curve=n+1) are connected, forming an n-th degree spline: `[[float, float, float], ...], ...]`.
Please refer to the documentation of the function you are using for further type information.
_class_ SplineLike[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.SplineLike> "Link to this definition")
```
[BezierPathLike](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPathLike> "manim.typing.BezierPathLike")
```

`shape: (PPC*N, 3)`
A special case of `[BezierPathLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPathLike> "manim.typing.BezierPathLike") where all the N Bézier curves consisting of PPC `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects (PPC: Points Per Curve=n+1) are connected, forming an n-th degree spline: `[[float, float, float], ...], ...]`.
This represents anything which can be converted to a :class:`[Spline`](https://docs.manim.community/en/stable/reference/<#manim.typing.Spline> "manim.typing.Spline") NumPy array.
Please refer to the documentation of the function you are using for further type information.
_class_ FlatBezierPoints[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.FlatBezierPoints> "Link to this definition")
```
NDArray[[PointDType](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType> "manim.typing.PointDType")] | tuple[float, ...]
```

`shape: (3*PPC*N,)`
A flattened array of Bézier control points: `[float, ...]`.
### Function types[¶](https://docs.manim.community/en/stable/reference/<#function_types> "Link to this heading")
_class_ FunctionOverride[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.FunctionOverride> "Link to this definition")
    
```
Callable

```
Copy to clipboard
Function type returning an `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") for the specified `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
_class_ PathFuncType[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PathFuncType> "Link to this definition")
```
Callable[[[Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike"), float], [Point3DLike](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike> "manim.typing.Point3DLike")]
```

Function mapping two :class:`[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") objects and an alpha value to a new :class:`[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D").
_class_ MappingFunction[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.MappingFunction> "Link to this definition")
```
Callable[[[Point3D](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D")], [Point3D](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D")]
```

A function mapping a :class:`[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D") to another :class:`[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D> "manim.typing.Point3D").
_class_ MultiMappingFunction[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.MultiMappingFunction> "Link to this definition")
```
Callable[[[Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")], [Point3D_Array](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array")]
```

A function mapping a :class:`[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array") to another :class:`[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array> "manim.typing.Point3D_Array").
### Image types[¶](https://docs.manim.community/en/stable/reference/<#image_types> "Link to this heading")
_class_ PixelArray[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "Link to this definition")
```
NDArray[[ManimInt](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt> "manim.typing.ManimInt")]
```

`shape: (height, width) | (height, width, 3) | (height, width, 4)`
A rasterized image with a height of `height` pixels and a width of `width` pixels.
Every value in the array is an integer from 0 to 255.
Every pixel is represented either by a single integer indicating its lightness (for greyscale images), an `[RGB_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Int> "manim.typing.RGB_Array_Int") or an `[RGBA_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Int> "manim.typing.RGBA_Array_Int").
_class_ GrayscalePixelArray[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.GrayscalePixelArray> "Link to this definition")
```
[PixelArray](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray")
```

`shape: (height, width)`
A 100% opaque grayscale `[PixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray"), where every pixel value is a `[ManimInt`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt> "manim.typing.ManimInt") indicating its lightness (black -> gray -> white).
_class_ RGBPixelArray[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBPixelArray> "Link to this definition")
```
[PixelArray](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray")
```

`shape: (height, width, 3)`
A 100% opaque `[PixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray") in color, where every pixel value is an `[RGB_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Int> "manim.typing.RGB_Array_Int") object.
_class_ RGBAPixelArray[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBAPixelArray> "Link to this definition")
```
[PixelArray](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray")
```

`shape: (height, width, 4)`
A `[PixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray> "manim.typing.PixelArray") in color where pixels can be transparent. Every pixel value is an `[RGBA_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Int> "manim.typing.RGBA_Array_Int") object.
### Path types[¶](https://docs.manim.community/en/stable/reference/<#path_types> "Link to this heading")
_class_ StrPath[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.StrPath> "Link to this definition")
    
```
str | PathLike[str]

```
Copy to clipboard
A string or `os.PathLike` representing a path to a directory or file.
_class_ StrOrBytesPath[¶](https://docs.manim.community/en/stable/reference/<#manim.typing.StrOrBytesPath> "Link to this definition")
    
```
str | bytes | PathLike[str] | PathLike[bytes]

```
Copy to clipboard
A string, bytes or `os.PathLike` object representing a path to a directory or file.
[ Next Plugins ](https://docs.manim.community/en/stable/reference/<../plugins.html>) [ Previous TexTemplateLibrary ](https://docs.manim.community/en/stable/reference/<manim.utils.tex_templates.TexTemplateLibrary.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [typing](https://docs.manim.community/en/stable/reference/<#>)
    * `[ManimFloat`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimFloat>)
    * `[ManimInt`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimInt>)
    * `[ManimColorDType`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorDType>)
    * `[RGB_Array_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Float>)
    * `[RGB_Tuple_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Float>)
    * `[RGB_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Array_Int>)
    * `[RGB_Tuple_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGB_Tuple_Int>)
    * `[RGBA_Array_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Float>)
    * `[RGBA_Tuple_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Tuple_Float>)
    * `[RGBA_Array_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Array_Int>)
    * `[RGBA_Tuple_Int`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBA_Tuple_Int>)
    * `[HSV_Array_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSV_Array_Float>)
    * `[HSV_Tuple_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSV_Tuple_Float>)
    * `[HSVA_Array_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSVA_Array_Float>)
    * `[HSVA_Tuple_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSVA_Tuple_Float>)
    * `[HSL_Array_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSL_Array_Float>)
    * `[HSL_Tuple_Float`](https://docs.manim.community/en/stable/reference/<#manim.typing.HSL_Tuple_Float>)
    * `[ManimColorInternal`](https://docs.manim.community/en/stable/reference/<#manim.typing.ManimColorInternal>)
    * `[PointDType`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointDType>)
    * `[Point2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D>)
    * `[Point2DLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike>)
    * `[Point2D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2D_Array>)
    * `[Point2DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point2DLike_Array>)
    * `[Point3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D>)
    * `[Point3DLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike>)
    * `[Point3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3D_Array>)
    * `[Point3DLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Point3DLike_Array>)
    * `[PointND`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND>)
    * `[PointNDLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointNDLike>)
    * `[PointND_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointND_Array>)
    * `[PointNDLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.PointNDLike_Array>)
    * `[Vector2D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D>)
    * `[Vector2D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector2D_Array>)
    * `[Vector3D`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D>)
    * `[Vector3D_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.Vector3D_Array>)
    * `[VectorND`](https://docs.manim.community/en/stable/reference/<#manim.typing.VectorND>)
    * `[VectorND_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.VectorND_Array>)
    * `[RowVector`](https://docs.manim.community/en/stable/reference/<#manim.typing.RowVector>)
    * `[ColVector`](https://docs.manim.community/en/stable/reference/<#manim.typing.ColVector>)
    * `[MatrixMN`](https://docs.manim.community/en/stable/reference/<#manim.typing.MatrixMN>)
    * `[Zeros`](https://docs.manim.community/en/stable/reference/<#manim.typing.Zeros>)
    * `[QuadraticBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints>)
    * `[QuadraticBezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike>)
    * `[QuadraticBezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPoints_Array>)
    * `[QuadraticBezierPointsLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPointsLike_Array>)
    * `[QuadraticBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPath>)
    * `[QuadraticBezierPathLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticBezierPathLike>)
    * `[QuadraticSpline`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticSpline>)
    * `[QuadraticSplineLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.QuadraticSplineLike>)
    * `[CubicBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints>)
    * `[CubicBezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike>)
    * `[CubicBezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPoints_Array>)
    * `[CubicBezierPointsLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPointsLike_Array>)
    * `[CubicBezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPath>)
    * `[CubicBezierPathLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicBezierPathLike>)
    * `[CubicSpline`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicSpline>)
    * `[CubicSplineLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.CubicSplineLike>)
    * `[BezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints>)
    * `[BezierPointsLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike>)
    * `[BezierPoints_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPoints_Array>)
    * `[BezierPointsLike_Array`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPointsLike_Array>)
    * `[BezierPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPath>)
    * `[BezierPathLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.BezierPathLike>)
    * `[Spline`](https://docs.manim.community/en/stable/reference/<#manim.typing.Spline>)
    * `[SplineLike`](https://docs.manim.community/en/stable/reference/<#manim.typing.SplineLike>)
    * `[FlatBezierPoints`](https://docs.manim.community/en/stable/reference/<#manim.typing.FlatBezierPoints>)
    * `[FunctionOverride`](https://docs.manim.community/en/stable/reference/<#manim.typing.FunctionOverride>)
    * `[PathFuncType`](https://docs.manim.community/en/stable/reference/<#manim.typing.PathFuncType>)
    * `[MappingFunction`](https://docs.manim.community/en/stable/reference/<#manim.typing.MappingFunction>)
    * `[MultiMappingFunction`](https://docs.manim.community/en/stable/reference/<#manim.typing.MultiMappingFunction>)
    * `[PixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.PixelArray>)
    * `[GrayscalePixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.GrayscalePixelArray>)
    * `[RGBPixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBPixelArray>)
    * `[RGBAPixelArray`](https://docs.manim.community/en/stable/reference/<#manim.typing.RGBAPixelArray>)
    * `[StrPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.StrPath>)
    * `[StrOrBytesPath`](https://docs.manim.community/en/stable/reference/<#manim.typing.StrOrBytesPath>)


