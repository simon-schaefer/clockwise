import itertools
import pathlib

from .interface import time_dict

__all__ = ['print_timings', 'stream_timings', 'log_timings']


def stream_timings():
    global time_dict

    # Sort the timing dictionary so that the element with the largest cumulative time is at the top.
    timing_dict_sorted = dict(sorted(time_dict.items(), key=lambda item: sum(item[1]), reverse=True))
    overall_time = sum(itertools.chain(*timing_dict_sorted.values()))

    # Print timings, i.e. title string, descriptions and timed elements.
    output_str = "Timings\n"
    output_str += "ID" + " " * 40 + "#Measurements" + " " * 5 + "Mean" + " " * 10 + "Max" + " " * 11 + \
                  "Cumulative" + " " * 4 + "Percentage" + "\n"
    for key, runtimes in timing_dict_sorted.items():
        num_measurements = str(len(runtimes))
        mean = f"{(sum(runtimes) / len(runtimes)):.8f}s"
        max_ = f"{max(runtimes):.8f}s"
        cumulative = f"{sum(runtimes):.8f}s"
        percentage = f"{sum(runtimes) / overall_time * 100:.2f}%"

        timing_str = key + " " * (40 + 2 - len(key))
        timing_str += num_measurements + " " * (5 + 13 - len(num_measurements))
        timing_str += mean + " " * (10 + 4 - len(mean))
        timing_str += max_ + " " * (11 + 3 - len(max_))
        timing_str += cumulative + " " * (4 + 10 - len(cumulative))
        timing_str += percentage

        output_str += timing_str + "\n"

    return output_str


def print_timings():
    output_str = stream_timings()
    print(output_str)


def log_timings(file_name: pathlib.Path = 'timings.pkl'):
    global time_dict

    import pickle as pkl
    file_name.parent.mkdir(exist_ok=True, parents=True)
    with open(file_name, 'wb') as f:
        pkl.dump(time_dict, f)
