import os
import fuzzGen

class TexFuzz:
    def __init__(self):
        self.character = {}
        self.debugging = {}
        self.file_io = {}
        self.fonts = {}

    def genTex(self):
        pass

    def genTexTest(self):
        random_gen = fuzzGen.RandomGen()
        with open('test/test.tex', 'w') as f:
            f.write('\\font\\myfont=cmr12 at 12pt \n')
            f.write(random_gen.random_gen())
            f.write('\\bye')

    def fuzzTex(self):
        os.system('cd test && tex test.tex')
        pass

if __name__ == '__main__':
    tex_fuzz = TexFuzz()
    tex_fuzz.genTexTest()
    tex_fuzz.fuzzTex()