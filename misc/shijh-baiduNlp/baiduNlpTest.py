from aip import AipNlp

APP_ID = '10437623'
API_KEY = 'Y1bwwQaaGZhcCW1aYl12cIeD'
SECRET_KEY = 'qMGZkOPiegiVVpyzh7AySBG2ubY0uY1V'
    
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

result = client.lexer('我想要下午去看一场银翼杀手')

print(type(result))
