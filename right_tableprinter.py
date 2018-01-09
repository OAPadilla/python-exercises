# Table Printer (column right-justified)
# Automate The Boring Stuff Ch.6
# Oscar Padilla


# Formats and outputs table with columns right-justified
def print_table(table):
    col_width = [0] * len(table)
    for i in range(len(table)):
        maxlen = table[i][0]
        for j in range(len(table[0])):
            if len(table[i][j]) > len(maxlen):
                maxlen = table[i][j]
            col_width[i] = len(maxlen)

    new_table = ""
    for i in range(len(table[0])):
        for j in range(len(table)):
            new_table += table[j][i].rjust(col_width[j]) + " "
        new_table += '\n'
    print(new_table)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
