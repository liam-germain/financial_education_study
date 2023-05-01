import re

def modify_stargazer_output(input_path, output_path):
    # Read the original LaTeX code from the file
    with open(input_path, 'r') as f:
        latex_code = f.read()

    # Perform the necessary modifications
    latex_code = latex_code.replace('\\begin{tabular}{@{\\extracolsep{5pt}}lccc}', '\\begin{tabular}{|l|c|c|c|}')
    latex_code = latex_code.replace('\\cr \\cline{3-4}', '')
    latex_code = latex_code.replace('\\hline \\[-1.8ex]', '\\hline')
    latex_code = latex_code.replace('\\textit{Note:} & \\multicolumn{3}{r}{$^{*}$p$<$0.1; $^{**}$p$<$0.05; $^{***}$p$<$0.01}', '\\multicolumn{4}{|l|}{\\textit{Note:} $^{*}$p$<$0.1; $^{**}$p$<$0.05; $^{***}$p$<$0.01}')
    latex_code = latex_code.replace('\\end{tabular}', '\\hline\n\\end{tabular}')
    latex_code = latex_code.replace('\\multicolumn{3}{c}{', '\\multicolumn{3}{c|}{')
    latex_code = latex_code.replace('\\begin{table}[!htbp] \centering', '')
    latex_code = latex_code.replace('\\end{table}', '')

    # Add necessary packages and environment
    header = "\\documentclass{article}\n\\usepackage{adjustbox}\n\\usepackage{array}\n\\usepackage{calc}\n\\begin{document}\n"
    footer = "\\end{document}"

    latex_code = header + "\\begin{adjustbox}{max width=\\paperwidth-2cm,center}\n" + latex_code + "\\end{adjustbox}\n" + footer

    # Write the modified LaTeX code to the output file
    with open(output_path, 'w') as f:
        f.write(latex_code)



def save_latex_code(fitted_models, output_path):
    from stargazer.stargazer import Stargazer

    # Create stargazer object with the list of fitted models
    stargazer = Stargazer(fitted_models)

    # Render the LaTeX code
    latex_code = stargazer.render_latex()

    # Save the LaTeX code to a file
    with open(output_path, 'w') as f:
        f.write(latex_code)
