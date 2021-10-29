import pyperclip

debug = False
cell_team_members = {}
cells_count = {}
cell_pph = {}

with open("cell team members.txt") as f:
    team_members_text = f.read()
for line in team_members_text.split("\n"):
    cell_number = int(line.split(":")[0])
    team_members = float(line.split(":")[1])
    cell_team_members[cell_number] = team_members

# figure out if it's friday
import datetime
weekday = datetime.datetime.today().weekday()


if weekday == 4: # if it's friday...
    hours = 7.25
else:
    hours = 8.25

# open up the data for the cells
with open("data.txt") as f:
    cell_data = f.read()
cell_data = cell_data.split('\n')


cells = list(cell_team_members.keys())
cells.sort()

for cell in cells:
    cell_pph[cell] = 0
    cells_count[cell] = 0


for line in cell_data:
    if line.lower().startswith("cell"):
        cell_stats = line.split('\t')
        cell = int(cell_stats[0][4:])
        cell_count = int(cell_stats[2])
        if cell not in cells_count:
            cells_count[cell] = cell_count
        else:
            cells_count[cell] += cell_count

cell_pph_needed = {}
cell_pieces_needed = {}
individual_pph = {}

now = datetime.datetime.now()
hour = now.hour
if hour >= 13:
    hour = hour % 12
minute = now.minute
if len(str(minute)) == 1:
    minute = "0" + str(minute)

output = "Since {0}:{1}:\n".format(hour, minute)

cells_done = 0
total_left = 0
print("Count for the cells:")
for cell in cells:
    cell_pph[cell] = round(cells_count[cell] / hours, 2)
    individual_pph[cell] = round(cell_pph[cell] / cell_team_members[cell], 2)
    if cell in (13, 14):
        cell_pph_needed[cell] = round(2 - individual_pph[cell], 2)
    else:
        cell_pph_needed[cell] = round(3 - individual_pph[cell], 2)
    pieces_needed = round(cell_pph_needed[cell] * hours * cell_team_members[cell])
    if pieces_needed < 0:
        pieces_needed = 0
    cell_pieces_needed[cell] = pieces_needed
    total_left += pieces_needed
    output += "Cell {0}: PPH {1}\n".format(cell, individual_pph[cell])
    if cell_pieces_needed[cell] <= 0:
        output += "C{0} done, {1}!\n".format(cell, cells_count[cell])
        cells_done += 1
    else:
        output += "Cell {0}: {1} left\n".format(cell, cell_pieces_needed[cell])
    print(cells_count[cell])
    if debug:
        print("Cell {0}: {1} done, PPH: {2}, PPH needed: {3}, pieces needed: {4}, indPPH: {5}".format(
            cell, cells_count[cell], cell_pph[cell], cell_pph_needed[cell], cell_pieces_needed[cell], individual_pph[cell]))
if cells_done > 0:
    output += "{0}/{1} cells done\n".format(cells_done, len(cell_pph))
output += "{0} to go!".format(total_left)

print("Team Members:")
for cell in cells:
    print (cell_team_members[cell])

print ("\n\n" + output)

pyperclip.copy(output)

input("Press enter to continue >")


    




