from flask import Flask, render_template, request

app = Flask(__name__)

# Roman converter logic
def int_to_roman(num):
    if not 1 <= num <= 3999:
        return None

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['number']
        try:
            num = int(user_input)
            if 1 <= num <= 3999:
                roman = int_to_roman(num)
                return render_template('result.html',
                                       number_decimal=num,
                                       number_roman=roman,
                                       developer_name='Kutlu')
            else:
                return render_template('index.html',
                                       not_valid=True,
                                       developer_name='Kutlu')
        except:
            return render_template('index.html',
                                   not_valid=True,
                                   developer_name='Kutlu')
    else:
        return render_template('index.html',
                               not_valid=False,
                               developer_name='Kutlu')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
