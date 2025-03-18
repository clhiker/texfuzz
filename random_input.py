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
