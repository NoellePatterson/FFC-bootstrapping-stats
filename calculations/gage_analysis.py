import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file_name = 'Final_Reference_Gages.csv'
file = pd.read_csv(file_name, sep=',')
gages_df = pd.DataFrame(file)
years = gages_df['TOTAL_YEARS']
classes = gages_df['NEW_CLASS']
x_pos = [index for index, _ in enumerate(years)]
colors = []
for val in classes:
    if val == 1:
        colors.append('#FFEB3B')
    if val == 2:
        colors.append('#0D47A1')
    if val == 3:
        colors.append('#80DEEA')  
    if val == 4:
        colors.append('#FF9800')
    if val == 5:
        colors.append('#F44336')
    if val == 6:
        colors.append('#8BC34A')
    if val == 7:
        colors.append('#F48FB1')
    if val == 8:
        colors.append('#7E57C2')
    if val == 9:
        colors.append('#C51162')

plt.bar(x_pos, years, color = colors)
plt.show()