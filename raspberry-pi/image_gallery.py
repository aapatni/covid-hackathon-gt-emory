import tkinter, glob, os
import PIL
from PIL import ImageTk, Image
from os import listdir


class Gallery:
    def __init__(self):
        # uninitialized variables
        self.img_width = None
        self.img_height = None
        self.pil_image = None
        self.file_list = []
        self.file_counter = 0

        # gets list of files
        self.get_file_list()

        # initialize root
        self.root = tkinter.Tk()
        self.screen_width, self.screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.screen_width, self.screen_height))
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.root.bind("<Button-1>", lambda e: (self.left_click(e)))
        self.root.bind("<Button-2>", lambda e: (self.right_click(e)))

        # initialize canvas
        self.canvas = tkinter.Canvas(self.root, width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        self.canvas.configure(background='black')

        # Initialize first image
        self.init_pil_image()
        self.image_to_draw = ImageTk.PhotoImage(self.pil_image)
        self.image_on_canvas = self.canvas.create_image(self.screen_width / 2, self.screen_height / 2, image=self.image_to_draw)

        # start main loop
        self.root.mainloop()

    def get_file_list(self):
        path_to_videos = "videos/"
        filenames = listdir(path_to_videos)
        self.file_list = [path_to_videos + filename for filename in filenames]
        self.file_list.sort(key=lambda x: os.path.getmtime(x))

    def init_pil_image(self):
        bad_image = True
        while bad_image:
            try:
                self.pil_image = Image.open(self.file_list[self.file_counter % len(self.file_list)])
                bad_image = False
            except PIL.UnidentifiedImageError:
                self.file_list.pop(self.file_counter % len(self.file_list))

        self.set_image_size()

    def set_image_size(self):
        self.img_width, self.img_height = self.pil_image.size
        # if self.img_width > self.screen_width or self.img_height > self.screen_height:
        ratio = min(self.screen_width / self.img_width, self.screen_height / self.img_height)
        self.img_width = int(self.img_width * ratio)
        self.img_height = int(self.img_height * ratio)
        self.pil_image = self.pil_image.resize((self.img_width, self.img_height), Image.ANTIALIAS)

    def redraw_pil(self):
        self.image_to_draw = ImageTk.PhotoImage(self.pil_image)
        self.canvas.itemconfig(self.image_on_canvas, image=self.image_to_draw)

    def left_click(self, event):
        self.file_counter += 1
        self.init_pil_image()
        self.redraw_pil()

    def right_click(self, event):
        self.file_counter -= 1
        self.init_pil_image()
        self.redraw_pil()


a = Gallery()
