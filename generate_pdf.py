#!/usr/bin/python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# data in a dictionary to be added to the pdf
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

# generates a simple report from the data in the dictionary
report = SimpleDocTemplate("/tmp/report.pdf")

# loads sample style sheet, crates a title
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit.", styles['h1'])

# creating a table of the fruit in a list of lists
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# adds the data to the report in a grid
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# creates a pie chart
report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels =[]
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
report_chart = Drawing()
report_chart.add(report_table)

# adds all data to the report
report.build([report_title, report_table, report_chart])