class Prostokat:
    def prostokat(self, a, b):
        #print(a, isinstance(a, int), b, isinstance(b, int))
        if isinstance(a, int) and isinstance(b, int):
            i = 0
            p = ""
            if a == 0 or b == 0:
                return ''
            while i < a:
                if i == 0:
                    p = p + b*"*"
                    if a > 1:
                        p = p + "\n"
                elif i == a-1:
                    p = p + b*"*"
                else:
                    if b > 1:
                        p = p + "*"+(b-2)*" " + "*\n"
                    else:
                        p += '*' * b + '\n'
                i = i+1
            return p
        else:
            raise Exception("Typ musi miec warosc Int")