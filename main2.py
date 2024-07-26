import random
import sys
import threading
import time

points_inside_circle = list()

# lock = threading.Lock()

# dividing the point count by threads


def calc_points_inside_circle(numero_de_pontos):
    point_inside_circle = 0

    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distance_from_center = x**2 + y**2
        if distance_from_center <= 1:
            point_inside_circle += 1

    # with lock:
    points_inside_circle.append(point_inside_circle)


if __name__ == "__main__":

    n_points = int(sys.argv[1])
    n_threads = 8
    points_by_thread = n_points // n_threads

    threads_list = list()

    for _ in range(n_threads):
        thread = threading.Thread(
            target=calc_points_inside_circle, args=(points_by_thread,)
        )
        threads_list.append(thread)

    start_time = time.time()

    for thread in threads_list:
        thread.start()
    for thread in threads_list:
        thread.join()

    total_circle_points = sum(points_inside_circle)
    print("total_circle_points", total_circle_points)
    estimate_pi = 4 * total_circle_points / n_points

    end_time = time.time()

    print(f"Aproximação de π com {n_points} pontos é: {estimate_pi}")
    print(f"Tempo de execução: {end_time - start_time} segundos")
