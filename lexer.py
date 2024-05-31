from sly import Lexer


class Lexer(Lexer):
    # Set of token names. This is always required
    tokens = { 'SHOW', 'MATH', 'VCUBE', 'VRECTPR', 'SARECTPR', 'ARECT', 'CIRCIRCLE', 'ACIRCLE', 'VCYL', 'SACYL', 'VCONE', 'SACONE', 'BINARY', 'CHARACTER', 'LENGTH', 'ORDINAL', 'POWER', 'VSPH', 'FRADIUS', 'SASPH', 'SACUBE', 'BEN', 'VAR', 'IF', 'ELSE', 'ROUND', 'INPUT', 'ELIF', 'RANDOMINT', 'ENDIF', 'FUNC', 'ENDFUNC', 'CALL' }
    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'\>\>\>.*'
    
    literals = { '=' }
    # Regular expression rules for tokens
    SHOW = r'show\(.+\)+'
    
    MATH = r'math\([\d\.]+\s+?[\+|\-|\*|/|\%]\s+?[\d\.]+\)+'
    
    VCUBE = r'vcube\([\d\.]+\)+'
    
    VRECTPR = r'vrectpr\([\d\.]+,\s+?[\d\.]+,\s+?[\d\.]+\)+'
    
    SARECTPR = r'sarectpr\([\d\.]+,\s+?[\d\.]+,\s+?[\d\.]+\)+'
    
    ARECT = r'arect\([\d\.]+,\s+?[\d\.]+\)+'
    
    CIRCIRCLE = r'circircle\([\d\.]+\)+'
    
    ACIRCLE = r'acircle\([\d\.]+\)+'
    
    VCYL = r'vcyl\([\d\.]+,\s+?[\d\.]+\)+'
    
    SACYL = r'sacyl\([\d\.]+,\s+?[\d\.]+\)+'
    
    VCONE = r'vcone\([\d\.]+,\s+?[\d\.]+\)+'
    
    SACONE = r'sacone\([\d\.]+,\s+?[\d\.]+\)+'
    
    FRADIUS = r'fradius\([\d\.]+\)+'
    
    VSPH = r'vsph\([\d\.]+\)+'
    
    BINARY = r'binary\(.+\)+'
    
    CHARACTER = r'character\([\d\.]+\)+'
    
    LENGTH = r'length\(.+?\)+'
    
    ORDINAL = r'ordinal\(.+?\)+'
    
    POWER = r'power\([\d\.]+,\s+?[\d\.]+\)+'

    SASPH = r'sasph\((?:[\d\.])+\)+'

    SACUBE = r'sacube\([\d\.]+\)+'

    BEN = r'ben\(.+?\)+'
    
    VAR = r'var\([\w\d\.]+\s+?=\s+?.*\)+'

    IF = r'if ?.* ?[:!<>= ]= ?.* ?'

    ELSE = r'else'

    ROUND = r'round\([\d|\.]+,\s+?(\d|\.)+\)+'

    INPUT = r'input\(.+?\)+'

    ELIF = r'elif ?.* ?[:!<>= ]= ?.* ?'

    RANDOMINT = r'randomint\(.+,\s+.+\)+'

    ENDIF = r'endif'

    FUNC = r'func\(.+?\)+'

    ENDFUNC = r'endfunc'

    CALL = r'call\(.+?\)+'
