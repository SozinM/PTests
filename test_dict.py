

class FormattedDict(dict):
    def __str__(self):
        print self.items()
        string = ''
        for key, value in self.items():
            tmpstr = ''
            if isinstance(value,dict):
                string += '%s:\n' % (tmpstr + key)
                while(isinstance(value,dict)):#thing to bypass recursion
                    tmpstr += '\t'
                    print value.items()
                    key, value = value.items()[0]#cause it is a list of tuples
                    string += '%s:\n' % (tmpstr+key)
                string += '\t%s\n' % (tmpstr+value)
            else:
                string += '%s:\n'% (key)
                string += '\t%s\n'%(value)
        return string



def main():
    print FormattedDict({ '1': { 'child': '1/child/value' }, '2': '2/value'})
if __name__ == '__main__': main()
