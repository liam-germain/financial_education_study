import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd

from matplotlib.backends.backend_pdf import PdfPages
import os
import tempfile

def create_bar_plot(data, column, title, filename):
    # Plot the bar plot using the binary column values (1s and 0s)
    bar_plot = data[column].plot(kind='bar', title=title)
    plt.ylabel('Count')
    plt.xlabel(column)
    # Save the plot to a file
    plt.savefig(filename)
    # Show the plot
    plt.show()

def create_pie_chart(data, column, title, filename):
    pie_chart = data[column].value_counts().plot(kind='pie', title=title, autopct='%1.1f%%')
    plt.savefig(filename)
    plt.clf()

def create_histogram(data, column, title, filename, bins=10):
    histogram = data[column].plot(kind='hist', bins=bins, title=title)
    plt.savefig(filename)
    plt.clf()

# Additional visualization functions can be added here
def create_age_histogram(data, column, title, file_name):
    # Create the histogram using the 'plot.hist' method
    age_histogram = data[column].plot.hist(bins=10, alpha=0.7)
    
    # Set the title of the histogram
    age_histogram.set_title(title)
    
    # Set the labels for the x-axis and y-axis
    age_histogram.set_xlabel('Age')
    age_histogram.set_ylabel('Frequency')
    
    # Save the histogram as an image file
    plt.savefig(file_name)
    
    # Show the histogram
    plt.show()
    
    
import re

def save_regression_summary_to_pdf(summary, filename):
    # Create a buffer to hold the summary text
    buf = StringIO()
    buf.write(summary.as_text())
    buf.seek(0)

    # Process the summary text to handle irregular spacing
    summary_lines = buf.readlines()
    
    print(f"Summary_lines for {filename}:")
    print(summary_lines)

    processed_lines = []
    row_labels = [
        "const",
        "How old are you?",
        "How would you rate your overall financial knowledge?",
        "How would you describe your risk tolerance?"
    ]

    for line in summary_lines:
        fields = []  # Initialize fields variable here
        for row_label in row_labels:
            if line.strip().startswith(row_label):
                fields = line.strip().split()
        if len(fields) >= 2:
            value = fields[-1]  # Use the last field as the value
            processed_lines.append((row_label, value))

    if not processed_lines:
        print(f"No data found in the regression summary for {filename}")
        return

    # Create a figure and axis to display the summary
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    ax.table(cellText=[[value] for row_label, value in processed_lines],
             colLabels=['Value'],
             rowLabels=[row_label for row_label, value in processed_lines],
             loc='center',
             cellLoc='left')

    # Save the figure to a PDF file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Regression summary saved to {filename}")

# visualization.py
import subprocess
from stargazer.stargazer import Stargazer



# def tex_to_pdf(tex_file, pdf_file):
#     try:
#         # Run the pdflatex command to generate the PDF
#         subprocess.run(['pdflatex', '-output-directory=output', '-jobname=regression_summary', tex_file], check=True)
#         print(f"PDF file created: {pdf_file}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error occurred while generating PDF: {e}")
#         return None
#     return pdf_file

def tex_to_pdf(tex_file, pdf_file):
    temp_dir = tempfile.mkdtemp()
    temp_tex = os.path.join(temp_dir, 'temp.tex')

    # Use standalone document class
    header = r"""\documentclass{standalone}
\usepackage{booktabs}
\begin{document}
"""
    footer = r"""\end{document}
"""
    with open(tex_file, 'r') as input_file:
        content = input_file.read()
    
    with open(temp_tex, 'w') as output_file:
        output_file.write(header + content + footer)

    # Print the LaTeX code being processed for debugging
    print(header + content + footer)

    try:
        subprocess.run(['pdflatex', '-output-directory', temp_dir, temp_tex], check=True)
        shutil.copy(os.path.join(temp_dir, 'temp.pdf'), pdf_file)
    finally:
        shutil.rmtree(temp_dir)

    return pdf_file



# def generate_regression_summary(fitted_models, output_filename):
#     # Create stargazer object with the list of fitted models
#     stargazer = Stargazer(fitted_models)

#     # Render the LaTeX code
#     latex_code = stargazer.render_latex()

#     # Add document class, necessary packages, and document environment
#     latex_code = (
#         "\\documentclass{article}\n"
#         "\\usepackage{booktabs}\n"  # Required for table formatting
#         "\\begin{document}\n"
#         "\\begin{center}\n"  # Add the center environment
#         + latex_code +
#         "\\end{center}\n"  # Close the center environment
#         "\\end{document}"
#     )

#     # Save the LaTeX code to a file
#     with open(output_filename, 'w') as f:
#         f.write(latex_code)

#     # Use the function tex_to_pdf to convert the .tex file to a .pdf file
#     tex_file = output_filename
#     pdf_file = tex_to_pdf(tex_file, 'output/regression_summary.pdf')

#     print("Regression summary saved to regression_summary.pdf")
#     return pdf_file




from stargazer.stargazer import Stargazer


def generate_regression_summary(fitted_models, output_filename):
    # Create Stargazer object with the list of fitted models
    stargazer = Stargazer(fitted_models)

    # Render the LaTeX code
    latex_code = stargazer.render_latex()
    print(latex_code)  # Add this line

    # Remove the table environment and replace with center environment
    latex_code = latex_code.replace("\\begin{table}", "\\begin{center}")
    latex_code = latex_code.replace("\\end{table}", "\\end{center}")

    # Add document class, necessary packages, and document environment
    latex_code = (
        "\\documentclass{standalone}\n"
        "\\usepackage{booktabs}\n"  # Required for table formatting
        "\\begin{document}\n"
        + latex_code +
        "\\end{document}"
    )

    # Create temporary directory and files
    with tempfile.TemporaryDirectory() as tempdir:
        tex_file = os.path.join(tempdir, 'temp.tex')
        pdf_file = os.path.join(tempdir, 'temp.pdf')

        # Save the LaTeX code to a file
        with open(tex_file, 'w') as f:
            f.write(latex_code)

        # Compile LaTeX to PDF
        os.system(f'pdflatex -output-directory={tempdir} {tex_file}')

        # Load PDF into matplotlib and save as PNG
        with PdfPages(pdf_file) as pdf_pages:
            for page_num in range(len(pdf_pages)):
                fig, ax = plt.subplots()
                ax.axis('off')
                ax.imshow(pdf_pages[page_num], cmap='gray')
                fig.savefig(f'{output_filename}_{page_num}.png', bbox_inches='tight')

    print("Regression summary saved to PNG files.")
    return [f'{output_filename}_{page_num}.png' for page_num in range(len(pdf_pages))]

# Example usage
# generate_regression_summary(fitted_models, 'output/regression_summary')












