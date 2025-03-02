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

    def gen_any_glue(self, any_dimen):
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
        glue = any_dimen
        if include_plus:
            glue += f" plus {plus_length}cm"
        if include_minus:
            glue += f" minus {minus_length}cm"
        return glue


class AnyText:
    def __init__(self):
        self.out_char = ['\\', '{', '}', '$', '&', '%', '#', '/', '_', '^']       # #是数学模型不能用，其他未知

    def simple_string(self):
        # 定义所有可能的字符（包括字母、数字、标点符号等）
        characters = string.ascii_letters + string.digits + string.punctuation
        # 过滤掉反斜杠
        for key_char in self.out_char:
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