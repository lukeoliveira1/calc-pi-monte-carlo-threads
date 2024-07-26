import time
import random
import threading
import matplotlib.pyplot as plt

n_points_to_test = [1000, 10000, 100000, 1000000]

#################################################################
# without threads


def calcular_pi(numero_de_pontos):
    pontos_dentro_do_circulo = 0

    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distancia_ao_centro = x**2 + y**2
        if distancia_ao_centro <= 1:
            pontos_dentro_do_circulo += 1

    pi_aproximado = 4 * pontos_dentro_do_circulo / numero_de_pontos
    return pi_aproximado


estimate_pi_without_threads = []
times_without_threads = []

for i in range(4):
    numero_de_pontos = n_points_to_test[i]
    start_time = time.time()
    estimate_pi = calcular_pi(numero_de_pontos)
    end_time = time.time()

    estimate_pi_without_threads.append(estimate_pi)
    times_without_threads.append(end_time - start_time)

print("estimate_pi_without_threads", estimate_pi_without_threads)

#################################################################

# with threads
lock = threading.Lock()


def calc_points_inside_circle(numero_de_pontos):
    point_inside_circle = 0

    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distance_from_center = x**2 + y**2
        if distance_from_center <= 1:
            point_inside_circle += 1

    with lock:
        points_inside_circle.append(point_inside_circle)


times_with_threads = []
estimate_pi_with_threads = []

for i in range(4):
    points_inside_circle = list()

    n_points = n_points_to_test[i]
    n_threads = 4
    points_by_thread = n_points // n_threads

    threads_list = list()

    for _ in range(n_threads):
        thread = threading.Thread(
            target=calc_points_inside_circle, args=(points_by_thread,)
        )
        threads_list.append(thread)
        # thread.start()

    time_start = time.time()
    for thread in threads_list:
        thread.start()
    for thread in threads_list:
        thread.join()

    total_circle_points = sum(points_inside_circle)
    estimate_pi = 4 * total_circle_points / n_points
    estimate_pi_with_threads.append(estimate_pi)

    time_end = time.time()

    times_with_threads.append(time_end - time_start)

print("estimate_pi_with_threads", estimate_pi_with_threads)

#################################################################
# chart

plt.plot(
    n_points_to_test,
    times_without_threads,
    marker="o",
    label="Without Threads",
)
plt.plot(
    n_points_to_test,
    times_with_threads,
    marker="o",
    label="With Threads For Calc Circle Points Qnt.",
)
plt.xlabel("Qnt. Points")
plt.ylabel("Time (s)")
plt.xscale("log")
plt.xticks(n_points_to_test, n_points_to_test)
plt.title("Comparison of Execution Time - Estimate PI With And Without Threads ")
plt.legend()
plt.grid(True)
plt.show()
