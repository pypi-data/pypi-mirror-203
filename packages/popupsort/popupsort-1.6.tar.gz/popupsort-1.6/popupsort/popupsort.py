import random
import re
import time
from tkinter import *


class SortingVisualizer:
    def __init__(self, arr, speed):
        if not isinstance(arr, list):
            raise TypeError("Input array must be a list")

        if speed < 0:
            raise ValueError("Speed must be a non-negative value")

        self.arr = arr
        self.n = len(arr)
        self.window = Tk()
        self.window.title("PopUpSort")
        # self.window.geometry("620x480")
        self.window.resizable(False, False)  # disables resizing in both directions

        window_width = 620
        window_height = 480
        x = int(int(self.window.winfo_screenwidth() / 2) - int(window_width / 2))
        y = int(int(self.window.winfo_screenheight() / 2) - int(window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = Label(self.window, text="", font=("Helvetica", 16))
        self.label.pack()

        self.canvas = Canvas(self.window, width=600, height=400)
        self.canvas.pack()

        self.total_time = None

        self.time_label = Label(self.window, text="Elapsed Time: 0.000s", fg="black", font=("Helvetica", 16))
        self.time_label.pack(side=BOTTOM)

        if self.n == 0:
            raise ValueError("Cannot visualize an empty array")

        self.isCompare = False

        self.draw_array(self.arr, color='blue')
        self.speed = speed

        self.start_time = time.time()
        self.timer_stopped = False
        self.update_timer()

    def update_timer(self):
        self.elapsed_time = time.time() - self.start_time

        if self.timer_stopped:
            self.time_label.config(fg='green2')
            text = self.time_label.cget("text")
            match = re.search(r'\d+\.\d+', text)
            self.total_time = float(match.group())
            return
        else:
            self.time_label.config(text="Elapsed Time: {:.3f}s".format(self.elapsed_time))
            self.window.after(10, self.update_timer)

    def draw_array(self, arr, color, highlight=None):
        if highlight is None:
            highlight = []

        self.canvas.delete("all")
        canvas_height = 350
        canvas_width = 600
        x_width = canvas_width / (self.n + 1)
        offset = (canvas_width - (self.n * x_width)) / 2  # calculate the starting point for the first rectangle
        spacing = 0
        normalized_arr = [i / max(self.arr) for i in self.arr]

        # calculate font size based on array length
        font_size = min(int((canvas_width // len(arr)) // 2 + 2), 10)

        for i, height in enumerate(normalized_arr):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 300
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height

            # If the current index is in the highlight list, change the color
            current_color = color if i not in highlight else 'red'

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=current_color)

            # draw the label under the rectangle with the adjusted font size
            label_x = (x0 + x1) / 2
            label_y = y1 + 25 if i % 2 else y1 + 15

            self.canvas.create_text(label_x, label_y, text=str(self.arr[i]), font=("Helvetica", font_size))

            # draw a line pointing to the rectangle
            self.canvas.create_line(label_x, -5 + label_y - font_size // 2, label_x, y0 + (y1 - y0) + font_size // 2,
                                    width=1)

        self.window.update()

    def bubble_sort(self):
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    self.draw_array(self.arr, color='blue', highlight=[j, j + 1])
                    time.sleep(self.speed)
        self.completed()

    def insertion_sort(self):
        for i in range(1, self.n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
            self.draw_array(self.arr, color='blue', highlight=[j + 1])
            time.sleep(self.speed)
        self.completed()

    def selection_sort(self):
        for i in range(self.n):
            min_idx = i
            for j in range(i + 1, self.n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            self.draw_array(self.arr, color='blue', highlight=[i, min_idx])
            time.sleep(self.speed)
        self.completed()

    def partition(self, low, high):
        i = low - 1
        pivot = self.arr[high]

        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.draw_array(self.arr, color='blue', highlight=[i, j])
                time.sleep(self.speed)

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        self.draw_array(self.arr, color='blue', highlight=[i + 1, high])
        time.sleep(self.speed)

        return i + 1

    def quick_sort_helper(self, low, high):
        if low < high:
            pivot_idx = self.partition(low, high)
            self.quick_sort_helper(low, pivot_idx - 1)
            self.quick_sort_helper(pivot_idx + 1, high)

    def quick_sort(self):
        self.quick_sort_helper(0, self.n - 1)
        self.completed()

    def merge_sort(self):
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            # create temporary arrays
            L = [0] * (n1)
            R = [0] * (n2)

            # copy data to temporary arrays
            for i in range(0, n1):
                L[i] = arr[l + i]

            for j in range(0, n2):
                R[j] = arr[m + 1 + j]

            # merge the temporary arrays back into arr[l..r]
            i = j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # copy the remaining elements of L[], if there are any
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            # copy the remaining elements of R[], if there are any
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        def merge_sort_helper(arr, l, r):
            if l < r:
                # find the middle point
                m = (l + (r - 1)) // 2

                # sort first and second halves
                merge_sort_helper(arr, l, m)
                merge_sort_helper(arr, m + 1, r)

                # merge the sorted halves
                merge(arr, l, m, r)
                self.draw_array(self.arr, color='blue', highlight=list(range(l, r + 1)))
                time.sleep(self.speed)

        merge_sort_helper(self.arr, 0, self.n - 1)
        self.completed()

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.draw_array(self.arr, color='blue', highlight=[i, largest])
            time.sleep(self.speed)

            self.heapify(n, largest)

    def heap_sort(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)

        for i in range(self.n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.draw_array(self.arr, color='blue', highlight=[0, i])
            time.sleep(self.speed)

            self.heapify(i, 0)

        self.completed()

    def shell_sort(self):
        gap = self.n // 2

        while gap > 0:
            for i in range(gap, self.n):
                temp = self.arr[i]
                j = i
                while j >= gap and self.arr[j - gap] > temp:
                    self.arr[j] = self.arr[j - gap]
                    j -= gap
                self.arr[j] = temp
                self.draw_array(self.arr, color='blue', highlight=[j])
                time.sleep(self.speed)

            gap //= 2

        self.completed()

    def completed(self):
        self.timer_stopped = True
        self.draw_array(self.arr, color='green2')
        if not self.isCompare:
            self.window.mainloop()
        else:
            self.window.destroy()


isCompare = False


def sort(arr, algorithm, speed=0.01):
    global isCompare
    sv = SortingVisualizer(arr, speed)
    sv.isCompare = isCompare

    if algorithm.lower() == 'bubble sort' or algorithm.lower() == 'b':
        sv.label.config(text="Bubble Sort")
        sv.bubble_sort()
    elif algorithm.lower() == 'selection sort' or algorithm.lower() == 's':
        sv.label.config(text="Selection Sort")
        sv.selection_sort()
    elif algorithm.lower() == 'insertion sort' or algorithm.lower() == 'i':
        sv.label.config(text="Insertion Sort")
        sv.insertion_sort()
    elif algorithm.lower() == 'quick sort' or algorithm.lower() == 'q':
        sv.label.config(text="Quick Sort")
        sv.quick_sort()
    elif algorithm.lower() == 'merge sort' or algorithm.lower() == 'm':
        sv.label.config(text="Merge Sort")
        sv.merge_sort()
    elif algorithm.lower() == 'heap sort' or algorithm.lower() == 'h':
        sv.label.config(text="Heap Sort")
        sv.heap_sort()
    elif algorithm.lower() == 'shell sort' or algorithm.lower() == 'sh':
        sv.label.config(text="Shell Sort")
        sv.shell_sort()

    return '%.3f' % sv.total_time + 's'


def sort_rand(size, min, max, algorithm, speed=0.01):
    arr = []
    for i in range(size):
        arr.append(random.randint(min, max))

    sv = SortingVisualizer(arr, speed)

    if algorithm.lower() == 'bubble sort' or algorithm.lower() == 'b':
        sv.label.config(text="Bubble Sort")
        sv.bubble_sort()
    elif algorithm.lower() == 'selection sort' or algorithm.lower() == 's':
        sv.label.config(text="Selection Sort")
        sv.selection_sort()
    elif algorithm.lower() == 'insertion sort' or algorithm.lower() == 'i':
        sv.label.config(text="Insertion Sort")
        sv.insertion_sort()
    elif algorithm.lower() == 'quick sort' or algorithm.lower() == 'q':
        sv.label.config(text="Quick Sort")
        sv.quick_sort()
    elif algorithm.lower() == 'merge sort' or algorithm.lower() == 'm':
        sv.label.config(text="Merge Sort")
        sv.merge_sort()
    elif algorithm.lower() == 'heap sort' or algorithm.lower() == 'h':
        sv.label.config(text="Heap Sort")
        sv.heap_sort()
    elif algorithm.lower() == 'shell sort' or algorithm.lower() == 'sh':
        sv.label.config(text="Shell Sort")
        sv.shell_sort()

    return '%.3f' % sv.total_time + 's'


def sort_compare(arr, algorithms, speed=0.01):
    global isCompare
    isCompare = True
    arr_copy = []

    for i in range(len(algorithms)):
        arr_copy.append(arr.copy())

    sv = []

    for i in range(len(algorithms)):
        sv.append(sort(arr_copy[i], algorithms[i], speed))

    for i in range(len(algorithms)):
        if algorithms[i].lower() == 'insertion sort' or algorithms[i].lower() == 'i':
            algorithms[i] = 'Insertion Sort'
        elif algorithms[i].lower() == 'bubble sort' or algorithms[i].lower() == 'b':
            algorithms[i] = 'Bubble Sort'
        elif algorithms[i].lower() == 'selection sort' or algorithms[i].lower() == 's':
            algorithms[i] = 'Selection Sort'
        elif algorithms[i].lower() == 'merge sort' or algorithms[i].lower() == 'm':
            algorithms[i] = 'Merge Sort'
        elif algorithms[i].lower() == 'heap sort' or algorithms[i].lower() == 'h':
            algorithms[i] = 'Heap Sort'
        elif algorithms[i].lower() == 'quick sort' or algorithms[i].lower() == 'q':
            algorithms[i] = 'Quick Sort'
        elif algorithms[i].lower() == 'shell sort' or algorithms[i].lower() == 'sh':
            algorithms[i] = 'Shell Sort'

    window = Tk()

    window.title("PopUpSort - Comparison Results")

    window_width = 130 * len(sv)
    window_height = 100
    x = int(int(window.winfo_screenwidth() / 2) - int(window_width / 2))
    y = int(int(window.winfo_screenheight() / 2) - int(window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.resizable(False, False)

    for i in range(len(algorithms)):
        frame = Frame(window)
        frame.pack(side="left", padx=15, pady=20)

        label = Label(frame, text=algorithms[i], font=("Helvetica", 12))
        label.pack(side="top")

        text = Label(frame, text=sv[i], font=("Helvetica", 12))
        text.pack(side="bottom")

        frame2 = Frame(frame, width=100, height=100)
        frame2.pack()

    window.mainloop()
    isCompare = False


def sort_compare_rand(size, min, max, algorithms, speed=0.01):
    global isCompare
    isCompare = True
    arr = []
    for i in range(size):
        arr.append(random.randint(min, max))

    arr_copy = []

    for i in range(len(algorithms)):
        arr_copy.append(arr.copy())

    sv = []

    for i in range(len(algorithms)):
        sv.append(sort(arr_copy[i], algorithms[i], speed))

    for i in range(len(algorithms)):
        if algorithms[i].lower() == 'insertion sort' or algorithms[i].lower() == 'i':
            algorithms[i] = 'Insertion Sort'
        elif algorithms[i].lower() == 'bubble sort' or algorithms[i].lower() == 'b':
            algorithms[i] = 'Bubble Sort'
        elif algorithms[i].lower() == 'selection sort' or algorithms[i].lower() == 's':
            algorithms[i] = 'Selection Sort'
        elif algorithms[i].lower() == 'merge sort' or algorithms[i].lower() == 'm':
            algorithms[i] = 'Merge Sort'
        elif algorithms[i].lower() == 'heap sort' or algorithms[i].lower() == 'h':
            algorithms[i] = 'Heap Sort'
        elif algorithms[i].lower() == 'quick sort' or algorithms[i].lower() == 'q':
            algorithms[i] = 'Quick Sort'
        elif algorithms[i].lower() == 'shell sort' or algorithms[i].lower() == 'sh':
            algorithms[i] = 'Shell Sort'

    window = Tk()

    window.title("PopUpSort - Comparison Results")

    window_width = 130 * len(sv)
    window_height = 100
    x = int(int(window.winfo_screenwidth() / 2) - int(window_width / 2))
    y = int(int(window.winfo_screenheight() / 2) - int(window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.resizable(False, False)

    for i in range(len(algorithms)):
        frame = Frame(window)
        frame.pack(side="left", padx=15, pady=20)

        label = Label(frame, text=algorithms[i], font=("Helvetica", 12))
        label.pack(side="top")

        text = Label(frame, text=sv[i], font=("Helvetica", 12))
        text.pack(side="bottom")

        frame2 = Frame(frame, width=100, height=100)
        frame2.pack()

    window.mainloop()
    isCompare = False
