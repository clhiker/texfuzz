import random
import random_input

class MathLatter(object):
    def use(self, num=1):
        pass
    def gen_something(self):
        return ""

class GreekLetters(MathLatter):
    def __init__(self):

        # 希腊字母，表示特定的数学或科学符号

        self.letters = [
            '\\alpha', '\\iota', '\\varrho', '\\beta', '\\kappa', '\\sigma',
            '\\gamma', '\\lambda', '\\varsigma', '\\delta', '\\mu', '\\tau',
            '\\epsilon', '\\nu', '\\upsilon', '\\varepsilon', '\\xi', '\\phi',
            '\\zeta', '\\o', '\\varphi', '\\eta', '\\pi', '\\chi',
            '\\theta', '\\varpi', '\\psi', '\\vartheta', '\\rho', '\\omega',
            '\\Gamma', '\\Xi', '\\Phi', '\\Delta', '\\Pi', '\\Psi',
            '\\Theta', '\\Sigma', '\\Omega', '\\Lambda', '\\Upsilon'
        ]         # len -> 41

    def use(self, nums=1):
        if nums > len(self.letters):
            return ''
        text_list = [item for item in random.sample(self.letters, nums)]
        return ' '.join(text_list)

    def useOne(self):
        return random.choice(list(self.letters))

    def gen_something(self):
        return "$\n" + self.use(3) +"\n$"

class SymbolsOfTypeOrd(MathLatter):
    def __init__(self):

        # 这些符号在数学模式中通常用于表示变量、常量或其他普通数学对象，而不是操作符、关系符号或其他特殊符号。

        self.symbols = [
            '\\aleph', '\\prime', '\\forall', '\\hbar', '\\emptyset', '\\exists',
            '\\imath', '\\nabla', '\\neg', '\\lnot', '\\jmath', '\\surd', '\\flat',
            '\\ell', '\\top', '\\natural', '\\wp', '\\bot', '\\sharp',
            '\\Re', '\\clubsuit', '\\Im', '\\angle', '\\diamondsuit', '\\partial',
            '\\triangle', '\\heartsuit', '\\infty', '\\backslash', '\\spadesuit'
        ]

    def use(self, nums=1):
        if nums > len(self.symbols):
            return ''
        text_list = [item for item in random.sample(self.symbols, nums)]
        return ' '.join(text_list)

    def gen_something(self):
        return "$\n" + self.use(3) +"\n$"

class LargeOperators(MathLatter):
    def __init__(self):
        self.operators = [
            '\\sum', '\\bigcap', '\\bigodot', '\\prod', '\\bigcup', '\\bigotimes',
            '\\coprod', '\\bigsqcup', '\\bigoplus', '\\int', '\\bigvee', '\\biguplus',
            '\\oint', '\\bigwedge'
        ]

    def advance_use(self, _1, _2, nums):
        op_tex = ''
        for i in range(nums):
            op_tex += "%s_{%s}^{%s}" % (random.choice(self.operators), _1, _2)+ '\n'
        return op_tex

    def gen_something(self):
        return "$\n"+ self.advance_use('x', 'y', 3) +"$"


class BinaryOperations(MathLatter):
    def __init__(self):
        self.operations = ['\\pm', '\\cap', '\\vee', '\\lor', '\\mp',
                           '\\cup', '\\wedge', '\\land', '\\setminus', '\\uplus',
                           '\\oplus', '\\cdot', '\\sqcap', '\\ominus', '\\times',
                           '\\sqcup', '\\otimes', '\\ast', '\\triangleleft', '\\oslash',
                           '\\star', '\\triangleright', '\\odot', '\\diamond', '\\wr',
                           '\\dagger', '\\circ', '\\bigcirc', '\\ddagger', '\\bullet',
                           '\\bigtriangleup', '\\amalg', '\\div', '\\bigtriangledown'
                           ]

    def advance_use(self, _1, _2, nums):
        op_tex = ''
        for i in range(nums):
            op_tex += "%s %s %s" % (_1, random.choice(self.operations), _2) + '\n'
        return op_tex

    def gen_something(self):
        return "$\n" + self.advance_use('A', 'B', 3) + "$"


class PageLayout:
    def __init__(self):
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.layout = ['\\hsize', '\\vsize', '\\displaywidth', '\\hoffset', '\\voffset']

    def use_one(self, dimen):
        lo = random.choice(list(self.layout))
        return "%s=%s" % (lo, dimen)

    def use(self, nums=1):
        tex_text = ''
        for i in range(nums):
            tex_text += self.use_one(self.dimen_space.gen_any_stand_dimen()) + '\n'
        return tex_text

    def gen_something(self):
        return "$\n" + self.use(3) + "$"

class Relations(MathLatter):
    def __init__(self):
        self.relations = [
            "\\leq", "\\le", "\\geq", "\\ge", "\\equiv", "\\prec",
            "\\succ", "\\sim", "\\preceq", "\\succeq", "\\simeq", "\\ll",
            "\\gg", "\\asymp", "\\subset", "\\supset", "\\approx", "\\subseteq",
            "\\supseteq", "\\cong", "\\sqsubseteq", "\\sqsupseteq", "\\bowtie", "\\in",
            "\\notin", "\\ni", "\\owns", "\\vdash", "\\dashv", "\\models",
            "\\smile", "\\mid", "\\doteq", "\\frown", "\\parallel", "\\perp",
            "\\propto", "\\not\\equiv", "\\notin", "\\ni", "\\owns", "\\vdash", "\\dashv",
            "\\models", "\\smile", "\\mid", "\\doteq", "\\frown", "\\parallel", "\\perp",
             "\\propto", "\\notequiv", "\\notin", "\\ne"
        ]
        ## \not 否定的用法？

    def use(self, nums=1):
        if nums > len(self.relations):
            return ''
        text_list = [item for item in random.sample(self.relations, nums)]
        return ' '.join(text_list)

    def useOne(self):
        return random.choice(list(self.relations))

    def gen_something(self):
        return "$\n" + self.use(3) + "\n$"

class Arrows(MathLatter):
    def __init__(self):
        self.arrows = [
            "\\leftarrow", "\\Leftarrow", "\\rightarrow", "\\Rightarrow", "\\leftrightarrow", "\\Leftrightarrow",
            "\\mapsto", "\\hookleftarrow", "\\leftharpoonup", "\\leftharpoondown", "\\rightleftharpoons", "\\longleftarrow",
            "\\Longleftarrow", "\\longrightarrow", "\\Longrightarrow", "\\longleftrightarrow", "\\Longleftrightarrow", "\\longmapsto",
            "\\hookrightarrow", "\\rightharpoonup", "\\rightharpoondown", "\\uparrow", "\\Uparrow", "\\downarrow",
            "\\Downarrow", "\\updownarrow", "\\Updownarrow", "\\nearrow", "\\searrow", "\\swarrow",
            "\\nwarrow"
        ]
    def use(self, nums=1):
        if nums > len(self.arrows):
            return ''
        text_list = [item for item in random.sample(self.arrows, nums)]
        return ' '.join(text_list)

    def useOne(self):
        return random.choice(list(self.arrows))

    def gen_something(self):
        return "$\n" + self.use(3) + "\n$"




class Delimiters:
    def __init__(self):
        self.form1 = [
           "\\lbrack", "\\lbrace",  "\\rbrack", "\\rbrace", "\\vert",
            "\\lceil",  "\\rceil", "\\lfloor", "\\rfloor"
        ]

    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def gen_something(self):
        tex_text = '$\n'
        tex_text += self.use_form1() + '\n'
        return tex_text + '$'


class EveryTimeInsertions:
    def __init__(self):
        self.any_text = random_input.AnyText()
        self.every = ['\\everypar', '\\everymath', '\\everydisplay', '\\everycr']

    def use_one(self, text):
        lo = random.choice(list(self.every))
        return "%s{%s}" % (lo, text)

    def use(self, nums=1):
        tex_text = ''
        for i in range(nums):
            tex_text += self.use_one(self.any_text.rec_string()) + '\n'
        return tex_text

    def gen_something(self):
        return self.use(3)


class Accents:
    def __init__(self):
        self.any_text = random_input.AnyText()
        self.accents = [
             "\\hat", "\\widehat", "\\tilde", "\\widetilde",  "\\check",  "\\acute",  "\\grave",
             "\\dot", "\\ddot",  "\\breve",  "\\bar",  "\\vec"
        ] # 可以嵌套使用

    def use_one(self, text):
        arr = random.choice(list(self.accents))
        return "%s{%s}" % (arr, text)

    def use(self, nums=1):
        tex_text = ''
        for i in range(nums):
            tex_text += self.use_one(self.any_text.rec_string()) + '\n'
        return tex_text

    def gen_something(self):
        return "$\n" + self.use(3) + "$"


class ElementaryMathControlSequences:
    def __init__(self):
        self.any_text = random_input.AnyText()
        self.control_sequences = [
            '\\root', '\\over', '\\atop', '\\choose', '\\brace', '\\brack',
            '\\displaystyle', '\\textstyle', '\\scriptstyle', '\\scriptscriptstyle'
        ]

        self.form_1 = [
             "\\overline",  "\\underline",  "\\sqrt"
        ]
        self.form_2 = [
             "\\root",
             "\\of"
        ]
        self.form_3 = [
            "\\over",
            "\\atop",
            "\\choose",
            "\\brace",
            "\\brack"
        ]

    def use_form1(self, text):
        case = random.choice(self.form_1)
        case1 = "%s{%s}" % (case, text)
        return case1

    def use_form2(self, text1, text2):
        case1 = "%s %s %s{%s}" % (self.form_2[0], text1, self.form_2[1], text2)
        case2 = "%s %s%s{%s}" % (self.form_2[0], text1, self.form_2[1], text2)
        return random.choice([case1, case2])

    def use_form3(self, text1, text2):
        case = random.choice(self.form_3)
        case1 = "{%s %s %s}" % (text1, case, text2)
        return case1

    def gen_something(self):
        tex_text = '$\n'
        tex_text += self.use_form1(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form2(self.any_text.simple_string(), self.any_text.simple_string()) + '\n'
        tex_text += self.use_form3(self.any_text.simple_string(), self.any_text.simple_string()) + '\n'
        return tex_text + '$'


#包含复杂嵌套情况，后面再修改
class NonItalicFunctionNames:
    def __init__(self):
        self.form1 = ['\\arccos', '\\cos', '\\csc', '\\exp', '\\ker',
                         '\\sinh', '\\arcsin', '\\cosh',
                          '\\lg', '\\ln', '\\arctan', '\\cot',
                          '\\log', '\\sec', '\\tan', '\\arg', '\\coth', '\\sin',
                          '\\tanh' ,'\\pmod'
                          ]
        self.form2 = ["\\limsup" , "\\lim" , "\\liminf"
                      ]
        self.form3 = ["\\min" , "\\gcd" , "\\hom" , '\\max'
                      ]
        self.form4 = ["\\Pr"
                      ]
        self.form5 = ["\\det" , "deg"
                      ]
        self.form6 = ["\\dim"
                      ]
        self.form7 = ["\\bmod"
                      ]
        self.form8 = ["\\mathop"
                      ]

        self.form9 = [ '\\sup',  '\\inf',
                      ]

        self.any_text = random_input.AnyText()


    def use_form1(self, text):
        case = random.choice(self.form1)
        case1 = "%s{%s}" % (case, text)
        return case1

    def use_form2(self, text):
        case = random.choice(self.form2)
        case2 = "x \to a"
        case1 = "%s_{%s}%s" % (case, case2,text)
        return case1

    def use_form3(self, text1 ,text2):
        case = random.choice(self.form3)
        case1 = "%s(%s,%s)" % (case, text1, text2)
        return case1

    def use_form4(self, text):
        case = random.choice(self.form4)
        case1 = "%s(%s)" % (case, text)
        return case1

    def use_form5(self, text):
        case = random.choice(self.form5)
        case1 = "%s %s" % (case, text)
        return case1

    def use_form6(self, text):
        case = random.choice(self.form6)
        case1 = "%s %s" % (case, text)
        return case1

    def use_form7(self, text):
        case = random.choice(self.form7)
        case1 = "%s %s %s" % (text,case, text)
        return case1

    def use_form8(self, text):
        case = random.choice(self.form8)
        case1 = "%s{%s}" % (case, text)
        return case1

    def use_form9(self):
        case = random.choice(self.form9)
        case1 = "%s" % (case)
        return case1




    def gen_something(self):
        tex_text = '$\n'
        tex_text += self.use_form1(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form2(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form3(self.any_text.simple_string(), self.any_text.simple_string()) + '\n'
        tex_text += self.use_form4(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form5(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form6(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form7(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form8(self.any_text.simple_string()) + '\n'
        tex_text += self.use_form9() + '\n'
        return tex_text + '$'


class FootnotesInsertionsAndUnderlines:
    def __init__(self):
        self.text = random_input.AnyText()
        self.footnote = ['\\footnote']
        self.insert_begin = ['\\topinsert', '\\pageinsert', '\\midinsert']
        self.insert_end = ['\\endinsert']
        self.underbar = ['\\underbar']

    def use_form1(self, text1, text2):
        case1 = "%s %s{%s}" % (self.footnote[0], text1, text2)
        return case1

    def use_form2(self, text):          # vmode material
        case = random.choice(self.insert_begin)
        case1 = "%s %s %s" % (case, text, self.insert_end[0])
        return case1

    def use_form3(self, text):
        case1 = "%s{%s}" % (self.underbar[0], text)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.text.simple_string(), self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.text.simple_string()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        return tex_text


class UsefulParametersAndConversions:
    def __init__(self):
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.days = [i for i in range(1, 32)]
        self.months = [i for i in range(1, 13)]
        self.years = [i for i in range(1900, 2030)]
        self.form1 = ['\\year', '\\month', '\\day']
        self.form2 = ['\\romannumeral']
        self.form3 = ['\\uppercase', '\\lowercase']
        self.form4 = ['\\jobname', ]

    def use_form1(self):
        case = random.choice(self.form1)
        if case == '\\year':
            case1 = "%s=%s" % (case, random.choice(self.years))
        elif case == '\\month':
            case1 = "%s=%s" % (case, random.choice(self.months))
        elif case == '\\day':
            case1 = "%s=%s" % (case, random.choice(self.days))
        else:
            case1 = case
        case2 = "\\the%s" % case
        # case3...
        return random.choice([case1, case2])

    def use_form2(self, number):
        case1 = "%s %s" % (self.form2[0], number)
        case2 = "%s%s" % (self.form2[0], number)
        return random.choice([case1, case2])

    def use_form3(self, text):
        case = random.choice(self.form3)
        case1 = "%s{%s}" % (case , text)
        return case1

    def use_form4(self):
        case1 = "%s" % (self.form4[0])
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.number.uint_number()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        tex_text += self.use_form4() + '\n'
        return tex_text


class FillsLeadersAndEllipses:
    def __init__(self):
        self.text = random_input.AnyText()
        self.box_rule = random_input.AnyBoxRule()
        self.dimen = random_input.DimensionsSpacingAndGlue()

        self.dots = ['\\dots', '\\ldots', '\\ddots', "\\cdots", "\\vdots"]
        self.fills = ['\\hrulefill', '\\rightarrowfill', '\\leftarrowfill', '\\dotfill']
        self.leaders_skip = ['\\leaders', '\\hskip']
        self.leaders_fill = ['\\leaders', '\\hfill']

    def use_form1(self):
        return '$' + random.choice(self.dots) + '$'

    def use_form2(self):
        return random.choice(self.fills)

    def use_form3(self, box, glue):
        case1 = "%s %s %s %s" % (self.leaders_skip[0], box, self.leaders_skip[1], glue)
        return case1

    def use_form4(self, box):
        case1 = "%s %s %s" % (self.leaders_fill[0], box, self.leaders_fill[1])
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2() + '\n'
        tex_text += self.use_form3(self.box_rule.any_box(), self.dimen.gen_any_stand_glue()) + '\n'
        tex_text += self.use_form4(self.box_rule.any_box()) + '\n'
        return tex_text

class TEXFontsAndMagnification:
    def __init__(self):
        self.font_names = [
            # Computer Modern 字体
            "cmr5", "cmr6", "cmr7", "cmr8", "cmr9", "cmr10", "cmr12", "cmr17",
            "cmbx5", "cmbx6", "cmbx7", "cmbx8", "cmbx9", "cmbx10", "cmbx12", "cmbx17",
            "cmti5", "cmti6", "cmti7", "cmti8", "cmti9", "cmti10", "cmti12", "cmti17",
            "cmbxti5", "cmbxti6", "cmbxti7", "cmbxti8", "cmbxti9", "cmbxti10", "cmbxti12", "cmbxti17",
            # "cmss5", "cmss6", "cmss7", "cmss8", "cmss9", "cmss10", "cmss12", "cmss17",
            # "cmtt5", "cmtt6", "cmtt7", "cmtt8", "cmtt9", "cmtt10", "cmtt12", "cmtt17",
            # "cmmi5", "cmmi6", "cmmi7", "cmmi8", "cmmi9", "cmmi10", "cmmi12", "cmmi17",
            # "cmsy5", "cmsy6", "cmsy7", "cmsy8", "cmsy9", "cmsy10", "cmsy12", "cmsy17",
            # "cmex5", "cmex6", "cmex7", "cmex8", "cmex9", "cmex10", "cmex12", "cmex17",
            # Latin Modern 字体
            # "lmr5", "lmr6", "lmr7", "lmr8", "lmr9", "lmr10", "lmr12", "lmr17",
            # "lmbx5", "lmbx6", "lmbx7", "lmbx8", "lmbx9", "lmbx10", "lmbx12", "lmbx17",
            # "lmti5", "lmti6", "lmti7", "lmti8", "lmti9", "lmti10", "lmti12", "lmti17",
            # "lmbxti5", "lmbxti6", "lmbxti7", "lmbxti8", "lmbxti9", "lmbxti10", "lmbxti12", "lmbxti17",
            # "lmtt5", "lmtt6", "lmtt7", "lmtt8", "lmtt9", "lmtt10", "lmtt12", "lmtt17"
        ]
        self.fonts = ["\\rm",  "\\bf",  "\\tt",  "\\sl",  "\\it"]
        self.magnification = ["\\magnification", "\\magstep", "\\magstephalf"]
        self.fontFN = ["\\font\\FN"]
        self.true_dimen = ["true"]
        self.char_symbol = ["\\char"]
        self.number = random_input.AnyNumber()
        self.dimen = random_input.DimensionsSpacingAndGlue()
        self.number2 = random_input.ThousandMultiplierGenerator()

    def use_form1(self):
        return random.choice(self.fonts)

    def use_form2(self, number, number2):
        case1 = "%s=%s" % (self.magnification[0], number2)
        case2 = "%s %s" % (self.magnification[1], number)
        case3 = self.magnification[2]
        return random.choice([case1, case2, case3])

    def use_form3(self, dimen):
        fontname = random.choice(self.font_names)
        case1 = "%s=%s" % (self.fontFN[0], fontname)
        case2 = "%s=%s at %s" % (self.fontFN[0], fontname, dimen)
        case3 = "%s=%s scaled %s" % (self.fontFN[0], fontname, dimen)
        return random.choice([case1, case2, case3])

    def use_form4(self, dimen):
        return "%s %s" % (self.true_dimen[0], dimen)

    def use_form5(self):
        decimal_list = list(range(256))
        octal_list = [oct(i) for i in range(0o377 + 1)]
        hex_list = [hex(i) for i in range(0xFF + 1)]
        case1 = "%s%d" % (self.char_symbol[0], random.choice(decimal_list))
        case2 = "%s'%s" % (self.char_symbol[0], random.choice(octal_list))
        case3 = "%s\"%s" % (self.char_symbol[0], random.choice(hex_list))
        return random.choice([case1, case2, case3])

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.number.uint_number() , self.number2.generate()) + '\n'
        tex_text += self.use_form3(self.dimen.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form4(self.dimen.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form5() + '\n'
        return tex_text




#需要修改。表格
class AlignmentDisplays:
    def __init__(self):
        self.form1 = ["\\settabs", "\\columns"]
        self.form2 = ["\\settabs"]
        self.form3 = ["\\halign"]
        self.form4 = ["\\openup" , "\\tabskip"]
        self.form5 = ["\\noalign"]
        self.noalign = ["\\hrule" , "\\vrule" , "\\vskip 5pt" , "\\hfil Note"]
        self.form6 = ["\\omit"]
        self.form7 = ["\\span"]
        self.form8 = ["\\multispan"]
        self.form9 = ["\\hidewidth"]

        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen = random_input.DimensionsSpacingAndGlue()
        self.settabs = random_input.RandomSettabsGenerator()
        self.halign = random_input.HalignGenerator()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()

    def use_form1(self, number):
        case = "%s %s %s" % (self.form1[0], number, self.form1[1])
        return case

    def use_form2(self, settab):
        case = "%s %s" % (self.form2[0], settab)
        return case

    def use_form3(self, halign):
        case = "%s{%s}" % (self.form3[0], halign)
        return case

    def use_form4(self, dimen):
        case = random.choice(self.form4)
        case = "%s %s" % (case, dimen)
        return case

    def use_form5(self):
        case1 = random.choice(self.noalign)
        case = "\\halign{\n\\hfil#\\hfil & \\hfil#\\hfil\\cr\nHeader1 & Header2 \\cr\n%s {%s}\nData1 & Data2 \\cr}" % (self.form5[0], case1)
        return case

    def use_form6(self):

        case = "\\halign{\n\\hfil#\\hfil & \\hfil#\\hfil\\cr\nHeader1 & Header2 \\cr\n%s\\hfil 自定义内容 \\hfil & 正常内容 \\cr\n}" % (self.form6[0])
        return case

    def use_form7(self):

        case = "\\halign{\n\\hfil#\\hfil & \\hfil#\\hfil & \\hfil#\\hfil\\cr\n %s 跨两列内容 & \\cr\n  A & B & C \\cr\n}" % (self.form7[0])
        return case

    def use_form8(self):

        case = "\\halign{\n\\hfil#\\hfil & \\hfil#\\hfil & \\hfil#\\hfil \\cr\n%s3 跨三列标题 \\cr\nA & B & C \\cr\n}" % (self.form8[0])
        return case

    def use_form9(self):

        case = "\\halign{\n\\hfil#\\hfil & #\\hfil \\cr\n正常列 & %s [紧凑内容] \\cr\n}" % (self.form9[0])
        return case

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.number.uint_number()) + '\n'
        tex_text += self.use_form2(self.settabs.generate()) + '\n'
        tex_text += self.use_form3(self.halign.generate()) + '\n'
        tex_text += self.use_form4(self.dimen_space.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form5() + '\n'
        tex_text += self.use_form6() + '\n'
        tex_text += self.use_form7() + '\n'
        tex_text += self.use_form8() + '\n'
        tex_text += self.use_form9() + '\n'
        return tex_text



class Boxes:
    def __init__(self):
        self.boxes = [
            "\\hbox", "\\vbox", "\\vtop"
        ]
        self.lap = ['\\rlap', '\\llap']
        self.vcenter = ['\\vcenter']
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.text = random_input.AnyText()

    def use_form1(self, dimen, text):
        case = random.choice(self.boxes)
        case1 = f"{case} to {dimen} {{ {text} }}"
        return case1

    def use_form2(self, text):
        case = random.choice(self.lap)
        case1 = f"{case} {{ {text} }} "
        return case1

    def use_form3(self, dimen, text):
        case = random.choice(self.vcenter)
        case1 = f"${case} to {dimen} {{ {text} }}$"
        return case1
    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.dimen_space.gen_any_stand_dimen(),
                                   self.text.simple_string())  + '\n' +"\\box0\n"
        tex_text += self.use_form2(self.text.simple_string()) + '\n'
        return tex_text


class OverfullBoxes:
    def __init__(self):
        self.boxes = [
            "\\hfuzz", "\\vfuzz", "\\overfullrule"
        ]
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
    def use_form1(self, dimen):
        case = random.choice(self.boxes)
        case1 = f"{case}={dimen} "
        return case1
    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.dimen_space.gen_any_stand_dimen()) + '\n'
        return tex_text




class IndentationAndItemizedLists:
    def __init__(self):
        self.form1 = [
            "\\item", "\\itemitem"
        ]
        self.form2 = [
            "\\indent", "\\noindent", "\\narrower"
        ]
        self.form3 = [
            "\\parindent", "\\displayindent", "\\leftskip", "\\rightskip", "\\hangindent",
        ]
        self.form4 = [
            "\\hangafter"
        ]
        self.form5 = [
            "\\parshape"
        ]

        self.text = random_input.AnyText()
        self.text2 = random_input.ParshaperGenerator()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()

    def use_form1(self, text):
        case = random.choice(self.form1)
        case1 = "%s { %s }" % (case, text)
        return case1

    def use_form2(self):
        case = random.choice(self.form2)
        return case

    def use_form3(self, any_dimen):
        case = random.choice(self.form3)
        case1 = "%s = %s" % (case, any_dimen)
        return case1

    def use_form4(self, any_number):
        case1 = "%s = %s" % (self.form4[0], any_number)
        return case1

    def use_form5(self, text2):
        case1 = "%s = %s" % (self.form5[0], text2)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.text.simple_string()) + '\n'
        tex_text += self.use_form2() + '\n'
        tex_text += self.use_form3(self.dimen_space.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form4(self.number.uint_number()) + '\n'
        tex_text += self.use_form4(self.text2.generate_parshape()) + '\n'
        return tex_text


class IndentationAndItemizedLists:
    def __init__(self):
        self.indentation = ["\\indent",  "\\noindent", "\\narrower",  "\\item", "\\itemitem"
        ]
        self.form1 = ["\\indent",  "\\noindent", "\\narrower"]
        self.form2 = ["\\parindent", "\\displayindent",  "\\leftskip", "\\rightskip", '\\hangindent']
        self.form3 = ["\\beginsection", "\\item", "\\itemitem"]
        self.form4 = ["\\hangafter"]
        self.form5 = ["\\par"]
        self.form6 = ["\\parshape"]

        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.text = random_input.AnyText()
        self.numbers = random_input.AnyNumber()
        self.parshap = random_input.ParshaperGenerator()

    def use_form1(self, text):
        case = random.choice(self.indentation)
        case1 = f"{case} {text} "
        return case1
    def use_form2(self, dimen, text):
        case = random.choice(self.form2)
        case1 = f"{case}={dimen} \n {text}"
        return case1
    def use_form3(self, text1, text2, text3):
        case1 = (f"{self.form3[0]} {{{text1}}} \n"
                 + f"{self.form3[1]} {text2}\n"
                 + f"{self.form3[2]} {text3} \n")
        return case1
    def use_form4(self, number):
        case = random.choice(self.form4)
        case1 = f"{case}={number} \n {self.form5[0]}"
        return case1
    def use_form6(self,parshape1):

        case1 = f"{parshape1}"
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.dimen_space.gen_any_stand_dimen(), self.text.simple_string()) + '\n'
        tex_text += self.use_form3(self.text.simple_string(),
                                    self.text.simple_string(),
                                    self.text.simple_string()) + '\n'
        tex_text += self.use_form4(self.numbers.uint_number()) + '\n'
        tex_text += self.use_form6(self.parshap.generate_parshape()) + '\n'
        return tex_text


class HeadersFootersAndPageNumbers:
    def __init__(self):
        self.form1 = [
            "\\nopagenumbers"
        ]
        self.form2 = [
            "\\pageno", "\\folio"
        ]
        self.form3 = [
            "\\footline", "\\headline"
        ]
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()

    def use_form1(self):
        case = random.choice(self.form1)
        return case

    def use_form2(self, any_number):
        case = random.choice(self.form2)
        case1 = "%s = %s" % (case, any_number)
        return case1

    def use_form3(self, text):
        case1 = "%s = %s " % (self.form2[1], text)
        return case1

    def use_form4(self, text):
        case = random.choice(self.form3)
        case1 = "%s = {%s}" % (case, text)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.number.uint_number()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        tex_text += self.use_form4(self.text.simple_string()) + '\n'
        return tex_text




#宏定义。 需要修改
class MacroDefinitions:
    def __init__(self):
        self.form1 = [
            "\\def", "\\gdef", "\\edef", "\\xdef"
        ]
        self.form2 = [
            "\\cs", "\\let"
        ]
        self.form3 = [
            "\\long", "\\outer", "\\global"
        ]
        self.form4 = [
            "\\noexpand"
        ]
        self.form5 = [
            "\\expandafter"
        ]
        self.form6 = [
            "\\futurelet"
        ]
        self.form7 = [
            "\\csname", "\\endcsname"
        ]
        self.form8 = [
            "\\string", "\\"
        ]
        self.form9 = [
            '\\number'
        ]
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.macro= random_input.RandomMacroGenerator()

    def use_form1(self, any_macro):
        case = random.choice(self.form1)
        case1 = "%s %s" % (case, any_macro)
        return case1

    def use_form2(self, text):
        case1 = "%s %s = %s" % (self.form2[1], self.form2[0], text)
        return case1

    def use_form3(self, any_macro):
        case = random.choice(self.form3)
        case1 = "%s %s %s" % (case, self.form1[0], any_macro)
        return case1

    def use_form4(self):
        case1 = "\\def\\foo{Hello, World!}\\par %s\\foo" % (self.form4[0])
        return case1

    def use_form5(self):
        case1 = "\\def\\a{Hello}\\def\\b{\\a}%s\\b\\relax" % (self.form5[0])
        return case1

    def use_form6(self):
        case1 = "\def\\tokenA{这是A}\n\def\\tokenB{这是B}\n\def\\next{}\n  %s\\next\\tokenA\\tokenB" % (self.form6[0])
        return case1

    def use_form7(self, text):
        case1 = "%s %s %s" % (self.form7[0], text, self.form7[1])
        return case1

    def use_form8(self, text):
        case1 = "%s%s%s" % (self.form8[0], self.form8[1], text)
        return case1

    def use_form9(self, any_number):
        case1 = "%s%s" % (self.form9[0], any_number)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.macro.gen_macro()) + '\n'
        tex_text += self.use_form2(self.text.simple_string()) + '\n'
        tex_text += self.use_form3(self.macro.gen_macro()) + '\n'
        tex_text += self.use_form4() + '\n'
        tex_text += self.use_form5() + '\n'
        tex_text += self.use_form6() + '\n'
        tex_text += self.use_form7(self.text.simple_string()) + '\n'
        tex_text += self.use_form8(self.text.simple_string()) + '\n'
        tex_text += self.use_form9(self.number.uint_number()) + '\n'

        return tex_text


class Conditionals:
    def __init__(self):
        self.form1 = [
            "\\if", "\\else", "\\fi"
        ]
        self.form2 = [
            "\\ifnum"
        ]
        self.form3 = [
            "\\ifdim"
        ]
        self.form4 = [
            "\\ifodd", "\\ifeof"
        ]
        self.form5 = [
            "\\ifmmode", "\\iftrue", "\\iffalse"
        ]
        self.form6 = [
            "\\if", "\\ifx"
        ]
        self.form7 = [
            "\\ifdim"
        ]
        self.form8 = [
            "\\ifcase", "\\or", "\\else", "\\fi"
        ]
        self.form9 = [
            "\\loop", "\\if", "\\repeat", "\\fi"
        ]
        self.form10 = [
            "\\newif", "\\ifblob", "\\blobtrue", "\\blobfalse"
        ]
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.rel= random_input.AnyRelation()

    def use_form1(self, text1, text2, text3):
        case1 = "%s %s %s %s %s %s" % (self.form1[0], text1, text2, self.form1[1], text3, self.form1[2])
        return case1

    def use_form2(self, any_number1, any_number2, any_relation):
        case1 = "%s %s %s %s %s" % (self.form2[0], any_number1, any_relation, any_number2, self.form1[2])
        return case1

    def use_form3(self, any_dimen1, any_dimen2, any_relation):
        case1 = "%s %s %s %s %s" % (self.form3[0], any_dimen1, any_relation, any_dimen2, self.form1[2])
        return case1

    def use_form4(self):
        case = random.choice(self.form4)
        any_number = str(random.randint(1, 10))
        case1 = "%s %s %s" % (case, any_number, self.form1[2])
        return case1

    def use_form5(self):
        case = random.choice(self.form5)
        case1 = "%s %s" % (case, self.form1[2])
        return case1

    def use_form6(self, text1, text2):
        case = random.choice(self.form6)
        case1 = "%s %s %s %s" % (case, text1, text2, self.form1[2])
        return case1


    def use_form8(self, any_number, text1, text2, text3):
        case1 = "%s %s %s %s %s %s %s %s" % (
        self.form8[0], any_number, text1, self.form8[1], text2, self.form8[2], text3, self.form8[3])
        return case1

    def use_form9(self, text1, text2):
        case1 = "%s %s %s %s %s" % (self.form9[0], text1, self.form9[1], text2, self.form9[2])
        return case1

    def use_form10(self):
        case = random.choice((self.form10[2], self.form10[3]))
        case1 = "%s%s %s " % (self.form10[0], self.form10[1], case)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form10() + '\n'
        tex_text += self.use_form1(self.text.simple_string(), self.text.simple_string(),
                                   self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.number.uint_number(), self.number.uint_number(),
                                   self.rel.generate_random_relation()) + '\n'
        tex_text += self.use_form3(self.dimen_space.gen_any_stand_dimen(), self.dimen_space.gen_any_stand_dimen(),
                                   self.rel.generate_random_relation()) + '\n'
        tex_text += self.use_form4() + '\n'
        tex_text += self.use_form5() + '\n'
        tex_text += self.use_form6(self.text.simple_string(), self.text.simple_string()) + '\n'

        tex_text += self.use_form8(self.number.uint_number(), self.text.simple_string(), self.text.simple_string(),
                                   self.text.simple_string()) + '\n'
        tex_text += self.use_form9(self.text.simple_string(), self.text.simple_string()) + '\n'
        # tex_text += self.use_form10() + '\n'


        return tex_text



class HorizontalSpacing:
    def __init__(self):
        self.form1 = [
            "\\quad", "\\qquad", "\\thinspace", "\\enspace", "\\enskip",
            "\\hfill", "\\hfill", "\\hfilneg",
             "\\>", "\\;", "\\!", "\\,", "\\negthinspace"
        ]
        self.form2 = [
             "\\mskip"
        ]
        self.form3 = [
            "\\hskip"
        ]

        self.leng = random_input.RandomTexLength2()
        self.leng1 = random_input.RandomTexLength()


    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def use_form2(self, any_length):
        case = random.choice(self.form2)
        case1 = "%s %s" % (case, any_length)
        return case1

    def use_form3(self, any_length):
        case = random.choice(self.form3)
        case1 = "%s %s" % (case, any_length)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.leng.gen_length()) + '\n'
        tex_text += self.use_form3(self.leng1.gen_length()) + '\n'

        return "$\n"+ tex_text +"$"


class VerticalSpacing:
    def __init__(self):
        self.form1 = [
            "\\vfill", "\\vfil", "\\strut"
        ]
        self.form2 = [
            "\\vskip"
        ]
        self.form3 = [
            "\\phantom", "\\vphantom", "\\hphantom", "\\smash"
        ]
        self.form4 = [
            "\\moveleft", "\\moveright", "\\hbox", "\\vbox"
        ]
        self.form5 = [
            "\\raise", "\\lower", "\\leavevmode"
        ]
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.leng = random_input.RandomTexLength()

    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def use_form2(self, any_length):
        case = random.choice(self.form2)
        case1 = "%s %s" % (case, any_length)
        return case1

    def use_form3(self, text):
        case = random.choice(self.form3)
        case1 = "%s {%s}" % (case, text)
        return case1

    def use_form4(self, any_dimen, text):
        case1 = random.choice((self.form4[0], self.form4[1]))
        case2 = random.choice((self.form4[2], self.form4[3]))
        case3 = "%s %s %s {%s}" % (case1, any_dimen, case2, text)
        return case3

    def use_form5(self, any_dimen, text):
        case1 = random.choice((self.form5[0], self.form5[1]))
        case2 = random.choice((self.form4[2], self.form4[3]))
        case3 = "%s %s %s %s {%s}" % (self.form5[2], case1, any_dimen, case2, text)
        return case3


    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.leng.gen_length()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        tex_text += self.use_form4(self.dimen_space.gen_any_stand_dimen(), self.text.simple_string()) + '\n'
        tex_text += self.use_form5(self.dimen_space.gen_any_stand_dimen(), self.text.simple_string()) + '\n'

        return tex_text

class SkipSpaceBetweenLines:
    def __init__(self):
        self.form1 = [
            "\\smallskip", "\\medskip", "\\bigskip",
            "\\smallbreak", "\\medbreak", "\\bigbreak",
            "\\filbreak"
        ]

    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'

        return tex_text


class SetLineSpacing:
    def __init__(self):
        self.form1 = [
            "\\baselineskip", "\\jot"
        ]
        self.form2 = [
            "\\openup"
        ]
        self.text = random_input.AnyText()
        self.number = random_input.AnyNumber()
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.leng = random_input.RandomTexLength()



    def use_form1(self, any_length):
        case = random.choice(self.form1)
        case1 = "%s = %s" % (case, any_length)
        return case1

    def use_form2(self, any_length):
        case1 = "%s %s" % (self.form2[0], any_length)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.leng.gen_length()) + '\n'
        tex_text += self.use_form2(self.leng.gen_length()) + '\n'

        return tex_text


class AllowUnjustifiedLines:
    def __init__(self):
        self.form1 = [
            "\\raggedright", "\\raggedbottom"
        ]

    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'

        return tex_text

class BracesAndMatrices:
    def __init__(self):
        self.form1 = [
            "\\matrix"
        ]
        self.form2 = [
            "\\pmatrix"
        ]
        self.form3 = [
            "\\bordermatrix"
        ]
        self.form4 = [
            "\\overbrace"
        ]
        self.form5 = [
            "\\underbrace"
        ]
        self.text = random_input.AnyText()
        self.generatorm = random_input.RandomMatrixGenerator()
        self.generatorpm = random_input.RandomMatrixGenerator1()
        self.generatorpb = random_input.RandomMatrixGenerator2()


    def use_form1(self, any_matrix):
        case1 = "%s {%s}" % (self.form1[0], any_matrix)
        return case1

    def use_form2(self, any_matrix):
        case1 = "%s {%s}" % (self.form2[0], any_matrix)
        return case1

    def use_form3(self, any_matrix):
        case1 = "%s {%s}" % (self.form3[0], any_matrix)
        return case1

    def use_form4(self, text):
        case1 = "%s {%s}" % (self.form4[0], text)
        return case1

    def use_form5(self, text1, text2):
        case1 = "%s {%s}_{%s}" % (self.form5[0], text1, text2)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.generatorm.gen_tex_code()) + '\n'
        tex_text += self.use_form2(self.generatorpm.generate_matrix()) + '\n'
        tex_text += self.use_form3(self.generatorpb.generate_matrix2()) + '\n'
        tex_text += self.use_form4(self.text.simple_string()) + '\n'
        tex_text += self.use_form5(self.text.simple_string(), self.text.simple_string()) + '\n'

        return "$\n"+ tex_text +"$"


class DisplayedEquations:
    def __init__(self):
        self.form1 = [
            "\\eqno", "\\leqno"
        ]
        self.form2 = [
            "\\eqalign"
        ]
        self.form3 = [
            "\\eqalignno", "\\leqalignno"
        ]
        self.form4 = [
            "\\displaylines"
        ]
        self.form5 = [
            "\\cases"
        ]

        self.text = random_input.AnyText()
        self.reg = random_input.RandomEquationGenerator()
        self.rmfg = random_input.EqalignGenerator()
        self.afg = random_input.AlignedFormulaGenerator()
        self.rfg = random_input.RandomFormulaGenerator()
        self.piece = random_input.RandomPiecewiseFunctionGenerator()

    def use_form1(self, any_math, text):
        case = random.choice(self.form1)
        case1 = "%s %s %s" % (any_math, case, text)
        return case1

    def use_form2(self, any_formula):
        case1 = "%s {%s}" % (self.form2[0], any_formula)
        return case1

    def use_form3(self, any_formula):
        case = random.choice(self.form3)
        case1 = "%s {%s}" % (case, any_formula)
        return case1

    def use_form4(self, any_formula):
        case1 = "%s {%s}" % (self.form4[0], any_formula)
        return case1

    def use_form5(self, any_piece):
        case1 = "%s {%s}" % (self.form5[0], any_piece)
        return case1


    def gen_something(self):
        tex_text = "\def\\frac#1#2{{#1 \over #2}}\n\def\sqr#1{\sqrt{#1}}\n\def\cos{\mathop{\\rm cos}\\nolimits}\n\def\sin{\mathop{\\rm sin}\\nolimits}\def\log{\mathop{\\rm log}\\nolimits}"
        tex_text += "$$\n" + self.use_form1(self.reg.gen_math(self.reg.generate_equation()), self.text.simple_string()) + "$$\n"
        tex_text += "$$\n" + self.use_form2(self.rmfg.generate_eqalign()) + "$$\n"
        tex_text += "$$\n" + self.use_form3(self.afg.gen_formula1()) + "$$\n"
        tex_text += "$$\n" + self.use_form4(self.rfg.gen_formula_block()) + "$$\n"
        tex_text += "$$\n" + self.use_form5(self.piece.gen_piecewise_function()) + "$$\n"

        return tex_text


if __name__ == '__main__':
    test_alignment_displays = AlignmentDisplays()
    print(test_alignment_displays.gen_something())
