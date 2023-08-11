
import numpy as np
import csv


class Simulation:
	def __init__(self,arrival_date,service_start_date,service_time):
		self.arrival_date = arrival_date
		self.service_start_date = service_start_date
		self.service_time = service_time
		self.service_end_date =	self.service_time +self.service_start_date
		self.wait = self.service_start_date - self.arrival_date

Customers=[]

#to take a sample using the exponential distribution
#generate lambd and mu
def interarrival(lambd):
	return np.random.exponential(1/lambd)
def service(mu):
	return np.random.exponential(1/mu)


#the main function to simulate M/M/1 queue.
def Queue(lambd, mu, end_time):
	t = 0
	arrival_date = 0

	#while-loop to start simulation
	while t < end_time:

		#Calculate Arrival date and service time for new customer
		arrival_date = arrival_date + interarrival(lambd)
		if len(Customers) == 0:
			service_start_date = arrival_date
		else:
			service_start_date= max(arrival_date,Customers[-1].service_end_date)
		service_time = service(mu)

		# create new customer
		Customers.append(Simulation(arrival_date, service_start_date, service_time))

		t = arrival_date

#----------------------------------

	#calculate summary statistics
	Waits=[c.wait for c in Customers]
	Mean_Wait=sum(Waits)/len(Waits)

	Total_Times=[c.wait+c.service_time for c in Customers]
	Mean_Time=sum(Total_Times)/len(Total_Times)

	Service_Times=[c.service_time for c in Customers]
	Mean_Service_Time=sum(Service_Times)/len(Service_Times)

	Utilisation=sum(Service_Times)/t

	Mean_peopleinQueue = round(Utilisation**2/ (1-Utilisation))


	#output summary statistics to screen
	print("")
	print("Summary results:")
	print("")
	print("Number of customers: ",len(Customers))
	print("Mean Service Time: ",Mean_Service_Time)
	print("Mean Wait: ",Mean_Wait)
	print("Mean Time in System: ",Mean_Time)
	print("Utilisation: ",Utilisation)
	print("Chairs needed: " , Mean_peopleinQueue)
	print("")

np.random.seed(10)
print(Queue(3,4,120))

#to output full dataset to csv
with open('QueueSimulation.csv', 'w') as csvfile:
	thewriter = csv.writer(csvfile)
	fieldnames= ['Customer', 'Arrival_Date', 'Wait', 'Service_Start_Date', 'Service_Time', 'Service_End_Date']
	thewriter.writerow(fieldnames)
	i = 0
	for customer in Customers:
		i = i + 1
		outrow = []
		outrow.append(i)
		outrow.append(customer.arrival_date)
		outrow.append(customer.wait)
		outrow.append(customer.service_start_date)
		outrow.append(customer.service_time)
		outrow.append(customer.service_end_date)
		thewriter.writerow(outrow)
	csvfile.close()



