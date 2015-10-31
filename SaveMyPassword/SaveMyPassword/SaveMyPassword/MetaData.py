import SaveMyPassword.Password, os

__meta = '..\%s\meta.data' %__package__

accounts = {}

if os.path.isfile(__meta):
    with open(__meta, 'r') as f:
        while True:
            line = f.readline()
            if line != '':
                Analysis(line)
            else:
                break
else:
    with open(__meta, 'w') as f:
        f.write('')

def Analysis(content):
    pass