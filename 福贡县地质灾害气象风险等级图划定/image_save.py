from PIL import Image
import os


def save_image_to_directory(input_path, output_dir, output_filename):
    """
    读取图片并保存到指定目录

    :param input_path: 输入图片路径
    :param output_dir: 输出目录
    :param output_filename: 输出文件名（带扩展名，如 "output.jpg"）
    """
    # 确保输出目录存在，如果不存在则创建
    os.makedirs(output_dir, exist_ok=True)

    # 打开图片文件
    with Image.open(input_path) as img:
        # 构造输出路径
        output_path = os.path.join(output_dir, output_filename)

        # 保存图片
        img.save(output_path)
        print(f"图片已成功保存至: {output_path}")
