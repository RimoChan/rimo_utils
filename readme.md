# 莉沫工具箱

经常用到的一些小代码，原本它们是我的各个repo里的重复代码，想了想就整理出来单独做一个repo用来import好了。

## 内容

+ cv0
    - OpenCV的包装，解决一些OpenCV里让人不舒服的地方。
    - 包含了`cv2`原本的所有属性
    - `cv0.show(img)`
        - `cv2.imshow`的包装。
        - 不需要设置名字，自带`waitKey`。
    - `cv0.read(img_path)`
        - 替代`cv2.imread`。
        - 解决中文路径读取失败的问题。
        - 在读取失败时不返回`None`，而是`raise`
    - `cv0.write(img, img_path, param=None)`
        - 替代`cv2.imwrite`
        - 解决中文路径写入失败的问题。
        - 为非`np.uint8`的图片转换格式。
    - `cv0.VideoCapGen(source, size: tuple = None)`
        - `cv2.VideoCapture`的包装
        - 一个生成器
        - 在读取失败时不返回`None`，而是`raise`
    - 绘图函数，包括: 
        - `cv0.circle(img, center, radius, color, thickness=1, lineType=16)` 
        - `cv0.putText(img, text, org, fontFace, fontScale, color, thickness=1, lineType=16, bottomLeftOrigin=False)`
        - 替代原本的同名函数。
        - 位置参数(如`center`)不再受限于`tuple`类型，内部元素也可以是`float`。
        - 默认使用带抗锯齿的`lineType`。

+ matrix
    - 齐次座标系的常用变换矩阵
    - `matrix.scale(x, y, z)`
        - 缩放矩阵
    - `matrix.rotate_ax(r, axis: tuple)`
        - 绕座标轴旋转矩阵
    - `matrix.rotate(angle, v)`
        - 旋转矩阵
    - `matrix.translate(x, y, z)`
        - 平移矩阵
    - `matrix.perspective(view_distance)`
        - 透视矩阵


+ 计时
    - 使用上下文管理器的计时器
    - `with 计时.计时(名字):`
        - 计算with块中的代码执行用时并print
    - `with 计时.帧率计(名字):`
        - 计算with块中的代码帧率
        - 在累积时长每到达3秒时会print一次


## 使用方法

莉沫工具箱可以直接通过pip安装，只要——

```bash
pip install git+https://github.com/RimoChan/rimo_utils.git
```

然后`from rimo_utils import 什么`就行了。

有一些注意事项: 

+ 如果你想升级莉沫工具箱，在`pip -U`的时候遇到了错误，这可能是因为你的pip版本太旧了。

+ pip并不会帮你装上requirements。因为这个仓库涉及很多领域，它的依赖非常多，所以你应该在遇到缺依赖的时候再用pip手动安装。


话说真的有人用吗……

