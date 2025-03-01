import os

import  texDef

class TexFuzz:
    def __init__(self):
        self.character = {}
        self.debugging = {}
        self.file_io = {}
        self.fonts = {}

        self._init_tex_generator()
        pass

    def _init_tex_generator(self):
        self.greek_letters = texDef.GreekLetters()
        self.symbols_of_type_ord = texDef.SymbolsOfTypeOrd()
        self.large_operators = texDef.LargeOperators()

    def genTex(self):
        pass

    def genTexTest(self):
        # text = self.greek_letters.use(1)
        # with open('test/test.tex', 'w') as f:
        #     for item in text:
        #         f.write(item+ '\n')
        #     f.write('\\bye')
        text = self.large_operators.advance_use('i=1', 'b')
        with open('test/test.tex', 'w') as f:
            f.write('\\font\\myfont=cmr12 at 12pt  % 直接设置字体\n')
            f.write(text+ '\n')
            f.write('\\bye')

    def fuzzTex(self):
        os.system('tex test/test.tex')
        pass

if __name__ == '__main__':
    tex_fuzz = TexFuzz()
    tex_fuzz.genTexTest()
    tex_fuzz.fuzzTex()