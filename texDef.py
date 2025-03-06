import random
import random_input

class MathLatter(object):
    def use(self, num=1):
        pass
    def gen_something(self):
        return ""

class GreekLetters(MathLatter):
    def __init__(self):
        '''
        希腊字母，表示特定的数学或科学符号
        '''
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
        '''
        这些符号在数学模式中通常用于表示变量、常量或其他普通数学对象，而不是操作符、关系符号或其他特殊符号。
        '''
        self.symbols = [
            '\\aleph', '\\prime', '\\forall', '\\hbar', '\\emptyset', '\\exists',
            '\\imath', '\\nabla', '\\neg', '\\lnot', '\\surd', '\\flat',
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

# class BinaryOperations(MathLatter):
#     def __init__(self):
#         self.operations = ['\\pm', '\\cap', '\\vee', '\\lor', '\\mp', '\\cup', '\\wedge', '\\land', '\\setminus', '\\uplus', '\\oplus', '\\cdot', '\\sqcap', '\\ominus', '\\times', '\\sqcup', '\\otimes', '\\ast', '\\triangleleft', '\\oslash', '\\star', '\\triangleright', '\\odot', '\\diamond', '\\wr', '\\dagger', '\\circ', '\\bigcirc', '\\ddagger', '\\bullet', '\\bigtriangleup', '\\amalg', '\\div', '\\bigtriangledown']
#
#

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
            "\\propto", "\\not\\equiv", "\\notin", "\\ne"
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

# 这个比较复杂，之后仔细修改
# class Delimiters(MathLatter):
#     def __init__(self):
#         self.delimiters = {
#             "[": "\\lbrack", "{": "\\lbrace", "]": "\\rbrack", "}": "\\rbrace", "|": "\\vert",
#             "⌈": "\\lceil", "⌉": "\\rceil", "⌊": "\\lfloor", "⌋": "\\rfloor"
#         }

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
             "\\hat",  "\\tilde",  "\\check",  "\\acute",  "\\grave",
             "\\dot",  "\\breve",  "\\bar",  "\\vec"
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

# 包含复杂嵌套情况，后面再修改
# class NonItalicFunctionNames:
#     def __init__(self):
#         self.functions = ['\\arccos', '\\cos', '\\csc', '\\exp', '\\ker',
#                           '\\limsup', '\\min', '\\sinh', '\\arcsin', '\\cosh',
#                           '\\deg', '\\gcd', '\\lg', '\\ln', '\\Pr', '\\sup',
#                           '\\arctan', '\\cot', '\\det', '\\hom', '\\lim',
#                           '\\log', '\\sec', '\\tan', '\\arg', '\\coth',
#                           '\\dim', '\\inf', '\\liminf', '\\max', '\\sin',
#                           '\\tanh', '\\pmod', '\\bmod', '\\mathop'
#                           ]

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
        self.days = [i for i in range(1, 32)]
        self.months = [i for i in range(1, 13)]
        self.years = [i for i in range(1900, 2030)]
        self.form1 = ['\\year', '\\month', '\\day', '\\jobname', ]
        self.form2 = ['\\romannumeral']
        self.form3 = ['\\uppercase', '\\lowercase']

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
        return case1

    def use_form2(self, number):
        case1 = "%s %s" % (self.form2[0], number)
        case2 = "%s%s" % (self.form2[0], number)
        return random.choice([case1, case2])

    def use_form3(self, text):
        case = random.choice(self.form3)
        case1 = "%s{%s}" % (case , text)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.number.uint_number()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        return tex_text

# class FillsLeadersAndEllipses:
#     def __init__(self):
#         self.dots = ['\\dots', '\\ldots', '\\ddots', "\\cdots", "\\vdots"]
#         self.fills = ['\\hrulefill', '\\rightarrowfill', '\\leftarrowfill', '\\dotfill']
#         self.leaders_skip = ['\\leaders', '\\hskip']
#         self.leaders_fill = ['\\leaders', '\\hfill']
#
#     def use_form1(self):
#         return random.choice(self.dots)
#
#     def use_form2(self):
#         return random.choice(self.fills)
#
#     def use_form3(self, any_text1, any_text2):
#         case1 = "%s %s %s %s" % (self.leaders_skip[0], any_text1, self.leaders_skip[1], any_text2)
#         return case1
#
#     def use_form4(self, any_text):
#         case1 = "%s %s %s" % (self.leaders_fill[0], any_text, self.leaders_fill[1])
#         return case1
#
#     def gen_something(self):
#         pass
#
# class TEXFontsAndMagnification:
#     def __init__(self):
#         self.fontnames = [
#             # Computer Modern 字体
#             "cmr5", "cmr6", "cmr7", "cmr8", "cmr9", "cmr10", "cmr12", "cmr17",
#             "cmbx5", "cmbx6", "cmbx7", "cmbx8", "cmbx9", "cmbx10", "cmbx12", "cmbx17",
#             "cmti5", "cmti6", "cmti7", "cmti8", "cmti9", "cmti10", "cmti12", "cmti17",
#             "cmbxti5", "cmbxti6", "cmbxti7", "cmbxti8", "cmbxti9", "cmbxti10", "cmbxti12", "cmbxti17",
#             "cmtt5", "cmtt6", "cmtt7", "cmtt8", "cmtt9", "cmtt10", "cmtt12", "cmtt17",
#             "cmmi5", "cmmi6", "cmmi7", "cmmi8", "cmmi9", "cmmi10", "cmmi12", "cmmi17",
#             "cmsy5", "cmsy6", "cmsy7", "cmsy8", "cmsy9", "cmsy10", "cmsy12", "cmsy17", "cmex10",
#             # Latin Modern 字体
#             "lmr5", "lmr6", "lmr7", "lmr8", "lmr9", "lmr10", "lmr12", "lmr17",
#             "lmbx5", "lmbx6", "lmbx7", "lmbx8", "lmbx9", "lmbx10", "lmbx12", "lmbx17",
#             "lmti5", "lmti6", "lmti7", "lmti8", "lmti9", "lmti10", "lmti12", "lmti17",
#             "lmbxti5", "lmbxti6", "lmbxti7", "lmbxti8", "lmbxti9", "lmbxti10", "lmbxti12", "lmbxti17",
#             "lmtt5", "lmtt6", "lmtt7", "lmtt8", "lmtt9", "lmtt10", "lmtt12", "lmtt17"
#         ]
#         self.fonts = ["\\rm",  "\\bf",  "\\tt",  "\\sl",  "\\it", "\\/"]
#         self.magnification = ["\\magnification", "\\magstep", "\\magstephalf"]
#         self.fontFN = ["\\font\\FN"]
#         self.true_dimen = ["true"]
#         self.char_symbol = ["\\char"]
#
#     def use_form1(self):
#         return random.choice(self.fonts)
#
#     def use_form2(self, any_number):
#         case1 = "%s=%s" % (self.magnification[0], any_number)
#         case2 = "%s %s" % (self.magnification[1], any_number)
#         case3 = self.magnification[2]
#         return random.choice([case1, case2, case3])
#
#     def use_form3(self, any_dimen):
#         fontname = random.choice(self.fontnames)
#         case1 = "%s=%s" % (self.fontFN[0], fontname)
#         case2 = "%s=%s at %s" % (self.fontFN[0], fontname, any_dimen)
#         case3 = "%s=%s scaled %s" % (self.fontFN[0], fontname, any_dimen)
#         return random.choice([case1, case2, case3])
#
#     def use_form4(self, any_dimen):
#         return "%s %s" % (self.true_dimen[0], any_dimen)
#
#     def use_form5(self):
#         decimal_list = list(range(256))
#         octal_list = [oct(i) for i in range(0o377 + 1)]
#         hex_list = [hex(i) for i in range(0xFF + 1)]
#         case1 = "%s%d" % (self.char_symbol[0], random.choice(decimal_list))
#         case2 = "%s'%s" % (self.char_symbol[0], random.choice(octal_list))
#         case3 = "%s\"%s" % (self.char_symbol[0], random.choice(hex_list))
#         return random.choice([case1, case2, case3])
#
#
# class AlignmentDisplays:
#     def __init__(self):
#         self.simple_line = ["\\+", "&", "\\cr"]
#         self.settabs = ["\\settabs", "\\columns"]
#         self.openup = ["\\openup"]
#         self.tabskip = ["\\tabskip"]
#
#         self.halign_form = ["\\halign", "to"]         # 表格头
#         self.form1 = ["\\omit",  "\\span",  "\\hidewidth", "\\crcr", "\\cr"]
#         self.form2 = ["\\noalign"]
#         self.form3 = ["\\multispan"]
#
#     # \+ ... \r
#     def generate_random_simpleline(self, num_columns):
#         # 随机生成列宽度（1.0 到 3.0 之间的浮点数）
#         widths = [round(random.uniform(1.0, 3.0), 1) for _ in range(num_columns)]
#         # 随机选择对齐方式（左对齐、居中对齐、右对齐）
#         alignments = ["左对齐", "居中对齐", "右对齐"]
#         selected_alignments = [random.choice(alignments) for _ in range(num_columns)]
#         # 构建 simple line
#         simple_line = r"\settabs \+ "
#         for width, alignment in zip(widths, selected_alignments):
#             if alignment == "左对齐":
#                 simple_line += rf"\hskip {width}in & "
#             elif alignment == "居中对齐":
#                 simple_line += rf"\hfil \hskip {width}in \hfil & "
#             elif alignment == "右对齐":
#                 simple_line += rf"\hskip {width}in \hfil & "
#         # 去掉最后一个多余的 "& " 并添加 \cr
#         simple_line = simple_line.rstrip("& ") + r" \cr"
#         return simple_line
#
#     def use_settabls(self, any_number, any_lines):
#         case1 = "%s %s %s" % (self.settabs[0], any_number, self.settabs[1])
#         case2 = "%s %s" % (self.settabs[0], any_lines)
#         return "%s%s" % (self.settabs[0], any_number)
#
#     def use_openup(self, any_dimen):
#         return "%s %s" % (self.openup[0], any_dimen)
#
#     def use_tabskip(self, any_glue):
#         return "%s=%s" % (self.tabskip[0], any_glue)
#
#     def use_form1(self):
#         return random.choice(self.form1)
#
#     def use_form2(self, any_text):          # vmode material
#         return "%s{%s}" % (self.form2[0], any_text)
#
#     def use_form3(self, any_number):
#         return "%s %s" % (self.form3[0], any_number)
#
#     def gen_random_table(self, table_num, any_text, any_number):
#         table_lines = []
#         res = ''
#         for i in range(table_num):
#             case1 = self.use_form1()
#             case2 = self.use_form2(any_text)
#             case3 = self.use_form3(any_number)
#             res += random.choice([case1, case2, case3]) + '\n'
#         return res
#
#     def table_head_form(self, any_table):
#         case1 = "%s{%s}" % (self.halign_form[0], any_table)
#         case2 = "%s %s %s" % (self.halign_form[0], self.halign_form[1], any_table)
#         return random.choice([case1, case2])
#
#
# class Boxes:
#     def __init__(self):
#         self.boxes = {
#             "hbox": "\\hbox to〈dimen〉", "vbox": "\\vbox to〈dimen〉", "vtop": "\\vtop to〈dimen〉",
#             "vcenter": "\\vcenter to〈dimen〉", "rlap": "\\rlap", "llap": "\\llap"
#         }
#
# class OverfullBoxes:
#     def __init__(self):
#         self.boxes = {
#             "hfuzz": "\\hfuzz", "vfuzz": "\\vfuzz", "overfullrule": "\\overfullrule"
#         }
#
# class IndentationAndItemizedLists:
#     def __init__(self):
#         self.indentation = {
#             "indent": "\\indent", "noindent": "\\noindent", "parindent": "\\parindent=〈dimen〉",
#             "displayindent": "\\displayindent=〈dimen〉", "leftskip": "\\leftskip=〈dimen〉",
#             "rightskip": "\\rightskip=〈dimen〉", "narrower": "\\narrower", "item": "\\item{〈label〉}",
#             "itemitem": "\\itemitem{〈label〉}"
#         }
#
# class HeadersFootersAndPageNumbers:
#     def __init__(self):
#         self.page_numbers = {
#             "nopagenumbers": "\\nopagenumbers", "pageno": "\\pageno", "folio": "\\folio",
#             "footline": "\\footline", "headline": "\\headline"
#         }
#
# class MacroDefinitions:
#     def __init__(self):
#         self.macro_definitions = {
#             "def": "\\def\\cs{〈replacement text〉}", "let": "\\let\\cs=〈token〉",
#             "longdef": "\\long\\def", "outerdef": "\\outer\\def", "globaldef": "\\global\\def",
#             "edef": "\\edef", "xdef": "\\xdef", "noexpand": "\\noexpand", "expandafter": "\\expandafter"
#         }
#
# class Conditionals:
#     def __init__(self):
#         self.conditionals = {
#             "if": "\\if〈condition〉〈true text〉\\else〈false text〉\\fi", "ifnum": "\\ifnum〈num1〉〈relation〉〈num2〉",
#             "ifdim": "\\ifdim〈dimen1〉〈relation〉〈dimen2〉", "ifodd": "\\ifodd〈num〉", "ifmmode": "\\ifmmode",
#             "ifx": "\\ifx〈token1〉〈token2〉", "ifdim": "\\ifdim〈dim1〉〈dim2〉", "ifeof": "\\ifeof〈number〉",
#             "iftrue": "\\iftrue", "iffalse": "\\iffalse", "ifcase": "\\ifcase〈number〉〈text0〉\\or〈text1〉\\or· · ·"
#         }
#


#
# class HorizontalSpacing:
#     def __init__(self):
#         self.spacing = {
#             "quad": "\\quad", "qquad": "\\qquad", "hskip": "\\hskip〈glue〉", "hfil": "\\hfil",
#             "hfill": "\\hfill", "hfilneg": "\\hfilneg", "thinspace": "\\thinspace", "enspace": "\\enspace"
#         }
#
# class VerticalSpacing:
#     def __init__(self):
#         self.spacing = {
#             "vskip": "\\vskip〈glue〉", "vfil": "\\vfil", "vfill": "\\vfill", "strut": "\\strut",
#             "phantom": "\\phantom{〈text〉}", "vphantom": "\\vphantom{〈text〉}", "hphantom": "\\hphantom{〈text〉}"
#         }
#
# class SkipSpaceBetweenLines:
#     def __init__(self):
#         self.spacing = {
#             "smallskip": "\\smallskip", "medskip": "\\medskip", "bigskip": "\\bigskip",
#             "smallbreak": "\\smallbreak", "medbreak": "\\medbreak", "bigbreak": "\\bigbreak",
#             "filbreak": "\\filbreak"
#         }
#
# class SetLineSpacing:
#     def __init__(self):
#         self.spacing = {
#             "baselineskip": "\\baselineskip = 〈glue〉", "single_space": "\\baselineskip = 12pt",
#             "one_and_half_space": "\\baselineskip = 18pt", "double_space": "\\baselineskip = 24pt",
#             "openup": "\\openup〈dimen〉", "jot": "1\\jot = 3pt"
#         }
#
# class AllowUnjustifiedLines:
#     def __init__(self):
#         self.justification = {
#             "raggedright": "\\raggedright", "raggedbottom": "\\raggedbottom"
#         }
#
# class BracesAndMatrices:
#     def __init__(self):
#         self.matrices = {
#             "matrix": "\\matrix", "pmatrix": "\\pmatrix", "bordermatrix": "\\bordermatrix",
#             "overbrace": "\\overbrace", "underbrace": "\\underbrace"
#         }
#
# class DisplayedEquations:
#     def __init__(self):
#         self.equations = {
#             "eqno": "\\eqno", "leqno": "\\leqno", "eqalign": "\\eqalign", "eqalignno": "\\eqalignno",
#             "leqalignno": "\\leqalignno", "displaylines": "\\displaylines", "cases": "\\cases",
#             "noalign": "\\noalign", "openup": "\\openup〈dimen〉"
#         }
