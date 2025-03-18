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

    import random


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
            tex_matrix += " & ".join(row) + " \\\\\n"

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
