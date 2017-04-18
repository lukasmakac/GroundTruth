class Image():

    def __init__(self, name, height, width, img_format='png', db=None):
        self.name = name
        self.height = height
        self.width = width
        self.format = img_format
        self.db = db

