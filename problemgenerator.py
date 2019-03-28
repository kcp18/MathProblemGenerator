import os

from random import Random
from datetime import date

class ProblemGenerator(object):
    def __init__(self):
        self.r_instance = Random()

    def generate_ones(self):
        r = self.r_instance
        x = r.randint(1, 9)
        i = r.randint(1, 9)

        problem = (x, i)
        answer = (x * i, )

        return (problem, answer)

    def generate_tens(self):
        r = self.r_instance
        x = r.randint(0, 9)
        y = r.randint(1, 9) if x == 0 else r.randint(0, 9)
        xy = (x * 10) + y

        i = r.randint(1, 9) if xy < 10 else r.randint(0, 9)
        j = r.randint(1, 9) if i == 0 else r.randint(0, 9)
        ij = (i * 10) + j

        problem = (xy, ij)
        answer = (xy * ij, )

        return (problem, answer)

    def generate_hundreds(self):
        r = self.r_instance
        xyz = r.randint(1, 999)
        ijk = r.randint(100, 999) if xyz < 100 else r.randint(1, 999)

        problem = (xyz, ijk)
        answer = (xyz * ijk, )

        return (problem, answer)


    def _generate_ns(self, digit):
        problem_answer = None

        if digit == 'ones':
            problem_answer = self.generate_ones()
        if digit == 'tens':
            problem_answer = self.generate_tens()
        if digit == 'hundreds':
            problem_answer = self.generate_hundreds()

        return problem_answer

    def get_problemset(self, num=10, digit='ones'):
        solution_dict = {}
        count = 0
        while count < num:
            s_tuple = self._generate_ns(digit)
            if solution_dict.get(s_tuple[0]) == None:
                solution_dict[s_tuple[0]] = s_tuple[1]
                count += 1

        return solution_dict

    def default_problemset(self):
        default_pset = {}

        ones_pset = self.get_problemset(3, 'ones')
        tens_pset = self.get_problemset(4, 'tens')
        huns_pset = self.get_problemset(3, 'hundreds')

        default_pset.update(ones_pset)
        default_pset.update(tens_pset)
        default_pset.update(huns_pset)

        return default_pset

    def write_problemset(self, pset=None):
        if pset == None:
            pset = self.default_problemset()

        t = date.today()

        pset_name = 'pset_%s-%s-%s.txt' % (t.year, t.month, t.day)
        answ_name = 'answer-' + pset_name

        pset_path = os.path.join(os.getcwd(), pset_name)
        ans_path = os.path.join(os.getcwd(), answ_name)

        with open(pset_path, 'w') as pset_f, open(ans_path, 'w') as ans_f:
            num = 1
            for problem, answer in pset.items():
                prob_str = '%d. %d x %d' % (num, problem[0], problem[1])
                ans_str = '%d. %d' %(num, answer[0])
                num += 1

                pset_f.write(prob_str + '\n\n')
                ans_f.write(ans_str + '\n\n')

if __name__ == '__main__':
    p = ProblemGenerator()
    p.write_problemset()
