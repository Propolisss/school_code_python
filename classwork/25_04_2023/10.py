s = 'АБГДЕ БВ ВЖИ ГВЖДБ ДЖЗ ЕДЗК ЖЛ ЗЖЛ ИЖЛ КЗЛМ МЛ'
dic = {st[0] : st[1:] for st in s.split()}

def f(start, end):
    if start[-1] == end:
        return 'З' not in start and 'Ж' in start
    return sum(f(start + sub, end) for sub in dic[start[-1]])
print(f('А', 'Л'))