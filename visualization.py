import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import subprocess

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

def tex_to_pdf(tex_file, pdf_file):
    try:
        # Run the pdflatex command to generate the PDF
        subprocess.run(['pdflatex', '-output-directory=output', '-jobname=regression_summary', tex_file], check=True)
        print(f"PDF file created: {pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating PDF: {e}")
        return None
    return pdf_file

def generate_regression_summary(fitted_models):
    # Create stargazer object with the list of fitted models
    stargazer = Stargazer(fitted_models)

    # Render the LaTeX code
    latex_code = stargazer.render_latex()

    # Add document class, packages, and document environment
    latex_code = (
        "\\documentclass{article}\n"
        "\\usepackage{booktabs}\n"
        "\\begin{document}\n"
        + latex_code +
        "\\end{document}"
    )

    # Save the LaTeX code to a file
    with open('output/regression_summary.tex', 'w') as f:
        f.write(latex_code)

    tex_file = 'output/regression_summary.tex'
    pdf_file = tex_to_pdf(tex_file, 'output/regression_summary.pdf')
    print("Regression summary saved to regression_summary.pdf")

