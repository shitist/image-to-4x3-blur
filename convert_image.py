import sys
import os
from PIL import Image, ImageFilter

def process_image(input_path):
    try:
        # 统一成绝对路径，方便跨文件夹拖拽
        input_path = os.path.abspath(input_path)
        if not os.path.exists(input_path):
            print(f"错误: 找不到图片 -> {input_path}")
            return

        # 读取原图并转为 RGB
        orig_img = Image.open(input_path).convert("RGB")
        w, h = orig_img.size
        
        # 计算 4:3 画布尺寸（不缩小原图）
        target_w = w
        target_h = int(w * 3 / 4)
        if target_h < h:
            target_h = h
            target_w = int(h * 4 / 3)

        print("正在生成氛围背景...")
        # 将原图拉伸到 4:3 画布并做高斯模糊作为背景
        bg_layer = orig_img.resize((target_w, target_h))
        bg_layer = bg_layer.filter(ImageFilter.GaussianBlur(radius=60))

        # 将清晰原图居中贴到模糊背景上
        offset = ((target_w - w) // 2, (target_h - h) // 2)
        bg_layer.paste(orig_img, offset)

        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_4to3_blur{ext}"

        # 最高质量保存，尽量减少压缩损失
        bg_layer.save(output_path, quality=100, subsampling=0)
        print(f"--- 处理成功 ---")
        print(f"输出文件: {output_path}")

    except Exception as e:
        print(f"运行出错: {e}")

# 支持拖拽单张或多张图片到 exe / BAT 入口
if __name__ == "__main__":
    if len(sys.argv) > 1:
        paths = sys.argv[1:]
        total = len(paths)
        print(f"共收到 {total} 个文件，开始逐个处理...\n")

        for idx, path in enumerate(paths, start=1):
            print(f"[{idx}/{total}] 开始处理: {path}")
            process_image(path)
    else:
        print("请将一张或多张图片拖拽到 BAT 文件上运行。")
