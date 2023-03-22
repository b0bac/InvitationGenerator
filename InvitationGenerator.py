# 基于Tkinter 绘制界面版本的邀请函（海报）生成器
import tkinter
from PIL import Image
from tkinter import Tk
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import messagebox


class GUIGenerator:
    def __init__(self):
        """图形化界面变量初始化"""
        self.generator = Tk()
        self.generator.title("邀请函生成器V1.0")
        self.generator.geometry("500x400")
        self.source_image_path_label = tkinter.Label(self.generator, text="原始图片文件：")
        self.source_image_path_input = tkinter.Entry(self.generator, width=47)
        self.invitee_name_list_file_label = tkinter.Label(self.generator, text="被邀请人名称列表文件：")
        self.invitee_name_list_file_input = tkinter.Entry(self.generator, width=47)
        self.invitation_card_save_path_label = tkinter.Label(self.generator, text="邀请函图片保存路径：")
        self.invitation_card_save_path_input = tkinter.Entry(self.generator, width=47)
        self.font_config_label = tkinter.Label(self.generator, text="字体颜色和大小，颜色RGB值域 (0-255)：")
        self.font_color_r_label = tkinter.Label(self.generator, text="R值：")
        self.font_color_r_input = tkinter.Entry(self.generator, width=5)
        self.font_color_g_label = tkinter.Label(self.generator, text="G值：")
        self.font_color_g_input = tkinter.Entry(self.generator, width=5)
        self.font_color_b_label = tkinter.Label(self.generator, text="B值：")
        self.font_color_b_input = tkinter.Entry(self.generator, width=5)
        self.font_size_label = tkinter.Label(self.generator, text="字体大小：")
        self.font_size_input = tkinter.Entry(self.generator, width=5)
        self.font_type_file_path_label = tkinter.Label(self.generator, text="字体文件路径：")
        self.font_type_file_path_input = tkinter.Entry(self.generator, width=47)
        self.word_position_label = tkinter.Label(self.generator, text="文字位置：")
        self.word_position_x_label = tkinter.Label(self.generator, text="横坐标：")
        self.word_position_x_input = tkinter.Entry(self.generator, width=5)
        self.word_position_y_label = tkinter.Label(self.generator, text="纵坐标：")
        self.word_position_y_input = tkinter.Entry(self.generator, width=5)
        self.generate_button = tkinter.Button(self.generator, height=1, width=10, text="开始生成", command=self.generate)
        self.copyright_label = tkinter.Label(self.generator, text="作者：b0b@c 一个不误正业的安全从业人员 联系：crsecscu@gmail.com")
        """内部变量初始化"""
        self.messagebox = messagebox
        self.image_file = None
        self.name_list = []
        self.font = None
        self.color = (0, 0, 0)
        self.position = {"x": 0, "y": 0}
        self.save_path = None

    def graph(self):
        self.source_image_path_label.place(x=30, y=20)
        self.source_image_path_input.place(x=30, y=50)
        self.invitee_name_list_file_label.place(x=30, y=80)
        self.invitee_name_list_file_input.place(x=30, y=110)
        self.invitation_card_save_path_label.place(x=30, y=140)
        self.invitation_card_save_path_input.place(x=30, y=170)
        self.font_config_label.place(x=30, y=200)
        self.font_color_r_label.place(x=30, y=230)
        self.font_color_r_input.place(x=70, y=230)
        self.font_color_g_label.place(x=130, y=230)
        self.font_color_g_input.place(x=170, y=230)
        self.font_color_b_label.place(x=230, y=230)
        self.font_color_b_input.place(x=270, y=230)
        self.font_size_label.place(x=340, y=230)
        self.font_size_input.place(x=410, y=230)
        self.font_type_file_path_label.place(x=30, y=270)
        self.font_type_file_path_input.place(x=30, y=300)
        self.word_position_label.place(x=30, y=340)
        self.word_position_x_label.place(x=100, y=340)
        self.word_position_x_input.place(x=160, y=340)
        self.word_position_y_label.place(x=220, y=340)
        self.word_position_y_input.place(x=280, y=340)
        self.generate_button.place(x=340, y=340)
        self.copyright_label.place(x=30, y=375)
        self.generator.mainloop()

    def warning(self, title, message):
        self.messagebox.showinfo(title, message)

    def generate_init(self):
        source_image_file_path = self.source_image_path_input.get()
        if source_image_file_path in ["", " ", None] or not isinstance(source_image_file_path, str):
            self.warning("注意", "请正确输入源图片文件路径!")
            return False
        self.image_file = source_image_file_path
        invitee_name_list_file = self.invitee_name_list_file_input.get()
        if invitee_name_list_file in ["", " ", None] or not isinstance(invitee_name_list_file, str):
            self.warning("注意", "请正确输入姓名文件路径!")
            return False
        with open(invitee_name_list_file, 'r') as filereader:
            for name in filereader.readlines():
                name = name.split("\n")[0].split("\r")[0]
                self.name_list.append(name)
        self.name_list = list(set(self.name_list))
        if len(self.name_list) <= 0:
            self.warning("注意", "没有找到需要生成邀请函的姓名!")
            return False
        try:
            r = int(self.font_color_r_input.get())
            g = int(self.font_color_r_input.get())
            b = int(self.font_color_r_input.get())
            if (r > 255 or r < 0) or (r > 255 or r < 0) or (r > 255 or r < 0):
                self.warning("异常", "颜色错误!请检查输入的颜色值是否在0-255范围内，包含0和255!")
                return False
            self.color = (r, g, b)
        except Exception as reason:
            self.warning("异常", str(reason))
            return False
        font_type_file = self.font_type_file_path_input.get()
        if font_type_file in ["", " ", None] or not isinstance(font_type_file, str):
            self.warning("注意", "请正确输入字体文件路径!")
            return False
        font_size = self.font_size_input.get()
        if font_size in ["", " ", None] or not isinstance(font_size, str):
            self.warning("注意", "请正确输入字体大小!")
            return False
        try:
            font_size = int(font_size)
        except Exception as reason:
            self.warning("异常", str(reason))
            return False
        self.font = ImageFont.truetype(font_type_file, font_size)
        try:
            x = int(self.word_position_x_input.get())
            y = int(self.word_position_y_input.get())
            self.position["x"] = x
            self.position["y"] = y
        except Exception as reason:
            self.warning("异常", str(reason))
            return False
        self.save_path = self.invitation_card_save_path_input.get()
        if self.save_path in ["", " ", None] or not isinstance(self.save_path, str):
            self.warning("注意", "请正确输入姓名文件路径!")
            return False
        return True

    def generate(self):
        if not self.generate_init():
            return
        else:
            for name in self.name_list:
                if name in ["", " ", None]:
                    continue
                text_width = self.font.getsize(name)
                try:
                    image_file = Image.open(self.image_file)
                except Exception as reason:
                    self.warning("异常", str(reason))
                    return
                drawer = ImageDraw.Draw(image_file)
                text_coordinate = (
                    int((image_file.size[0] - text_width[0]) / 2 - self.position.get("x")),
                    int(self.position.get("y"))
                )
                drawer.text(text_coordinate, name, self.color, font=self.font)
                image_file.save(self.save_path+str(name)+".jpg", "jpeg", quality=95)


if __name__ == "__main__":
    generator = GUIGenerator()
    generator.graph()
