import os
import shutil
import subprocess
import glob
from platform import system
from subprocess import Popen, PIPE
from subprocess import TimeoutExpired
from tqdm import tqdm

import fuzzGen

class TexFuzz:
    def __init__(self, seeds_dir):
        self.character = {}
        self.debugging = {}
        self.file_io = {}
        self.fonts = {}
        self.seeds_dir = seeds_dir

    def gen_tex(self):
        pass

    def gen_multi_tex_text(self, seeds_num):
        if os.path.exists(self.seeds_dir):
            shutil.rmtree(self.seeds_dir)
        os.makedirs(self.seeds_dir)
        random_gen = fuzzGen.RandomGen()
        for i in tqdm(range(seeds_num)):
            with open(f'{self.seeds_dir}/{i}.tex', 'w') as f:
                f.write(
                    '\\hsize=210mm\n'
                    '\\vsize=297mm\n'
                    '\\pdfpagewidth=210mm\n'
                    '\\pdfpageheight=297mm\n')
                f.write('\\font\\myfont=cmr12 at 12pt \n')
                f.write(random_gen.random_gen())
                f.write('\\bye')

    def gen_tex_text(self):
        random_gen = fuzzGen.RandomGen()
        with open('seeds/test.tex', 'w') as f:
            f.write(
                    '\\hsize=210mm\n'
                    '\\vsize=297mm\n'
                    '\\pdfpagewidth=210mm\n'
                    '\\pdfpageheight=297mm\n')
            f.write('\\font\\myfont=cmr12 at 12pt \n')
            f.write(random_gen.random_gen())
            f.write('\\bye')


    def diff_testing(self):
        cmd_1 = ['/usr/bin/xetex', '-jobname=seeds/1', 'seeds/test.tex']
        try:
            ret_1 = subprocess.run(cmd_1, stdout=PIPE, stderr=PIPE)
            if ret_1.returncode != 0:
                print(ret_1.stderr.decode())
        except:
            print('err')

        cmd_2 = ['/usr/bin/tectonic', 'seeds/test.tex', '-f', 'plain' ]
        try:
            ret_2 = subprocess.run(cmd_2, stdout=PIPE, stderr=PIPE)
            if ret_2.returncode != 0:
                print(ret_2.stderr.decode())
        except:
            print('err')

        subprocess.run(['mv', 'seeds/test.pdf', 'seeds/2.pdf'], stdout=PIPE, stderr=PIPE)
        pngs = []
        for i in range(1, 3):
            cmd = ['/usr/bin/pdftoppm', '-png', 'seeds/%d.pdf' % i, 'seeds/%d' % i]
            subprocess.run(cmd, stdout=PIPE, stderr=PIPE)
            png_ones = glob.glob("seeds/%d-*.png" % i)
            png_ones = sorted(png_ones, key=lambda x: int(x.split('-')[1].split('.')[0]))
            pngs.append(png_ones)


        for i,j in zip(pngs[0], pngs[1]):
            cmd_diff = ['/usr/bin/perceptualdiff', str(i), str(j)]
            res_diff = subprocess.run(cmd_diff, stdout=PIPE, stderr=PIPE)
            if res_diff.returncode == 0:
                print('%s 与 %s 页pdf 内容一致' % (i,j))
            else:
                print(res_diff.stdout.decode())
                print(res_diff.stderr.decode())

        os.system('rm seeds/*')

    def fuzz_multi_tex(self):
        with open('out.log', 'w') as f:
            for name in tqdm(os.listdir(self.seeds_dir)):
                cmd = ['xetex', name]
                try:
                    res = subprocess.run(cmd, cwd=self.seeds_dir, stdout=PIPE, stderr=PIPE, timeout=5)
                    if res.returncode != 0:
                        f.write(name + '\n')
                        f.write(f'{res.returncode}\n')
                        f.write(res.stderr.decode() + '\n')
                        f.write(res.stdout.decode() + '\n')
                except TimeoutExpired as e:
                    f.write(f'{name}\n')

    def fuzz_tex(self):
        os.system('cd seeds && xetex test.tex')
        pass

if __name__ == '__main__':
    tex_fuzz = TexFuzz('multi-seeds')
    # tex_fuzz.gen_tex_text()
    tex_fuzz.gen_multi_tex_text(100)
    tex_fuzz.fuzz_multi_tex()
    # tex_fuzz.diff_testing()
    # tex_fuzz.fuzz_tex()