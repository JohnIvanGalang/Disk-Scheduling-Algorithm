from random import randint
from rich.console import Console
from rich.table import Table
from time import sleep
from os import system


console = Console()

# This is a Non-Preemtive Priotity Scheduling Program
# Round Robin nak nabutang kay ambot, wa ko na ayusa kay bayn maruba 
class RoundRobin:

    processList = []
    
    # Function to get the user input for processes
    def User_Input(self, Num_Process):
        for IDprocess in range(1, Num_Process + 1):
            tempList = []
            
            # Prompt for arrival time, burst time, and priority level
            arrivalTime = int(input(f"\nP{IDprocess} Arrival Time: "))
            burstTime = int(input(f"P{IDprocess} Burst Time: "))
            Priority = int(input(f"P{IDprocess} Priotiy lvl: "))
            
            tempList = [f"P{IDprocess}", arrivalTime, burstTime, Priority]
            
            self.processList.append(tempList)
    
    # Function that generates random input for processes
    def Random_Input(self, Num_Process):
        half = Num_Process // 2
        randomizer_limit = Num_Process + half
        
        for IDprocess in range(1, Num_Process + 1):
            tempList = []

            while True:
                arrivalTime = randint(0, randomizer_limit)
                
                if [_process for _process in self.processList if _process[1] == arrivalTime]:
                    pass
                else:
                    break

            burstTime = randint(1, 20)
            Priority = randint(1, Num_Process)
            
            tempList = [f"P{IDprocess}", arrivalTime, burstTime, Priority, 0 ]

            self.processList.append(tempList)

    # Execution of the Algorithm
    def Execute(self):
        table = Table(title="Non-Preemptive Priority Scheduling", style="bold white")
        table.add_column("Process ID", style="bold cyan", justify="center")
        table.add_column("Arrival Time", style="bold cyan", justify="center")
        table.add_column("Burst Time", style="bold cyan", justify="center")
        table.add_column("Priority Level", style="bold cyan", justify="center")

        for process in self.processList:
            table.add_row(process[0], str(process[1]), str(process[2]), str(process[3]))
        
        console.print(table)

        currentTime = 0
        ProcessComplete = []
        MemoryQueue = []

        print("\n\n--------Gantt Chart Simulation--------") # Simulation or displaying of process of the algorithm
        while len(ProcessComplete) < len(self.processList):
            for process in self.processList:
                if process[1] <= currentTime and process not in ProcessComplete and process not in MemoryQueue:
                    MemoryQueue.append(process)

            console.print(f"\nTimeframe {currentTime}")

            # Executed if there is no Process in the moment
            if not MemoryQueue:
                console.print(f"Running: None\n")
                console.rule(style="green", characters="-")
                sleep(1)
                currentTime += 1
                continue

            MemoryQueue.sort(key=lambda x: (x[3], x[1]))  # Sort by priority and arrival time
            
            current_process = MemoryQueue.pop(0) # pops the first elemnt stored in the memory queue
            ProcessComplete.append(current_process)
            currentTime += current_process[2]

            console.print(f"Running: {current_process[0]}")
            console.print(f"Burst Time: 0")
            console.print(f"Priority lvl: {current_process[3]}\n")
            console.rule(style="green", characters="-")
            sleep(1)


        totalWT = 0
        totalTT = 0

        for process in self.processList:
            turnarroundTime = currentTime - process[1]
            waitingTime = turnarroundTime - process[2]

            totalWT += waitingTime
            totalTT += turnarroundTime

        WT = totalWT / len(self.processList) # Waiting time
        TT = totalTT / len(self.processList) # Turnaround TIme

        table2 = Table(title="Results", style="bold white")
        table2.add_column("Process ID", style="bold cyan", justify="center")
        table2.add_column("Waiting Time", style="bold cyan", justify="center")
        table2.add_column("Turnaround Time", style="bold cyan", justify="center")

        for process in self.processList:
            waitingTime = currentTime - process[1] - process[2]
            turnarroundTime = waitingTime + process[2]
            table2.add_row(process[0], str(waitingTime), str(turnarroundTime))

        console.print(table2)

        console.print(f"WT average: {WT}")
        console.print(f"TT average: {TT}\n\n")


# Main Function of the program
def mainFunction():
    The_User = RoundRobin()

    Number_of_process = int(input("Number of process: "))
    print("\n\t[ 1 ] User Input ->")
    print("\t[ 2 ] random INput->")
    UR = int(input("\nUser or Random Input? >>  "))

    if UR == 1:
        The_User.User_Input(Number_of_process)
    elif UR == 2:
        The_User.Random_Input(Number_of_process)
        
    The_User.Execute()

# Entry point of the Non-Preemtive Algorithm Program
if __name__ == "__main__":
    system("cls")
    sleep(0.8)
    mainFunction()
