import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


def calculate(num1: str, num2: str):
    first = int(num1, 2)
    second = int(num2, 2)
    standard = int('10000000000000000', 2)
    sum = first + second
    # rollback
    if sum >= standard:
        sum = sum - standard + 1
    return format(sum, '#018b')[2:]


def negate(num: str):
    return bin(((1 << 16) + (~int(num, 2))))[2:]


axLabel = plt.axes([0.3, 0.8, 0.5, 0.075])
num1 = TextBox(axLabel, 'num1')
axLabel = plt.axes([0.3, 0.7, 0.5, 0.075])
num2 = TextBox(axLabel, 'num2')
axLabel = plt.axes([0.3, 0.6, 0.5, 0.075])
num3 = TextBox(axLabel, 'num3')
axLabel = plt.axes([0.3, 0.3, 0.5, 0.075])
button = Button(axLabel, 'checksum')


def calculate_result(event):
    newLabel = plt.axes([0.3, 0.5, 0.5, 0.075])
    result = TextBox(newLabel, 'result', initial=negate(calculate(calculate(num1.text, num2.text), num3.text)))
    allnums = [num1.text, num2.text, num3.text, result.text]

    check_sum = calculate(allnums[0], allnums[1])
    for i in range(2, len(allnums)):
        check_sum = calculate(check_sum, allnums[i])
    check_sum = int(check_sum, 2)
    check_sum = bin(check_sum)[2:]
    axLabel = plt.axes([0.3, 0.4, 0.5, 0.075])
    checksum = TextBox(axLabel, 'checksum', initial=check_sum)
    if checksum.text == '1111111111111111':
        button.label.set_text('successful')
    else:
        button.label.set_text('unsuccessful')
    plt.show()


button.on_clicked(calculate_result)
plt.show()
