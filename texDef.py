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
            # "cmbxti5", "cmbxti6", "cmbxti7", "cmbxti8", "cmbxti9", "cmbxti10", "cmbxti12", "cmbxti17",
            "cmss5", "cmss6", "cmss7", "cmss8", "cmss9", "cmss10", "cmss12", "cmss17",
            "cmtt5", "cmtt6", "cmtt7", "cmtt8", "cmtt9", "cmtt10", "cmtt12", "cmtt17",
            "cmmi5", "cmmi6", "cmmi7", "cmmi8", "cmmi9", "cmmi10", "cmmi12", "cmmi17",
            "cmsy5", "cmsy6", "cmsy7", "cmsy8", "cmsy9", "cmsy10", "cmsy12", "cmsy17",
            "cmex5", "cmex6", "cmex7", "cmex8", "cmex9", "cmex10", "cmex12", "cmex17",
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

    def use_form1(self):
        return random.choice(self.fonts)

    def use_form2(self, number):
        case1 = "%s=%s" % (self.magnification[0], number)
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
        tex_text += self.use_form2(self.number.uint_number()) + '\n'
        tex_text += self.use_form3(self.dimen.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form4(self.dimen.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form5() + '\n'
        return tex_text

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
#         self.text = random_input.AnyText()
#         self.number = random_input.AnyNumber()
#         self.dimen = random_input.DimensionsSpacingAndGlue()
#
#     # \+ ... \r
#     def gen_random_simpleline(self, num_columns):
#         num_columns = int(num_columns)
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
#         return random.choice([case1, case2])
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
#     def gen_random_table(self, rows, cols, any_dimen, any_text):
#         """
#         随机生成一个包含指定命令的 Plain TeX 表格。
#         参数:
#             rows (int): 表格的行数。
#             cols (int): 表格的列数。
#         返回:
#             str: 生成的 Plain TeX 表格代码。
#         """
#         # 定义可用的命令及其参数
#         commands = [
#             "\\omit",  # 忽略当前列的格式
#             "\\span",  # 跨列
#             "\\hidewidth",  # 隐藏宽度
#             "\\crcr",  # 换行
#             "\\cr",  # 换行
#             "\\noalign",  # 插入额外内容
#             "\\multispan",  # 跨多列
#         ]
#         rows = int(rows)
#         cols = int(cols)
#
#         # 生成列格式
#         col_format = " & ".join(["c"] * cols)  # 每列居中对齐
#
#         # 生成表格内容
#         table_head = ['']
#         case1 = "%s {{ {%s} \\cr\n" % (self.halign_form[0], col_format)
#         case2 = "%s %s %s {{ {%s} \\cr\n" % (self.halign_form[0], self.halign_form[1], any_dimen, col_format)
#         table = random.choice([case1, case2])
#         # table = f"\\halign to 1sp {{ {col_format} \\cr\n"
#         for row in range(rows):
#             row_content = []
#             for col in range(cols):
#                 # 随机选择一个命令
#                 command = random.choice(commands)
#
#                 # 根据命令生成内容
#                 if command == "\\omit":
#                     row_content.append("\\omit " + any_text)
#                 elif command == "\\span":
#                     row_content.append(
#                         "\\span " + str(random.randint(1, cols - col)) + " " + any_text)
#                 elif command == "\\hidewidth":
#                     row_content.append("\\hidewidth " + random.choice(["W", "H", "I"]))
#                 elif command == "\\multispan":
#                     row_content.append(
#                         "\\multispan " + str(random.randint(1, cols - col)) + " " + any_text)
#                 else:
#                     row_content.append(any_text)
#
#             # 随机插入 \\noalign
#             if random.random() < 0.3:  # 30% 的概率插入 \\noalign
#                 table += "\\noalign{" + random.choice(["*", "\\hrule", "\\vskip 5pt"]) + "}\n"
#
#             # 添加行内容
#             table += " & ".join(row_content) + " \\cr\n"
#
#         table += "}"
#         return table
#
#     # def gen_random_table(self, table_num, any_text, any_number):
#     #     res = ''
#     #     for i in range(table_num):
#     #         case1 = self.use_form1()
#     #         case2 = self.use_form2(any_text)
#     #         case3 = self.use_form3(any_number)
#     #         res += random.choice([case1, case2, case3]) + '\n'
#     #     return res
#     #
#     # def table_head_form(self, any_table, any_dimen):
#     #
#     #     return random.choice([case1, case2])
#
#     def random_tex_table(self, rows, cols):
#         """
#         随机生成一个包含指定命令的 Plain TeX 表格。
#
#         参数:
#             rows (int): 表格的行数。
#             cols (int): 表格的列数。
#
#         返回:
#             str: 生成的 Plain TeX 表格代码。
#         """
#         # 定义可用的命令及其参数
#         commands = [
#             "\\omit",  # 忽略当前列的格式
#             "\\span",  # 跨列
#             "\\hidewidth",  # 隐藏宽度
#             "\\crcr",  # 换行
#             "\\cr",  # 换行
#             "\\noalign",  # 插入额外内容
#             "\\multispan",  # 跨多列
#         ]
#
#         # 生成合法的列格式，每列包含一个 # 占位符
#         col_format = " & ".join(["c#"] * cols)  # 每列居中对齐，并包含 # 占位符
#
#         # 生成表格内容
#         table = f"\\halign to 1sp {{ {col_format} \\cr\n"
#         for row in range(rows):
#             row_content = []
#             col = 0
#             while col < cols:
#                 # 随机选择一个命令
#                 command = random.choice(commands)
#
#                 # 根据命令生成内容
#                 if command == "\\omit":
#                     row_content.append("\\omit " + random.choice(["A", "B", "C", "D"]))
#                     col += 1
#                 elif command == "\\span":
#                     span_cols = random.randint(1, cols - col)
#                     row_content.append(f"\\span {span_cols} " + random.choice(["X", "Y", "Z"]))
#                     col += span_cols
#                 elif command == "\\hidewidth":
#                     row_content.append("\\hidewidth " + random.choice(["W", "H", "I"]))
#                     col += 1
#                 elif command == "\\multispan":
#                     span_cols = random.randint(1, cols - col)
#                     row_content.append(f"\\multispan {span_cols} " + random.choice(["M", "N", "O"]))
#                     col += span_cols
#                 else:
#                     row_content.append(random.choice(["A", "B", "C", "D"]))
#                     col += 1
#
#             # 随机插入 \\noalign
#             if random.random() < 0.3:  # 30% 的概率插入 \\noalign
#                 table += "\\noalign{" + random.choice(["*", "\\hrule", "\\vskip 5pt"]) + "}\n"
#
#             # 添加行内容
#             table += " & ".join(row_content) + " \\cr\n"
#
#         table += "}"
#         return table
#
#     def gen_something(self):
#         tex_text = ''
#         tex_text += self.random_tex_table(3, 5) + '\n'
#         # tex_text += self.gen_random_table(
#         #     # self.number.uint_number(), self.number.uint_number(),
#         #     3,3,
#         #     self.dimen.gen_any_stand_dimen(),
#         #     self.text.simple_string()) + '\n'
#         # tex_text += self.use_settabls(self.number.uint_number(),
#         #                               self.gen_random_simpleline(self.number.uint_number())) + '\n'
#         # tex_text += self.use_openup(self.dimen.gen_any_stand_dimen()) + '\n'
#         # tex_text += self.use_tabskip(self.dimen.gen_any_stand_glue()) + '\n'
#         return tex_text


class Boxes:
    def __init__(self):
        self.boxes = [
            "\\hbox", "\\vbox", "\\vtop"
        ]
        self.lap = ['\\rlap', 'llap']
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
                                   self.text.simple_string()) + '\n'
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


# class IndentationAndItemizedLists:
#     def __init__(self):
#         self.form1 = [
#             "\\item", "\\itemitem"
#         ]
#         self.form2 = [
#             "\\indent", "\\noindent", "\\narrower"
#         ]
#         self.form3 = [
#             "\\parindent", "\\displayindent", "\\leftskip", "\\rightskip", "\\hangident",
#         ]
#         self.form4 = [
#             "\\hangafter", "\\parshape"
#         ]
#
#     def use_form1(self, text):
#         case = random.choice(self.form1)
#         case1 = "%s { %s }" % (case, text)
#         return case1
#
#     def use_form2(self):
#         case = random.choice(self.form2)
#         return case
#
#     def use_form3(self, any_dimen):
#         case = random.choice(self.form3)
#         case1 = "%s = %s" % (case, any_dimen)
#         return case1
#
#     def use_form4(self, any_number):
#         case = random.choice(self.form4)
#         case1 = "%s = %s" % (case, any_number)
#         return case1
#
#     def gen_something(self):
#         tex_text = ''
#         tex_text += self.use_form1(self.text.simple_string()) + '\n'
#         tex_text += self.use_form2() + '\n'
#         tex_text += self.use_form3(self.dimen_space.gen_any_stand_dimen()) + '\n'
#         tex_text += self.use_form4(self.number.uint_number()) + '\n'
#         return tex_text

class IndentationAndItemizedLists:
    def __init__(self):
        self.indentation = ["\\indent",  "\\noindent",  "\\parindent", "\\displayindent",  "\\leftskip",
             "\\rightskip",  "\\narrower",  "\\item", "\\itemitem"
        ]
        self.form1 = ["\\indent",  "\\noindent", "\\narrower"]
        self.form2 = ["\\parindent", "\\displayindent",  "\\leftskip", "\\rightskip", '\\hangindent']
        self.form3 = ["\\beginsection", "\\item", "\\itemitem"]
        self.form4 = ["\\hangafter", "\\parshape"]
        self.dimen_space = random_input.DimensionsSpacingAndGlue()
        self.text = random_input.AnyText()
        self.numbers = random_input.AnyNumber()

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
        case1 = f"{case}={number}"
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.dimen_space.gen_any_stand_dimen(), self.text.simple_string()) + '\n'
        tex_text += self.use_form3(self.text.simple_string(),
                                    self.text.simple_string(),
                                    self.text.simple_string()) + '\n'
        tex_text += self.use_form4(self.numbers.uint_number()) + '\n'
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

class MacroDefinitions:
    def __init__(self):
        self.form1 = [
            "\\def", "gdef", "edef", "xdef"
        ]
        self.form2 = [
            "\\cs", "\\let"
        ]
        self.form3 = [
            "\\long", "\\outer", "global"
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
            "\\number"
        ]

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
        case1 = "\\def\\foo{Hello, World!}\\n %s\\foo" % (self.form4[0])
        return case1

    def use_form5(self):
        case1 = "\\def\\a{Hello}\\def\\b{\\a}%s\\b\\relax" % (self.form5[0])
        return case1

    def use_form6(self):
        case1 = "%s\\next\\tokenA\\tokenB" % (self.form6[0])
        return case1

    def use_form7(self, text):
        case1 = "%s %s %s" % (self.form7[0], text, self.form7[1])
        return case1

    def use_form8(self, text):
        case1 = "%s%s%s" % (self.form8[0], self.form8[1], text)
        return case1

    def use_form9(self, any_number):
        case1 = "%s%s" % (self.form9, any_number)
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
            "\\loop", "\\if", "\\repeat"
        ]
        self.form10 = [
            "\\newif", "\\ifblob", "\\blobtrue", "\\blobfalse"
        ]

    def use_form1(self, text1, text2, text3):
        case1 = "%s %s %s %s %s %s" % (self.form1[0], text1, text2, self.form1[1], text3, self.form1[2])
        return case1

    def use_form2(self, any_number1, any_number2, any_relation):
        case1 = "%s %s %s %s" % (self.form2, any_number1, any_relation, any_number2)
        return case1

    def use_form3(self, any_dimen1, any_dimen2, any_relation):
        case1 = "%s %s %s %s " % (self.form3, any_dimen1, any_relation, any_dimen2)
        return case1

    def use_form4(self, any_number):
        case = random.choice(self.form4)
        case1 = "%s %s" % (case, any_number)
        return case1

    def use_form5(self):
        case = random.choice(self.form5)
        case1 = "%s" % (case)
        return case1

    def use_form6(self, text1, text2):
        case = random.choice(self.form6)
        case1 = "%s %s %s" % (case, text1, text2)
        return case1

    def use_form7(self, any_dimen1, any_dimen2):
        case1 = "%s %s %s" % (self.form7, any_dimen1, any_dimen2)
        return case1

    def use_form8(self, any_number, text1, text2, text3):
        case1 = "%s %s %s %s %s %s %s %s" % (
        self.form8[0], any_number, text1, self.form8[1], text2, self.form8[2], text3, self.form8[3])
        return case1

    def use_form9(self, text1, text2):
        case1 = "%s %s %s %s %s" % (self.form9[0], text1, self.form9[1], text2, self.form9[2])
        return case1

    def use_form10(self):
        case = random.choice(self.form10[2], self.form10[3])
        case1 = "%s %s %s " % (self.form10[0], self.form10[1], case)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.text.simple_string(), self.text.simple_string(),
                                   self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.number.uint_number(), self.number.uint_number(),
                                   self.rel.generate_random_relation()) + '\n'
        tex_text += self.use_form3(self.dimen_space.gen_any_stand_dimen(), self.dimen_space.gen_any_stand_dimen(),
                                   self.rel.generate_random_relation()) + '\n'
        tex_text += self.use_form4(self.number.uint_number()) + '\n'
        tex_text += self.use_form5() + '\n'
        tex_text += self.use_form6(self.text.simple_string(), self.text.simple_string()) + '\n'
        tex_text += self.use_form7(self.dimen_space.gen_any_stand_dimen(),
                                   self.dimen_space.gen_any_stand_dimen()) + '\n'
        tex_text += self.use_form8(self.number.uint_number(), self.text.simple_string(), self.text.simple_string(),
                                   self.text.simple_string()) + '\n'
        tex_text += self.use_form9(self.text.simple_string(), self.text.simple_string()) + '\n'
        tex_text += self.use_form10() + '\n'

        return tex_text


class HorizontalSpacing:
    def __init__(self):
        self.form1 = [
            "\\quad", "\\qquad", "\\thinspace", "\\enspace", "\\enskip",
            "\\hfill", "\\hfill", "\\hfilneg",
            "\\thickspace", "\\>", "\\medspace", "\\;", "\\!", "\\,", "\\negthinspace"
        ]
        self.form2 = [
            "\\hskip", "\\mskip"
        ]

    def use_form1(self):
        case = random.choice(self.form1)
        case1 = "%s" % (case)
        return case1

    def use_form2(self, any_length):
        case = random.choice(self.form2)
        case1 = "%s %s" % (case, any_length)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.leng.gen_length()) + '\n'

        return tex_text


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
            "\\raise", "\\lower", "\\moveleft", "\\moveright", "\\hbox", "\\vbox"
        ]

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
        case1 = random.choice(self.form4[0], self.form4[1], self.form4[2], self.form4[3])
        case2 = random.choice(self.form4[4], self.form4[5])
        case3 = "%s %s %s {%s}" % (case1, any_dimen, case2, text)
        return case3

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1() + '\n'
        tex_text += self.use_form2(self.leng.gen_length()) + '\n'
        tex_text += self.use_form3(self.text.simple_string()) + '\n'
        tex_text += self.use_form4(self.dimen_space.gen_any_stand_dimen(), self.text.simple_string()) + '\n'

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

    def use_form1(self, any_length):
        case = random.choice(self.form1)
        case1 = "%s = %s" % (case, any_length)
        return case1

    def use_form2(self, any_length):
        case1 = "%s %s" % (self.form2, any_length)
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

    def use_form1(self, any_matrix):
        case1 = "%s {%s}" % (self.form1, any_matrix)
        return case1

    def use_form2(self, any_matrix):
        case1 = "%s {%s}" % (self.form2, any_matrix)
        return case1

    def use_form3(self, any_matrix):
        case1 = "%s {%s}" % (self.form3, any_matrix)
        return case1

    def use_form4(self, text):
        case1 = "%s {%s}" % (self.form4, text)
        return case1

    def use_form5(self, text1, text2):
        case1 = "%s {%s}_{%s}" % (self.form5, text1, text2)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.generatorm.gen_tex_code()) + '\n'
        tex_text += self.use_form2(self.generatorpm.generate_matrix()) + '\n'
        tex_text += self.use_form3(self.generatorpb.generate_matrix2()) + '\n'
        tex_text += self.use_form4(self.text.simple_string()) + '\n'
        tex_text += self.use_form5(self.text.simple_string(), self.text.simple_string()) + '\n'

        return tex_text


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
        self.form6 = [
            "\\noalign"
        ]

    def use_form1(self, any_math, text):
        case = random.choice(self.form1)
        case1 = "%s %s %s" % (any_math, case, text)
        return case1

    def use_form2(self, any_formula):
        case1 = "%s {%s}" % (self.form2, any_formula)
        return case1

    def use_form3(self, any_formula):
        case = random.choice(self.form3)
        case1 = "%s {%s}" % (case, any_formula)
        return case1

    def use_form4(self, any_formula):
        case1 = "%s {%s}" % (self.form4, any_formula)
        return case1

    def use_form5(self, any_piece):
        case1 = "%s {%s}" % (self.form5, any_piece)
        return case1

    def use_form6(self, text):
        case1 = "%s {%s}" % (self.form6, text)
        return case1

    def gen_something(self):
        tex_text = ''
        tex_text += self.use_form1(self.reg.gen_math(self.reg.generate_equation()), self.text.simple_string()) + '\n'
        tex_text += self.use_form2(self.rmfg.gen_formula()) + '\n'
        tex_text += self.use_form3(self.afg.gen_formula1()) + '\n'
        tex_text += self.use_form4(self.rfg.gen_formula_block()) + '\n'
        tex_text += self.use_form5(self.piece.gen_piecewise_function()) + '\n'
        tex_text += self.use_form6(self.text.simple_string()) + '\n'

        return tex_text


if __name__ == '__main__':
    test_alignment_displays = AlignmentDisplays()
    print(test_alignment_displays.gen_something())