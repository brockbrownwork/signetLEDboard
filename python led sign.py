from pyperclip import copy
import datetime
from openpyxl import load_workbook

workbook = load_workbook(filename = "PPH CALC.xlsx", data_only = True)
sheet = workbook.active
cells = []
pph = {}
team_members = {}
pieces_goal = {}
pieces_done = {}
pieces_left = {}

row = 5
value = sheet[f"A{row}"].value
while str(value).isdigit():
    value = sheet[f"A{row}"].value
    cell = value
    cells.append(cell)
    pph[cell] = round(sheet[f"F{row}"].value, 2)
    pieces_goal[cell] = round(sheet[f"I{row}"].value)
    team_members[cell] = round(sheet[f"E{row}"].value)
    pieces_done[cell] = round(sheet[f"B{row}"].value)
    pieces_left[cell] = round(sheet[f"H{row}"].value)
    row += 1
cells.pop()

now = datetime.datetime.now()
hour = now.hour
if hour >= 13:
    hour = hour % 12
minute = now.minute
if len(str(minute)) == 1:
    minute = "0" + str(minute)

output = "Since {0}:{1}:\n".format(hour, minute)

for cell in cells:
    output += f'C{cell} PPH: {pph[cell]}\n'
    output += f'C{cell} goal: {pieces_goal[cell]}\n'
    output += f'C{cell}: {pieces_done[cell]} pcs\n'
    if pieces_left[cell] >= 0:
        output += f'C{cell}: {pieces_left[cell]} left\n'

print(cells)

output = output[:-1]

print(output)

copy(output)


