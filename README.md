# 16x9-to-4x3

将任意比例的图片转换为 4:3，并用原图模糊背景填充空白区域的小工具。

- 支持拖拽单张或多张图片到 `run.bat` / `convert_image.exe`
- 自动计算 4:3 画布尺寸，不会缩小原图
- 使用原图拉伸 + 高斯模糊作为背景，中心保持清晰
- 提供 Python 源码和已打包好的 Windows 可执行文件

## 使用方法（普通用户）

### 方式一：使用打包好的 exe

1. 下载仓库中的 `convert_image.exe`（位于 `dist/` 目录）
2. 将一张或多张图片拖拽到 `convert_image.exe` 上
3. 程序会在每张图片**同目录下**生成一个新文件，例如：
   - `example.jpg` -> `example_4to3_blur.jpg`

> 提示：这是无控制台版本，拖拽时不会弹出黑色窗口，只会在目标目录上生成结果文件。

### 方式二：使用 `run.bat`（可查看处理过程）

1. 确保 `run.bat` 与 `convert_image.exe` 在同一目录
2. 将图片拖拽到 `run.bat` 上
3. 窗口中会显示处理进度和输出路径

## 使用方法（开发者 / 想看源码的用户）

1. 安装 Python 3 和依赖：

   ```bash
   pip install pillow
   ```

2. 直接运行脚本：

   ```bash
   python convert_image.py <image_path>
   ```

   或给出多张图片：

   ```bash
   python convert_image.py img1.jpg img2.png
   ```

## 打包为 exe

本仓库使用 [PyInstaller](https://www.pyinstaller.org/) 打包：

```bash
py -m pip install pyinstaller
py -m PyInstaller --onefile --noconsole convert_image.py
```

生成的可执行文件位于 `dist/convert_image.exe`。
