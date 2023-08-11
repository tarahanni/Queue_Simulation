# Queue_Simulation

## 1. Introduction
Facing long queues is a common occurrence in everyday life, whether it's waiting at the supermarket checkout, at the bank, or even queuing for an elevator. These queues are formed because service capabilities do not match service demand, resulting in delays for facility users (customers) seeking immediate service.

For many people, waiting in queues can be tiring and time-wasting, leading some to choose alternative options. This poses a significant challenge for companies, especially those in the service industry. To retain customers, implementing additional service facilities is important to reduce queue length. However, this approach can increase operational costs. Therefore, efficiency becomes very important. In this project, I will simulate a queuing system at a ticket counter.

## 2. Elements of Queuing

In a queuing scenario, two main participants are present: the customer and the server. Customers originate from a source. Upon reaching a service facility, they can commence service right away or wait in a queue if the facility is occupied. When a facility completes a service, it automatically serves a waiting customer (if any) from the queue. In the absence of a queue, the facility becomes idle until a new customer arrives.

For queue analysis purposes, customer arrivals are indicated by the time between successive customers (interarrival time), while the service process is defined by the time spent on each customer (service time).

## 3. Exponential Distribution
The exponential probability distribution is used to describe the time until the next customer arrives with the expected value 𝜆 and the time it takes the person at the counter to process a ticket request with the expected value μ. After the ticket has been issued, the customer leaves the waiting area.

$f_\lambda(x)=\frac{1}{\lambda} \exp \left(-\frac{x}{\lambda}\right)$

## 4. The M/M/1 queue
We will analyze the model with exponential interarrival times with mean 1/λ, exponential service times with mean 1/μ, and a single server. Customers are served in order of arrival.
We require that

$\rho=\frac{\lambda}{\mu}<1$

It means λ must be smaller than μ; otherwise, the queue length will explode. The quantity ρ is the fraction of time the server is working.

<img width="841" alt="Screenshot 2023-08-11 at 14 44 59" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/27f8027b-a655-4a61-b028-ccb080010013">

Model (M/M/1) is the simplest model to provide an overview of queuing cases. Single-counter ticket sales are an example of this model. Figure 1 describes the model(M/M/1). Ls or system length is the total number of customers in the system, whether they are still queuing or being served. Ws or time in the system is the time taken by the customer from entering the waiting line
to leaving the system. La is the queue length to describe the number of customers currently in the
waiting line. Thus, the time it takes the customer to queue is Wa.

- **Ls**: the average number of customers in the system
- **La**: the average number of customers in the queue
- **Ws**: the average time of arrival in the system
- **Wa**: the average waiting time of arrival


## 5. Simulation in Python
The queuing system witnessed at the ticket counter service facility entails customers encountering a choice between immediate service or waiting in line for their turn. If a customer must wait, they join a queue and remain in line until it's their turn to be served. Notably, the ticket counter operates with a single available server.
The first thing we will do in python is initialize the objects we will create using the ***__init__()*** method. The structure for writing the ***__init__()*** method in a class is as follows:

<img width="812" alt="Screenshot 2023-08-11 at 14 59 28" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/1d551dc0-70be-4292-9820-c17e8d5ae106">


since we are going to draw samples from an exponential distribution, we need the function ***numpy.random.exponential()***:

<img width="526" alt="Screenshot 2023-08-11 at 14 59 36" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/f7a92f86-fb91-46e7-82f9-2580b040639a">

We need to initialize an empty list to hold all data from customers because, in this simulation, we don't know how many customers in 120 minutes. And now, we will simulate the M/M/1 model with the following function:

<img width="476" alt="Screenshot 2023-08-11 at 14 59 42" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/c147225e-3df3-457d-b3f3-410edbe89d2f">

The above functions are used for later output, but the functions below are actual simulations and calculate customer arrival and service time for new customers.

<img width="921" alt="Screenshot 2023-08-11 at 14 59 48" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/3f475daf-24c6-4561-aa82-06f631298b82">

After calculating for new customers,we'll proceed to calculate key summary metrics like the average queue waiting time (Wa), the average overall waiting time (Ws), the counter's occupancy probability (ρ), among others. In an effort to enhance customer comfort during waiting, the operator plans to offer seating arrangements. To determine the required number of seats during the simulation period, we'll use average number of customers in the queue (La).

<img width="649" alt="Screenshot 2023-08-11 at 14 59 55" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/c2d8db37-4223-478d-ac0d-c1ffe87bf512">

We need the ***print()*** method to display the statistical summary results.

<img width="592" alt="Screenshot 2023-08-11 at 15 00 01" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/a3cba0d9-9ec0-48ff-820b-940983eb2d9f">

To generate the same random value every time it is called, we need the ***numpy.random.seed()*** method. We will simulate within 120 minutes, with three people expected to come in a minute and with four people expected to be served in a minute.

<img width="301" alt="Screenshot 2023-08-11 at 15 00 06" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/7b24f87a-6cd7-44a2-b970-f15de6cc61f8">

And the expected output will come out like this:

<img width="409" alt="Screenshot 2023-08-11 at 15 00 12" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/2cba1dce-5994-4535-ba7e-e9c865664f3d">

By performing the simulation above, the following results are obtained:
the simulation was carried out in 120 minutes or 2 hours; there were 401 customers who came to buy tickets. With this, we can conclude that the average person waiting is in the range of 1 to 2 minutes per person, and we also know that the operator requires at least six seats for customers waiting to be served.

We will enter a new number since we need to test with different λ and μ.

<img width="436" alt="Screenshot 2023-08-11 at 15 00 18" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/8eea5ec6-9601-445f-b677-e3b14545395e">

From the simulation above, we can conclude that in 120 minutes, 628 customers will buy tickets. Five customers arrive in one minute, and six customers are being served in one minute. We can also find out the operator needs seven seats in this simulation.

Then we will test with customers who come only one person in one minute, and the server can serve two customers in 1 minute.

<img width="415" alt="Screenshot 2023-08-11 at 15 00 22" src="https://github.com/tarahanni/Queue_Simulation/assets/135048214/f5a6571d-d5ac-4d20-b1b8-ec8f47bce543">

With this, we conclude that there will be no long queues. Therefore the operator only needs to prepare only one seat in this simulation.



