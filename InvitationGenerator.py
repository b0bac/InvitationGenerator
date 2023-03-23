# 基于Tkinter 绘制界面版本的邀请函（海报）生成器
import tkinter
from PIL import Image
from tkinter import Tk
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, askdirectory


class GUIGenerator:
    def __init__(self):
        """内部变量初始化"""
        self.messagebox = messagebox
        self.image_file = None
        self.name_list = []
        self.font = None
        self.color = None
        self.position = {"x": 0, "y": 0}
        self.save_path = None
        """图形化界面变量初始化"""
        self.generator = Tk()
        self.generator.title("邀请函生成器V1.1")
        self.generator.geometry("500x400")
        self.source_image_path_label = tkinter.Label(self.generator, text="原始图片文件：")
        self.source_image_path_input = tkinter.Entry(self.generator, width=40)
        self.source_image_file_select_button = tkinter.Button(
            self.generator,
            height=1,
            width=3,
            text="选择",
            command=self.source_image_file_select_function
        )
        self.invitee_name_list_file_label = tkinter.Label(self.generator, text="被邀请人名称列表文件：")
        self.invitee_name_list_file_input = tkinter.Entry(self.generator, width=40)
        self.invitee_name_list_file_select_button = tkinter.Button(
            self.generator,
            height=1,
            width=3,
            text="选择",
            command=self.invitee_name_list_file_select_function
        )
        self.invitation_card_save_path_label = tkinter.Label(self.generator, text="邀请函图片保存路径：")
        self.invitation_card_save_path_input = tkinter.Entry(self.generator, width=40)
        self.invitation_card_save_path_select_button = tkinter.Button(
            self.generator,
            height=1,
            width=3,
            text="选择",
            command=self.invitation_card_save_path_select_function
        )
        self.font_config_label = tkinter.Label(self.generator, text="字体属性：")
        self.font_color_select_label = tkinter.Label(self.generator, text="字体颜色：")
        self.font_color_select_input = tkinter.Entry(self.generator, width=10, bg="white")
        self.font_color_select_button = tkinter.Button(
            self.generator,
            height=1,
            width=5,
            text="颜色选择",
            command=self.font_color_select_function
        )
        self.font_size_label = tkinter.Label(self.generator, text="字体大小：")
        self.font_size_input = tkinter.Entry(self.generator, width=8)
        self.font_type_file_path_label = tkinter.Label(self.generator, text="字体文件路径：")
        self.font_type_file_path_input = tkinter.Entry(self.generator, width=40)
        self.font_type_file_select_button = tkinter.Button(
            self.generator,
            height=1,
            width=3,
            text="选择",
            command=self.font_type_file_select_function
        )
        self.word_position_label = tkinter.Label(self.generator, text="文字位置：")
        self.word_position_x_label = tkinter.Label(self.generator, text="横坐标：")
        self.word_position_x_input = tkinter.Entry(self.generator, width=5)
        self.word_position_y_label = tkinter.Label(self.generator, text="纵坐标：")
        self.word_position_y_input = tkinter.Entry(self.generator, width=5)
        self.generate_button = tkinter.Button(self.generator, height=1, width=10, text="开始生成", command=self.generate)
        self.copyright_label = tkinter.Label(self.generator, text="作者：b0b@c 一个不误正业的安全从业人员 联系：crsecscu@gmail.com")

    def source_image_file_select_function(self):
        selected_file_path = askopenfilename(
            parent=self.generator,
            title="原始图片选择",
            initialdir="~/"
        )
        self.source_image_path_input.insert("end", selected_file_path)

    def invitee_name_list_file_select_function(self):
        selected_file_path = askopenfilename(
            parent=self.generator,
            title="受邀嘉宾姓名文件选择",
            initialdir="~/"
        )
        self.invitee_name_list_file_input.insert("end", selected_file_path)

    def invitation_card_save_path_select_function(self):
        selected_path = askdirectory(
            parent=self.generator,
            title="邀请函存储路径选择",
            initialdir="~/"
        )
        self.invitation_card_save_path_input.insert("end", selected_path)

    def font_type_file_select_function(self):
        selected_file_path = askopenfilename(
            parent=self.generator,
            title="字体类型文件选择",
            initialdir="~/"
        )
        self.font_type_file_path_input.insert("end", selected_file_path)

    def font_color_select_function(self):
        color = colorchooser.askcolor(
            parent=self.generator,
            title="字体颜色选择"
        )
        self.font_color_select_input.config(bg=str(color[1]))
        self.font_color_select_input.place(x=100, y=230)
        self.color = str(color[1])

    def graph(self):
        self.source_image_path_label.place(x=30, y=20)
        self.source_image_path_input.place(x=30, y=50)
        self.source_image_file_select_button.place(x=401, y=47)
        self.invitee_name_list_file_label.place(x=30, y=80)
        self.invitee_name_list_file_input.place(x=30, y=110)
        self.invitee_name_list_file_select_button.place(x=401, y=107)
        self.invitation_card_save_path_label.place(x=30, y=140)
        self.invitation_card_save_path_input.place(x=30, y=170)
        self.invitation_card_save_path_select_button.place(x=401, y=167)
        self.font_config_label.place(x=30, y=200)
        self.font_color_select_label.place(x=30, y=230)
        self.font_color_select_input.place(x=100, y=230)
        self.font_color_select_button.place(x=215, y=227)
        self.font_size_label.place(x=310, y=230)
        self.font_size_input.place(x=380, y=230)
        self.font_type_file_path_label.place(x=30, y=270)
        self.font_type_file_path_input.place(x=30, y=300)
        self.font_type_file_select_button.place(x=401, y=297)
        self.word_position_label.place(x=30, y=340)
        self.word_position_x_label.place(x=100, y=340)
        self.word_position_x_input.place(x=160, y=340)
        self.word_position_y_label.place(x=220, y=340)
        self.word_position_y_input.place(x=280, y=340)
        self.generate_button.place(x=340, y=337)
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
        if self.color is None:
            self.warning("注意", "没有设置颜色")
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
                image_file.save(self.save_path + "/" + str(name) + ".jpg", "jpeg", quality=95)


if __name__ == "__main__":
    generator = GUIGenerator()
    generator.graph()
