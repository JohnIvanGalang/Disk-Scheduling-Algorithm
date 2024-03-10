from rich.console import Console
from rich.table import Table
import os

console = Console()

table = Table(title="Round Robin", style="bold white")
table.add_column("Process Id", style="bold cyan", justify="center")
table.add_column("Arrival Time", style="bold cyan", justify="center")
table.add_column("Burst Time", style="bold cyan", justify="center")
table.add_column("Priority", style="bold cyan", justify="center")

ID_list = []
AT_list = []
BT_list = []
PR_list = []


os.system("cls")
user = int(input("Number of Process: "))

for i in range(user):
    processID = str(input("Process ID: "))
    ID_list.append(processID)

    arrivalTime = str(input("Arrival Time: "))
    AT_list.append(arrivalTime)
    
    burstTime = str(input("Burst Time: "))
    BT_list.append(burstTime)
    
    priority = str(input("Priority lvl: "))
    PR_list.append(priority)
    console.rule(style="white on bold", characters="-")

    
    table.add_row(processID, arrivalTime, burstTime, priority)
print("Process ID List:", ID_list)
print("Arrival Time List:", AT_list)
print("Burst Time List:", BT_list)
print("Priority List:", PR_list)

console.rule(style="white on bold", characters="-")

console.print(table)
