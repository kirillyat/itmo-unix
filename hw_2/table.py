def generate_latex_table(data):
    if not data:
        return ""

    latex = "\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n"
    latex += "\hline\n"

    for row in data:
        latex += " & ".join(str(cell) for cell in row) + " \\\\ \hline \n"

    latex += "\end{tabular}\n"

    return latex

table_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

latex_table = generate_latex_table(table_data)
print(latex_table)

with open('artifacts/table.tex', 'w') as file:
    file.write(latex_table)