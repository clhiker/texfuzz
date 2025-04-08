import random
import string

class DimensionsSpacingAndGlue:
    def __init__(self):
        self.standard_dimensions = [
            "pt",  # 点（Point），1 pt ≈ 0.3515 mm
            "mm",  # 毫米（Millimeter）
            "cm",  # 厘米（Centimeter）
            "in",  # 英寸（Inch），1 in = 25.4 mm
            "bp",  # 大点（Big Point），1 bp = 1/72 in
            "pc",  # 派卡（Pica），1 pc = 12 pt
            "dd",  # Didot 点，1 dd ≈ 0.376 mm
            "cc",  # Cicero，1 cc = 12 dd
            "sp",  # Scaled Point，1 sp = 1/65536 pt
            "em",  # 当前字体中字母 "M" 的宽度
            "ex",  # 当前字体中字母 "x" 的高度
        ]
        self.math_units = [
            "mu",  # 数学单位，1 mu = 1/18 em
        ]
        self.dimensions = self.standard_dimensions + self.math_units
        # self.dimensions = ["pt",  "pc",  "in",  "cm", "em", "ex",  "mu", "mm"]
        self.glue = []

    def gen_any_stand_dimen(self):
        return "%s%s" % (str(random.randint(1, 9)), random.choice(self.standard_dimensions))

    def gen_any_math_dimen(self):
        return "%s%s" % (str(random.randint(1, 9)), random.choice(self.math_units))

    def gen_any_dimen(self):
        return "%s%s" % (str(random.randint(1, 9)), random.choice(self.dimensions))

    def gen_any_glue(self):
        # 随机决定是否包含 plus 部分
        include_plus = random.choice([True, False])
        if include_plus:
            # 随机生成可拉伸长度（0.1 到 2.0 之间的浮点数）
            plus_length = round(random.uniform(0.1, 2.0), 1)
        else:
            plus_length = None
        # 随机决定是否包含 minus 部分
        include_minus = random.choice([True, False])
        if include_minus:
            # 随机生成可压缩长度（0.1 到 1.0 之间的浮点数）
            minus_length = round(random.uniform(0.1, 1.0), 1)
        else:
            minus_length = None
        # 构造 glue 表达式
        glue = self.gen_any_dimen()
        if include_plus:
            glue += f" plus {plus_length}cm"
        if include_minus:
            glue += f" minus {minus_length}cm"
        return glue

    def gen_any_stand_glue(self):
        # 随机决定是否包含 plus 部分
        include_plus = random.choice([True, False])
        if include_plus:
            # 随机生成可拉伸长度（0.1 到 2.0 之间的浮点数）
            plus_length = round(random.uniform(0.1, 2.0), 1)
        else:
            plus_length = None
        # 随机决定是否包含 minus 部分
        include_minus = random.choice([True, False])
        if include_minus:
            # 随机生成可压缩长度（0.1 到 1.0 之间的浮点数）
            minus_length = round(random.uniform(0.1, 1.0), 1)
        else:
            minus_length = None
        # 构造 glue 表达式
        glue = self.gen_any_stand_dimen()
        if include_plus:
            glue += f" plus {plus_length}cm"
        if include_minus:
            glue += f" minus {minus_length}cm"
        return glue

class AnyText:
    def __init__(self):
        # 16个无效代码
        # self.cat_coders = ['\\', '{', '}', '$', '#', '^', '_', '@', '␣', '&', '%', '/', '?']       # #是数学模型不能用，其他未知
        self.special_symbol = ['#', '$', '%', '&', '{', '}', '_', '^', '~',
                               '\\', '"', "'", ';', '!', '<', '>', '|', '+',
                               '-', '=', '/', '?', '@', '[', ']', '`', '^', '~']
    def simple_string(self):
        # 定义所有可能的字符（包括字母、数字、标点符号等）
        characters = string.ascii_letters + string.digits + string.punctuation
        # 过滤掉反斜杠
        for key_char in self.special_symbol:
            characters = characters.replace(key_char, '')
        # 随机生成字符串的长度（1 到 10）
        length = random.randint(1, 10)
        # 生成随机字符串
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def rec_string(self):
        '''
        包含 tex 语句的随机字符串
        :return:
        '''
        return self.simple_string()

class AnyNumber:
    def __init__(self):
        pass
    def uint_number(self):
        return str(random.randint(1, 1000))

class AnyBoxRule:
    def __init__(self):
        self.boxs = ["\\hbox", "\\vbox", '\\setbox', '\\box' ]
        self.box_type = ["\\rule"]
        self.dimen = DimensionsSpacingAndGlue()

    def any_box(self):
        # 随机生成盒子内容（文本）
        content = ''.join(
            random.choice(string.ascii_letters + string.digits + " ") for _ in range(random.randint(5, 20)))

        # 随机选择盒子类型：hbox 或 vbox
        box_type = random.choice([r"\hbox", r"\vbox"])

        # 随机决定是否保存盒子到寄存器
        if random.choice([True, False]):
            register = random.randint(0, 255)  # 确保寄存器编号在 0 到 255 之间
            # 生成代码，确保 \box 在最前面定义
            return fr"\box{register} \setbox{register}={box_type}{{{content}}}"
        else:
            # 直接生成盒子代码
            return fr"{box_type}{{{content}}}"

    def any_rule(self):
        # 随机选择水平线或垂直线
        line_type = random.choice([r"\hrule", r"\vrule"])

        # 随机生成高度、宽度和深度
        height = random.uniform(0.1, 2)
        width = random.uniform(1, 10)
        depth = random.uniform(0, 1)

        # 生成线条代码
        if line_type == r"\hrule":
            return fr"{line_type} height {height}pt width {width}cm depth {depth}pt"
        else:
            return fr"{line_type} height {height}cm width {width}pt depth {depth}pt"

    def any_box_rule(self):
        # 随机生成盒子内容
        box_content = self.any_box()
        # 随机生成规则
        rule_content = self.any_rule()

        # 随机决定规则是放在盒子内部还是外部
        if random.choice([True, False]):
            # 规则放在盒子内部
            if "{" in box_content and "}" in box_content:
                # 在盒子内容中插入规则
                box_content = box_content.replace("}", f" {rule_content}}}")
            else:
                # 如果盒子内容没有大括号，直接拼接
                box_content = fr"\hbox{{{box_content} {rule_content}}}"
            return box_content
        else:
            # 规则放在盒子外部
            return fr"{box_content} {rule_content}"

    def any_box_or_rule(self):
        # 随机选择生成盒子、线条或两者
        choice = random.choice(["box", "line"])

        if choice == "box":
            return self.any_box()
        else:
            return self.any_rule()


class AnyRelation:
    def __init__(self):
        self.relations = ["<", ">", "="]  # 支持的比较符号

    def generate_random_relation(self):
        """
        生成随机比较符号
        :return: 随机比较符号（如 "<", ">", "="
        """
        return random.choice(self.relations)


class RandomTexLength:
    def __init__(self):
        """
        初始化随机长度生成器
        """
        self.units = ["pt", "cm", "mm", "em", "ex"]  # 支持的长度单位

    def gen_length(self, min_value=1, max_value=1000):
        """
        生成随机长度
        :param min_value: 最小值（默认 1）
        :param max_value: 最大值（默认 100）
        :return: 随机长度（如 "10pt", "0.5cm"）
        """
        value = random.uniform(min_value, max_value)
        unit = random.choice(self.units)
        return f"{value:.2f}{unit}"  # 保留两位小数

class RandomTexLength2:
    def __init__(self):
        """
        初始化随机长度生成器
        """
        self.units = ["mu"]  # 支持的长度单位

    def gen_length(self, min_value=1, max_value=1000):
        """
        生成随机长度
        :param min_value: 最小值（默认 1）
        :param max_value: 最大值（默认 100）
        :return: 随机长度（如 "10pt", "0.5cm"）
        """
        value = random.uniform(min_value, max_value)
        unit = random.choice(self.units)
        return f"{value:.2f}{unit}"  # 保留两位小数


class RandomMatrixGenerator:
    def __init__(self, min_rows=2, max_rows=5, min_cols=2, max_cols=5, min_value=0, max_value=100):
        """
        初始化随机矩阵生成器
        :param min_rows: 最小行数（默认 2）
        :param max_rows: 最大行数（默认 5）
        :param min_cols: 最小列数（默认 2）
        :param max_cols: 最大列数（默认 5）
        :param min_value: 元素最小值（默认 0）
        :param max_value: 元素最大值（默认 100）
        """
        self.min_rows = min_rows
        self.max_rows = max_rows
        self.min_cols = min_cols
        self.max_cols = max_cols
        self.min_value = min_value
        self.max_value = max_value

    def generate_matrix(self):
        """
        生成随机矩阵
        :return: 随机矩阵（列表的列表）
        """
        rows = random.randint(self.min_rows, self.max_rows)
        cols = random.randint(self.min_cols, self.max_cols)
        matrix = [[random.randint(self.min_value, self.max_value) for _ in range(cols)] for _ in range(rows)]
        return matrix

    def gen_tex_code(self):
        """
        生成 plain TeX 格式的矩阵代码
        :return: plain TeX 格式的矩阵代码
        """
        matrix = self.generate_matrix()
        tex_code = ""
        for row in matrix:
            tex_code += "  " + " & ".join(map(str, row)) + " \\cr" + " "

        return tex_code


class RandomMatrixGenerator1:
    def __init__(self, max_rows=5, max_cols=5):
        """
        初始化随机矩阵生成器
        :param max_rows: 最大行数（默认 5）
        :param max_cols: 最大列数（默认 5）
        """
        self.max_rows = max_rows
        self.max_cols = max_cols

    def generate_element1(self):
        """
        生成随机矩阵元素
        :return: 随机元素（数字或符号）
        """
        if random.choice([True, False]):
            return str(random.randint(0, 9))  # 生成数字
        else:
            return random.choice(string.ascii_letters)  # 生成字母

    def generate_matrix(self):
        """
        生成随机矩阵
        :return: 符合 plain TeX 语法的矩阵
        """
        rows = random.randint(1, self.max_rows)  # 随机生成行数
        cols = random.randint(1, self.max_cols)  # 随机生成列数

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.generate_element1())  # 生成随机元素
            matrix.append(row)

        # 将矩阵转换为 plain TeX 语法
        tex_matrix = ""
        for row in matrix:
            tex_matrix += " & ".join(row) + " \\cr\n"

        return tex_matrix


class RandomMatrixGenerator2:
    def __init__(self, min_rows=2, max_rows=5, min_cols=2, max_cols=5):
        """
        初始化矩阵生成器
        :param min_rows: 最小行数（默认 2）
        :param max_rows: 最大行数（默认 5）
        :param min_cols: 最小列数（默认 2）
        :param max_cols: 最大列数（默认 5）
        """
        self.min_rows = min_rows
        self.max_rows = max_rows
        self.min_cols = min_cols
        self.max_cols = max_cols

    def generate_element2(self):
        """
        生成随机矩阵元素
        :return: 随机元素（数字、符号或表达式）
        """
        # 随机生成数字、符号或简单表达式
        options = [
            str(random.randint(0, 9)),  # 数字
            random.choice(['+', '-', '\\times', '\\div']),  # 符号
            f"{random.randint(1, 9)}^{random.randint(1, 9)}",  # 指数
            f"\\sqrt{{{random.randint(1, 9)}}}"  # 根号
        ]
        return random.choice(options)

    def generate_matrix2(self):
        """
        生成随机矩阵
        :return: 符合 plain TeX 语法的矩阵
        """
        # 随机生成行数和列数
        rows = random.randint(self.min_rows, self.max_rows)
        cols = random.randint(self.min_cols, self.max_cols)

        # 生成列标签
        col_labels = [f"c_{i + 1}" for i in range(cols)]

        # 生成行标签
        row_labels = [f"r_{i + 1}" for i in range(rows)]

        # 生成矩阵内容
        matrix_content = []
        for i in range(rows):
            row = [self.generate_element2() for _ in range(cols)]
            matrix_content.append(row)

        # 构建 plain TeX 矩阵
        tex_matrix = ""
        # 添加列标签
        tex_matrix += " & " + " & ".join(col_labels) + " \\cr\n"
        # 添加行标签和矩阵内容
        for i in range(rows):
            tex_matrix += row_labels[i] + " & " + " & ".join(matrix_content[i]) + " \\cr\n"

        return tex_matrix


class RandomEquationGenerator:
    def __init__(self, min_value=0, max_value=10, operators=None):
        """
        初始化随机公式生成器
        :param min_value: 常数的最小值（默认 0）
        :param max_value: 常数的最大值（默认 10）
        :param operators: 支持的数学运算符（默认 +, -, *, /）
        """
        self.min_value = min_value
        self.max_value = max_value
        self.operators = operators if operators else ["+", "-", "*", "/"]

    def generate_equation(self):
        """
        生成随机数学公式
        :return: 随机生成的数学公式（字符串）
        """
        variables = ["x", "y", "z"]
        var1 = random.choice(variables)
        var2 = random.choice(variables)
        operator = random.choice(self.operators)
        constant = random.randint(self.min_value, self.max_value)
        equation = f"{var1} {operator} {var2} = {constant}"
        return equation

    def gen_math(self, equation):
        """
        生成 plain TeX 格式的公式代码
        :param equation: 数学公式（字符串）
        :param equation_number: 公式编号（整数）
        :return: plain TeX 格式的公式代码
        """
        tex_code = f"{equation}"
        return tex_code


if __name__ == '__main__':
    test_any_box_rule = AnyBoxRule()
    # 测试随机生成 box
    print("Random Box:")
    print(test_any_box_rule.any_box())

    # 测试随机生成 rule
    print("\nRandom Rule:")
    print(test_any_box_rule.any_rule())

    # 测试随机生成 box 和 rule 的组合
    print("\nRandom Box with Rule:")
    print(test_any_box_rule.any_box_rule())


class RandomMathFormulaGenerator:
    def __init__(self, max_terms=5):
        """
        初始化随机数学公式生成器
        :param max_terms: 每行最大项数（默认 5）
        """
        self.max_terms = max_terms

    def generate_term(self):
        """
        生成随机数学项（数字、符号或表达式）
        :return: 随机生成的数学项
        """
        # 随机生成数字、符号或表达式
        choices = [
            str(random.randint(0, 9)),  # 数字
            random.choice(['+', '-', '\\times', '\\div']),  # 符号
            random.choice(string.ascii_letters),  # 字母
            f"\\frac{{{random.randint(1, 9)}}}{{{random.randint(1, 9)}}}",  # 分数
            f"\\sqrt{{{random.randint(1, 9)}}}"  # 平方根
        ]
        return random.choice(choices)

    def gen_formula(self):
        """
        生成随机数学公式
        :param num_lines: 公式的行数（默认 3）
        :return: 符合 plain TeX 语法的数学公式
        """
        formula = []
        for _ in range(3):
            # 随机生成每行的项数
            num_terms = random.randint(1, self.max_terms)
            line = []
            for _ in range(num_terms):
                line.append(self.generate_term())
            # 随机选择一个对齐点（用 & 标记）
            if len(line) > 1:
                align_pos = random.randint(0, len(line) - 1)
                line[align_pos] = f"& {line[align_pos]}"
            formula.append(" ".join(line))
        # 将公式转换为 plain TeX 语法
        tex_formula = " \\cr\n".join(formula) + "\n"
        return tex_formula
    


class AlignedFormulaGenerator:
    def __init__(self, max_formulas=5):
        """
        初始化公式生成器
        :param max_formulas: 最大公式行数（默认 5）
        """
        self.max_formulas = max_formulas

    def generate_expression(self):
        """
        生成随机数学表达式
        :return: 随机生成的数学表达式
        """
        # 随机生成数字、变量或运算符
        options = [
            str(random.randint(0, 9)),  # 数字
            random.choice(string.ascii_lowercase),  # 变量
            random.choice(['+', '-', '\\times', '\\div'])  # 运算符
        ]
        return random.choice(options)

    def gen_formula1(self, with_number=True, tex_formula=''):
        """
        生成随机对齐公式
        :param with_number: 是否为公式添加编号
        :return: 符合 plain TeX 语法的对齐公式
        """
        # 随机生成公式行数
        num_formulas = random.randint(1, self.max_formulas)

        # 生成公式内容
        formulas = []
        for i in range(num_formulas):
            left = self.generate_expression()  # 左边表达式
            right = self.generate_expression()  # 右边表达式
            formula = f"{left} = {right}"  # 使用 = 对齐
            formulas.append(formula)

        # 构建 plain TeX 公式
       
        for i, formula in enumerate(formulas):
            if with_number:
                print(tex_formula)
                tex_formula += f"  {formula} & ({i+1})\\cr\n"  # 添加编号
            else:
                tex_formula += f"  {formula} \\cr\n"  # 无编号
     
        return tex_formula
    



class RandomFormulaGenerator:
    def __init__(self, min_lines=1, max_lines=5):
        """
        初始化公式生成器
        :param min_lines: 最小行数（默认 1）
        :param max_lines: 最大行数（默认 5）
        """
        self.min_lines = min_lines
        self.max_lines = max_lines

    def generate_formula2(self):
        """
        随机生成一个公式
        :return: 随机生成的公式
        """
        # 随机生成公式类型
        formula_types = [
            lambda: f"{random.randint(1, 9)} + {random.randint(1, 9)} = {random.randint(2, 18)}",  # 加法
            lambda: f"{random.randint(1, 9)} - {random.randint(1, 9)} = {random.randint(-8, 8)}",  # 减法
            lambda: f"{random.randint(1, 9)} \\times {random.randint(1, 9)} = {random.randint(1, 81)}",  # 乘法
            lambda: f"\\frac{{{random.randint(1, 9)}}}{{{random.randint(1, 9)}}}",  # 分数
            lambda: f"\\sqrt{{{random.randint(1, 9)}}}",  # 平方根
            lambda: f"({random.randint(1, 9)} + {random.randint(1, 9)})^2",  # 平方
        ]
        return random.choice(formula_types)()

    def gen_formula_block(self):
        """
        生成多行公式，用 \cr 分隔
        :return: 符合 plain TeX 语法的公式块
        """
        num_lines = random.randint(self.min_lines, self.max_lines)
        formulas = [self.generate_formula2() for _ in range(num_lines)]
        return " \\cr\n".join(formulas)
    





class RandomPiecewiseFunctionGenerator:
    def __init__(self, min_value=0, max_value=10):
        """
        初始化分段函数生成器
        :param min_value: 条件的最小值（默认 0）
        :param max_value: 条件的最大值（默认 10）
        """
        self.min_value = min_value
        self.max_value = max_value

    def generate_condition(self):
        """
        生成随机条件
        :return: 随机条件（字符串）
        """
        operators = ["<", ">", "<=", ">=", "="]
        variable = "x"
        value = random.randint(self.min_value, self.max_value)
        operator = random.choice(operators)
        return f"{variable} {operator} {value}"

    def generate_result(self):
        """
        生成随机结果
        :return: 随机结果（字符串）
        """
        return str(random.randint(self.min_value, self.max_value))

    def gen_piecewise_function(self):
        """
        生成分段函数
        :param num_pairs: 条件-结果对的数量
        :return: 符合 plain TeX 语法的分段函数
        """
        pairs = []
        for _ in range(3):
            condition = self.generate_condition()
            result = self.generate_result()
            pairs.append(f"{condition} & {result}")
        return " \\cr\n".join(pairs)



class RandomMacroGenerator:
    def __init__(self, min_params=0, max_params=3, min_content_length=1, max_content_length=5):
        """
        初始化宏生成器
        :param min_params: 最小参数数量（默认 0）
        :param max_params: 最大参数数量（默认 3）
        :param min_content_length: 定义内容最小长度（默认 1）
        :param max_content_length: 定义内容最大长度（默认 5）
        """
        self.min_params = min_params
        self.max_params = max_params
        self.min_content_length = min_content_length
        self.max_content_length = max_content_length

    def generate_macro_name(self):
        """
        生成随机宏名称
        :return: 随机生成的宏名称
        """
        # 随机生成宏名称
        prefix = random.choice(["my", "custom", "new", "define"])
        suffix = random.choice(["command", "macro", "func", "var"])
        return f"\\{prefix}{suffix}"

    def generate_parameter_text(self):
        """
        生成随机参数文本
        :return: 随机生成的参数文本
        """
        num_params = random.randint(self.min_params, self.max_params)
        params = [f"#{i+1}" for i in range(num_params)]
        return "".join(params)

    def generate_definition_content(self):
        """
        生成随机定义内容
        :return: 随机生成的定义内容
        """
        # 随机生成定义内容
        content_length = random.randint(self.min_content_length, self.max_content_length)
        content = []
        for _ in range(content_length):
            content.append(random.choice([
                f"Process parameter: {random.choice(['#1', '#2', '#3'])}",
                "Perform some operation",
                "Return a value",
                "Print a message"
            ]))
        return "\n  ".join(content)

    def gen_macro(self):
        """
        生成随机宏定义
        :return: 符合 plain TeX 语法的宏定义
        """
        macro_name = self.generate_macro_name()
        parameter_text = self.generate_parameter_text()
        definition_content = self.generate_definition_content()

        # 构建宏定义
        macro_definition = f"{macro_name}{parameter_text}{{\n  {definition_content}\n}}"
        return macro_definition


import random
from typing import List, Tuple


class ParshaperGenerator:
    def __init__(self,
                 max_lines: int = 10,
                 max_indent: float = 50.0,
                 base_width: float = 400.0,  # 假设基础行宽为400pt
                 indent_unit: str = 'pt',
                 width_unit: str = 'pt'):
        """
        初始化参数生成器

        :param max_lines: 最大生成行数 (N)
        :param max_indent: 最大缩进量
        :param base_width: 基础行宽 (相当于\hsize)
        :param indent_unit: 缩进单位 (pt/mm/em等)
        :param width_unit: 行宽单位
        """
        self.max_lines = max_lines
        self.max_indent = max_indent
        self.base_width = base_width
        self.indent_unit = indent_unit
        self.width_unit = width_unit

    def generate_line_params(self) -> Tuple[float, float]:
        """生成单行的缩进和行宽参数"""
        indent = round(random.uniform(0, self.max_indent), 2)
        width = round(self.base_width - indent, 2)
        return (indent, width)

    def generate_parshape(self,
                          fixed_line_count: int = None,
                          progressive: bool = False) -> str:
        """
        生成完整的\parshape命令

        :param fixed_line_count: 固定行数(N)，None则随机
        :param progressive: 是否生成递增缩进
        :return: \parshape命令字符串
        """
        # 确定行数
        N = fixed_line_count if fixed_line_count else random.randint(1, self.max_lines)

        params = []
        current_indent = 0.0

        for k in range(N):
            if progressive:
                # 渐进式缩进：每行比前一行增加随机缩进
                indent_step = random.uniform(0, self.max_indent / N)
                current_indent = round(min(current_indent + indent_step, self.max_indent), 2)
            else:
                # 完全随机缩进
                current_indent = round(random.uniform(0, self.max_indent), 2)

            width = round(self.base_width - current_indent, 2)
            params.extend([current_indent, width])

        # 转换为TeX格式
        param_strs = []
        for i, val in enumerate(params):
            # 每两个参数后换行（i从0开始计数）
            if i % 2 == 0 and i != 0:
                param_strs.append('\n' + ' ' * 11)  # 保持对齐
            param_strs.append(f"{val}{self.indent_unit if i % 2 == 0 else self.width_unit} ")

        # 构建完整命令
        command = f"\\parshape={N}\n" + ' ' * 11 + ''.join(param_strs).strip()
        return command

    @staticmethod
    def validate_parshape(params: List[float]) -> bool:
        """验证生成的参数是否有效"""
        if len(params) % 2 != 0:
            return False
        for i in range(0, len(params), 2):
            if params[i] + params[i + 1] > 500:  # 假设总宽度不超过500pt
                return False
        return True


import random
from typing import List


class EqalignGenerator:
    def __init__(self):
        self.variables = ['x', 'y', 'z', 'a', 'b', 'c']
        self.operators = ['+', '-', '\\times', '\\div']
        self.functions = ['\\sqrt', '\\sin', '\\cos', '\\log']
        self.max_depth = 3

    def generate_random_term(self, depth=0) -> str:
        """生成随机数学项"""
        if depth >= self.max_depth:
            return random.choice(self.variables + ['1', '2', '3', '4', '5'])

        choice = random.random()
        if choice < 0.3:
            # 生成分数
            return f"\\frac{{{self.generate_random_term(depth + 1)}}}{{{self.generate_random_term(depth + 1)}}}"
        elif choice < 0.6:
            # 生成函数
            func = random.choice(self.functions)
            arg = self.generate_random_term(depth + 1)
            return f"{func}{{{arg}}}" if func != '\\sqrt' else f"{func}{{{arg}}}"
        else:
            # 生成变量或数字
            return random.choice(self.variables + [str(random.randint(1, 9))])

    def generate_random_expression(self, side='left') -> str:
        """生成随机表达式"""
        lhs = self.generate_random_term()
        if side == 'left':
            return lhs

        rhs = self.generate_random_term()
        operator = random.choice(self.operators)
        return f"{lhs} {operator} {rhs}"

    def generate_eqalign(self, num_lines=3) -> str:
        """生成完整的eqalign环境"""
        lines = []
        for _ in range(num_lines):
            left_expr = self.generate_random_expression(side='left')
            right_expr = self.generate_random_expression(side='right')
            lines.append(f"  {left_expr} &= {right_expr} \\cr")

        return "\n" + "\n".join(lines) + "\n"


import random
from typing import List, Tuple


class ParshapeGenerator:
    def __init__(self):
        self.max_lines = 10  # 最大行数
        self.max_indent = 300  # 最大缩进（单位：pt）
        self.max_width = 500  # 最大行宽（单位：pt）
        self.common_units = ['pt', 'mm', 'cm', 'in']  # 常用单位

    def generate_random_length(self) -> str:
        """生成随机长度值（带单位）"""
        value = random.randint(0, self.max_width)
        unit = random.choice(self.common_units)
        return f"{value}{unit}"

    def generate_line_spec(self) -> Tuple[str, str]:
        """生成单行的缩进和宽度对"""
        indent = self.generate_random_length()
        width = self.generate_random_length()
        # 确保宽度不小于缩进
        while int(width[:-2]) < int(indent[:-2]):
            width = self.generate_random_length()
        return (indent, width)

    def generate_parshape(self, num_lines: int = None) -> str:
        """生成完整的\parshape命令"""
        if num_lines is None:
            num_lines = random.randint(1, self.max_lines)

        lines = []
        for _ in range(num_lines):
            indent, width = self.generate_line_spec()
            lines.append(f"{indent} {width}")

        return f"{num_lines} {' '.join(lines)}"


