import json

data = []
with open('c://Users//USER//OneDrive//文件//intern//graph-instruct_multi.jsonl') as f:
    for line in f:
        data.append(json.loads(line))




        from google.colab import drive
drive.mount('/content/drive')
os.chdir("drive/My Drive/Colab Notebooks")