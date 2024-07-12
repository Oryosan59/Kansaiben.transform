import re
from flask import Flask, render_template, request

app = Flask(__name__)

def replace_text(input_text):
    # 標準語 -> 関西弁 の変換ルール
    transformations = {
        r'こんにちは': 'まいど',
        r'ありがとうございます': 'おおきに',
        r'おはようございます': 'おはようさん',
        r'こんばんは': 'ばんは',
        r'すみません': 'すんまへん',
        r'本当': 'ほんま',
        r'そうです': 'せやねん',
        r'違います': 'ちゃうねん',
        r'とても': 'めっちゃ',
        r'私': 'わて',
        r'あなた': 'あんさん',
        r'です。|だ。|である。': 'でんがな。',
        r'ます。': 'まんがな。',
        r'た。': 'たがな。',
    }
    
    replaced_text = input_text
    for pattern, replacement in transformations.items():
        replaced_text = re.sub(pattern, replacement, replaced_text)
    
    return replaced_text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        result = replace_text(input_text)
    return render_template('index.html', result=result, input=input_text)

if __name__ == '__main__':
    app.run(debug=True)
