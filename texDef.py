import random

class MathLatter(object):
    def use(self, num=1):
        pass


class GreekLetters(MathLatter):
    def __init__(self):
        '''
        希腊字母，表示特定的数学或科学符号
        '''
        self.letters = ['\\alpha', '\\iota', '\\varrho', '\\beta', '\\kappa', '\\sigma', '\\gamma', '\\lambda', '\\varsigma', '\\delta', '\\mu', '\\tau', '\\epsilon', '\\nu', '\\upsilon', '\\varepsilon', '\\xi', '\\phi', '\\zeta', '\\o', '\\varphi', '\\eta', '\\pi', '\\chi', '\\theta', '\\varpi', '\\psi', '\\vartheta', '\\rho', '\\omega', '\\Gamma', '\\Xi', '\\Phi', '\\Delta', '\\Pi', '\\Psi', '\\Theta', '\\Sigma', '\\Omega', '\\Lambda', '\\Upsilon']         # len -> 34

    def use(self, nums=1):
        '''
        :param nums: 随机生成的字符个数，nums < 34
        :return: 随机生成的字符列表
        '''
        if nums > 34:
            return []
        text_list = ["$" + item + "$" for item in random.sample(self.letters, nums)]
        return text_list

    def useOne(self):
        return "$"+ random.choice(list(self.letters.values()))  +"$"

class SymbolsOfTypeOrd(MathLatter):
    def __init__(self):
        '''
        这些符号在数学模式中通常用于表示变量、常量或其他普通数学对象，而不是操作符、关系符号或其他特殊符号。
        '''
        self.symbols = ['\\aleph', '\\prime', '\\forall', '\\hbar', '\\emptyset', '\\exists', '\\imath', '\\nabla', '\\neg', '\\lnot', '\\surd', '\\flat', '\\ell', '\\top', '\\natural', '\\wp', '\\bot', '\\sharp', '\\Re', '\\clubsuit', '\\Im', '\\angle', '\\diamondsuit', '\\partial', '\\triangle', '\\heartsuit', '\\infty', '\\backslash', '\\spadesuit']


class LargeOperators(MathLatter):
    def __init__(self):
        self.operators = ['\\sumT', '\\bigcapJ', '\\bigodotQ', '\\prodS', '\\bigcupN', '\\coprodF', '\\bigsqcupL', '\\bigoplusR', '\\intW', '\\bigveeU', '\\biguplusH', '\\ointV', '\\bigwedge']

    def advance_use(self, _1, _2):
        op = random.choice(list(self.operators))
        return "$ %s_{%s}^{%s} $" % (op, _1, _2)


class BinaryOperations(MathLatter):
    def __init__(self):
        self.operations = ['\\pm', '\\cap', '\\vee', '\\lor', '\\mp', '\\cup', '\\wedge', '\\land', '\\setminus', '\\uplus', '\\oplus', '\\cdot', '\\sqcap', '\\ominus', '\\times', '\\sqcup', '\\otimes', '\\ast', '\\triangleleft', '\\oslash', '\\star', '\\triangleright', '\\odot', '\\diamond', '\\wr', '\\dagger', '\\circ', '\\bigcirc', '\\ddagger', '\\bullet', '\\bigtriangleup', '\\amalg', '\\div', '\\bigtriangledown']


class PageLayout:
    def __init__(self):
        self.layout = ['\\leq', '\\le', '\\geq', '\\ge', '\\equiv', '\\prec', '\\succ', '\\sim', '\\preceq', '\\succeq', '\\simeq', '\\ll', '\\gg', '\\asymp', '\\subset', '\\supset', '\\approx', '\\subseteq', '\\supseteq', '\\cong', '\\sqsubseteq', '\\sqsupseteq', '\\bowtie', '\\in', '\\notin', '\\owns', '\\vdash', '\\dashv', '\\models', '\\smile', '\\doteq', '\\frown', '\\parallel', '\\perp', '\\propto', '\\equiv', '\\notin', '\\ne']

    def use(self, dimen):
        lo = random.choice(list(self.layout))
        return "%s=%s" % (lo, dimen)

class Relations(MathLatter):
    def __init__(self):
        self.relations = [
            "\\leq", "\\ge", "\\equiv", "\\prec", "\\subset", "\\in",
            "\\approx", "\\propto", "\\perp", "\\sim"
        ]

class Arrows(MathLatter):
    def __init__(self):
        self.arrows = {
            "←": "\\leftarrow", "→": "\\rightarrow", "⇐": "\\Leftarrow", "⇒": "\\Rightarrow",
            "↔": "\\leftrightarrow", "↗": "\\nearrow", "↓": "\\downarrow"
        }

class Delimiters(MathLatter):
    def __init__(self):
        self.delimiters = {
            "[": "\\lbrack", "{": "\\lbrace", "]": "\\rbrack", "}": "\\rbrace", "|": "\\vert",
            "⌈": "\\lceil", "⌉": "\\rceil", "⌊": "\\lfloor", "⌋": "\\rfloor"
        }

class Accents:
    def __init__(self):
        '''
        可嵌套
        \hat{\hat A} 空格或者 {} 区分
        '''
        self.accents = [
             "\\hat",  "\\tilde",  "\\check",  "\\acute",  "\\grave",
             "\\dot",  "\\breve",  "\\bar",  "\\vec"
        ]

    def use(self, any_text):
        arr = random.choice(list(self.accents))
        case1 = "%s{%s}" % (arr, any_text)
        case2 = "%s %s" % (arr, any_text)
        return random.choice([case1, case2])

class ElementaryMathControlSequences:
    def __init__(self):
        self.control_sequences = [
            '\\root', '\\over', '\\atop', '\\choose', '\\brace', '\\brack',
            '\\displaystyle', '\\textstyle', '\\scriptstyle', '\\scriptscriptstyle'
        ]

        self.form_1 = {
            "overline": "\\overline", "underline": "\\underline", "sqrt": "\\sqrt"
        }
        self.form_2 = {
            "root": "\\root",
            "of": "\\of"
        }
        self.form_3 = {

        }

    def onePara(self):
        '''
        \pri{} or \pri xxx
        :return:
        '''


class NonItalicFunctionNames:
    def __init__(self):
        self.functions = {
            "arccos": "\\arccos", "arcsin": "\\arcsin", "arctan": "\\arctan", "arg": "\\arg",
            "cos": "\\cos", "cosh": "\\cosh", "cot": "\\cot", "coth": "\\coth", "csc": "\\csc",
            "deg": "\\deg", "det": "\\det", "exp": "\\exp", "gcd": "\\gcd", "hom": "\\hom",
            "inf": "\\inf", "ker": "\\ker", "lg": "\\lg", "lim": "\\lim", "liminf": "\\liminf",
            "limsup": "\\limsup", "log": "\\log", "log2": "\\log_2", "ln": "\\ln", "log": "\\log",
            "max": "\\max", "min": "\\min", "Pr": "\\Pr", "sec": "\\sec", "sin": "\\sin",
            "sinh": "\\sinh", "sup": "\\sup", "tan": "\\tan", "tanh": "\\tanh"
        }

class FootnotesInsertionsAndUnderlines:
    def __init__(self):
        self.insertions = {
            "footnote": "\\footnote{〈marker〉{〈text〉}}",
            "topinsert": "\\topinsert〈vmode material〉\\endinsert",
            "pageinsert": "\\pageinsert〈vmode material〉\\endinsert",
            "midinsert": "\\midinsert〈vmode material〉\\endinsert",
            "underbar": "\\underbar{〈text〉}"
        }

class UsefulParametersAndConversions:
    def __init__(self):
        self.parameters = {
            "day": "\\day", "month": "\\month", "year": "\\year", "jobname": "\\jobname",
            "romannumeral": "\\romannumeral〈number〉", "uppercase": "\\uppercase{〈token list〉}",
            "lowercase": "\\lowercase{〈token list〉}"
        }

class FillsLeadersAndEllipses:
    def __init__(self):
        self.fills = {
            "dots": "\\dots", "ldots": "\\ldots", "cdots": "\\cdots", "vdots": "\\vdots",
            "ddots": "\\ddots", "hrulefill": "\\hrulefill", "rightarrowfill": "\\rightarrowfill",
            "leftarrowfill": "\\leftarrowfill", "dotfill": "\\dotfill"
        }

class TEXFontsAndMagnification:
    def __init__(self):
        self.fonts = {
            "rm": "\\rm", "bf": "\\bf", "tt": "\\tt", "sl": "\\sl", "it": "\\it",
            "magnification": "\\magnification=〈number〉", "magstep": "\\magstep〈number〉",
            "magstephalf": "\\magstephalf", "font": "\\font\\FN=〈fontname〉", "char": "\\char‘\\c"
        }

class AlignmentDisplays:
    def __init__(self):
        self.alignments = {
            "settabs": "\\settabs〈number〉\\columns", "halign": "\\halign", "openup": "\\openup〈dimen〉",
            "noalign": "\\noalign{〈vmode material〉}", "tabskip": "\\tabskip=〈glue〉",
            "omit": "\\omit", "span": "\\span", "multispan": "\\multispan〈number〉", "hidewidth": "\\hidewidth"
        }

class Boxes:
    def __init__(self):
        self.boxes = {
            "hbox": "\\hbox to〈dimen〉", "vbox": "\\vbox to〈dimen〉", "vtop": "\\vtop to〈dimen〉",
            "vcenter": "\\vcenter to〈dimen〉", "rlap": "\\rlap", "llap": "\\llap"
        }

class OverfullBoxes:
    def __init__(self):
        self.boxes = {
            "hfuzz": "\\hfuzz", "vfuzz": "\\vfuzz", "overfullrule": "\\overfullrule"
        }

class IndentationAndItemizedLists:
    def __init__(self):
        self.indentation = {
            "indent": "\\indent", "noindent": "\\noindent", "parindent": "\\parindent=〈dimen〉",
            "displayindent": "\\displayindent=〈dimen〉", "leftskip": "\\leftskip=〈dimen〉",
            "rightskip": "\\rightskip=〈dimen〉", "narrower": "\\narrower", "item": "\\item{〈label〉}",
            "itemitem": "\\itemitem{〈label〉}"
        }

class HeadersFootersAndPageNumbers:
    def __init__(self):
        self.page_numbers = {
            "nopagenumbers": "\\nopagenumbers", "pageno": "\\pageno", "folio": "\\folio",
            "footline": "\\footline", "headline": "\\headline"
        }

class MacroDefinitions:
    def __init__(self):
        self.macro_definitions = {
            "def": "\\def\\cs{〈replacement text〉}", "let": "\\let\\cs=〈token〉",
            "longdef": "\\long\\def", "outerdef": "\\outer\\def", "globaldef": "\\global\\def",
            "edef": "\\edef", "xdef": "\\xdef", "noexpand": "\\noexpand", "expandafter": "\\expandafter"
        }

class Conditionals:
    def __init__(self):
        self.conditionals = {
            "if": "\\if〈condition〉〈true text〉\\else〈false text〉\\fi", "ifnum": "\\ifnum〈num1〉〈relation〉〈num2〉",
            "ifdim": "\\ifdim〈dimen1〉〈relation〉〈dimen2〉", "ifodd": "\\ifodd〈num〉", "ifmmode": "\\ifmmode",
            "ifx": "\\ifx〈token1〉〈token2〉", "ifdim": "\\ifdim〈dim1〉〈dim2〉", "ifeof": "\\ifeof〈number〉",
            "iftrue": "\\iftrue", "iffalse": "\\iffalse", "ifcase": "\\ifcase〈number〉〈text0〉\\or〈text1〉\\or· · ·"
        }

class DimensionsSpacingAndGlue:
    def __init__(self):
        self.dimensions = {
            "point": "pt", "pica": "pc", "inch": "in", "centimeter": "cm", "millimeter": "mm",
            "mu": "mu", "em": "em", "ex": "ex", "mathunit": "mu", "glue": "〈dimen〉 plus〈dimen〉 minus〈dimen〉"
        }

class HorizontalSpacing:
    def __init__(self):
        self.spacing = {
            "quad": "\\quad", "qquad": "\\qquad", "hskip": "\\hskip〈glue〉", "hfil": "\\hfil",
            "hfill": "\\hfill", "hfilneg": "\\hfilneg", "thinspace": "\\thinspace", "enspace": "\\enspace"
        }

class VerticalSpacing:
    def __init__(self):
        self.spacing = {
            "vskip": "\\vskip〈glue〉", "vfil": "\\vfil", "vfill": "\\vfill", "strut": "\\strut",
            "phantom": "\\phantom{〈text〉}", "vphantom": "\\vphantom{〈text〉}", "hphantom": "\\hphantom{〈text〉}"
        }

class SkipSpaceBetweenLines:
    def __init__(self):
        self.spacing = {
            "smallskip": "\\smallskip", "medskip": "\\medskip", "bigskip": "\\bigskip",
            "smallbreak": "\\smallbreak", "medbreak": "\\medbreak", "bigbreak": "\\bigbreak",
            "filbreak": "\\filbreak"
        }

class SetLineSpacing:
    def __init__(self):
        self.spacing = {
            "baselineskip": "\\baselineskip = 〈glue〉", "single_space": "\\baselineskip = 12pt",
            "one_and_half_space": "\\baselineskip = 18pt", "double_space": "\\baselineskip = 24pt",
            "openup": "\\openup〈dimen〉", "jot": "1\\jot = 3pt"
        }

class AllowUnjustifiedLines:
    def __init__(self):
        self.justification = {
            "raggedright": "\\raggedright", "raggedbottom": "\\raggedbottom"
        }

class BracesAndMatrices:
    def __init__(self):
        self.matrices = {
            "matrix": "\\matrix", "pmatrix": "\\pmatrix", "bordermatrix": "\\bordermatrix",
            "overbrace": "\\overbrace", "underbrace": "\\underbrace"
        }

class DisplayedEquations:
    def __init__(self):
        self.equations = {
            "eqno": "\\eqno", "leqno": "\\leqno", "eqalign": "\\eqalign", "eqalignno": "\\eqalignno",
            "leqalignno": "\\leqalignno", "displaylines": "\\displaylines", "cases": "\\cases",
            "noalign": "\\noalign", "openup": "\\openup〈dimen〉"
        }
