import texDef

class RandomGen:
    def __init__(self):
        self.tex_text = ''

    def random_gen(self):
        class_names = [name for name in dir(texDef) if isinstance(getattr(texDef, name), type)]
        objects = [getattr(texDef, name)() for name in class_names]
        for obj in objects:
            self.tex_text += obj.gen_something() + '\n'
        return self.tex_text


if __name__ == '__main__':
    random_gen = RandomGen()

