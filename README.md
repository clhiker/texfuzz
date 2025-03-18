//
// Created by clhiker on 25-2-25.
//

/*
input: tex:300 (从文件读取，每行一条指令）
string: tex*tex 90k 指令，每条一行，
result.tex
tex 头
90k
tex 尾
system("tex result.tex")
finding bug
*/

//fork
//    subprocess
//    system()

## 分类码
- 转义字符；用于标记控制序列的开始。IniTeX 默认使用反斜线 \ 作为转义字符（ASCII 码为 92）。
- 分组开始符；TeX 遇到此类字符时，会进入新的一层分组。在 plain TeX 中，默认的分组开始符是左花括号 {。
- 分组结束符；TeX 遇到此类字符时，会关闭并从当前分组中退出。在 plain TeX 中，默认的分组开始符是左花括号 }。
- 数学切换符；此类字符是数学公式的左右定界符。在 plain TeX 中，默认的数学切换符是美元符号 $。
- 制表符；在 \halign（\valign）制作的表格中，作为列（行）间分隔符。在 plain TeX 中，默认的制表符是与符号 &。
- 行终止符；TeX 用来表达输入行结束的字符。IniTeX 将回车符 <return>（ASCII 编码为 13）作为默认的行终止符。这就是为什么 IniTeX 中，\endlinechar 的值是 13（详见前文）。
- 参数符；用于表示宏的参数。在 plain TeX 中，默认的参数符是井号 #。
- 上标符；在数学模式中表示上标；也可用于在输入文件中表示无法直接输入的字符（详见后文）。在 plain TeX 中，默认的上标符即是 ^。
- 下标符；在数学模式中表示下标。在 plain TeX 中，默认的下标符是下划线 _。
- 被忽略字符；此类字符将被 TeX 自输入流中清除，因此不会影响后续处理。在 plain TeX 中，默认将空字符 <null>（ASCII 编码为 0）设置为被忽略字符。
- 空格符；TeX 对待空格符的方式较为特殊。IniTeX 将空格 <space>（ASCII 编码为 32）作为默认的空格符。
- 字母；IniTeX 默认只将 a ... z 和 A ... Z 分为此类。在宏包中，某些「隐秘」字符（例如 @）会被暂时分为此类。
- 其他字符；IniTeX 将所有未归于其他类的字符归于此类。因此，数字和标点都属于此类。
- 活动字符；活动字符相当于一个无需转义字符前导的 TeX 控制序列。在 plain TeX 中，只有带子 ~ 是活动字符，表示不可断行的空格。
- 注释符；TeX 遇见注释符后，会将从注释符开始到输入行尾的所有内容视作注释而忽略。在 IniTeX 中，默认的注释符是百分号 %。
- 无效字符；该分类包含了不应在 TeX 中出现的字符。IniTeX 将退格字符（ASCII 编码为 127）<delete> 归于此类。

## 常见命令
- tex *.tex  编译tex
- xdvi *.dvi 查看dvi文件

- 
- "[^"]*":

# PlainTex 语法规则
### group 
group is everything after an opening brace and before the matching closing brace.
### token
A token is a character, a control sequence, or a group.
### control sequence
A control sequence is anything that begins with a . It is not printed as is, it is expanded by the TeX engine according to its type.\
### command
A command (or function or macro) is a control sequence that may expand to text, to (re)definition of control sequences, etc.
### primitive
A primitive is a command that is hard coded in the TeX engine, i.e. it is not written in Plain TeX.
### register
A register is the TeX way to handle variables. They are limited in numbers (256 for each type of register in classic TeX, 32767 in e-TeX).
### length
A length is a control sequence that contains a length (a number followed by a unit). See Lengths.
### font
A font is a control sequence that refers to a font file. See Fonts.
### box
A box is an object that is made for printing. Anything that ends on the paper is a box: letters, paragraphs, pages... See Boxes.
### glue
A glue is a certain amount of space that is put between boxes when they are being concatenated.
### counter
A counter is a register containing a number. See Counters.


### 数学模式


# 差分测试
## 差分项：[tectonic](https://github.com/tectonic-typesetting/tectonic)
tectonic 可以在plainTex 模式下，生成 xdv/pdf 等格式文件
```shell
tectonic -f plain seeds.tex
# xdv 模式
tectonic -f plain seeds.tex --outfmt xdv
```

## 对比工具
### diffpdf
linux 自带（apt）安装，但是匹配太严格

### diff-pdf
较为折中的方案
```shell
# 构建
sudo apt install make automake g++ libpoppler-glib-dev poppler-utils libwxgtk3.0-gt
k3-dev -y
git clone https://github.com/vslavik/diff-pdf.git
cd diff-pdf
./bootstrap
./configure
make
sudo make install
```
diff-pdf -v 1.pdf 2.pdf


## 差分命令
```shell
# 直接对比pdf
xetex -jobname=1 seeds.tex
tectonic -f plain seeds.tex && mv seeds.pdf 2.pdf
diff-pdf -v 1.pdf 2.pdf #（太过精确，容易报错）

# 转为图片对比图片
pdftoppm -png 1.pdf 1
pdftoppm -png 2.pdf 2
perceptualdiff 1-1.png 2-1.png
# 也可以直接对比 md5
md5sum 1-1.png
md5sum 2-1.png

# 查看图片基础信息
identify 2-1.png
identify 1-1.png
```

## 统一页面格式
```latex
% 设置页面尺寸（A4）
\hsize=210mm
\vsize=297mm
\pdfpagewidth=210mm
\pdfpageheight=297mm
% 设置字体（不一定需要）
\font\myfont=cmr12
\myfont
```