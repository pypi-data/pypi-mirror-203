import os
from typing import Callable, List

from tqdm import tqdm

config_default_values = {"return_errors": False, "print_errors": True}


def param_list(exec_data):
    func = exec_data[0]
    chunk_id = exec_data[1]
    params = exec_data[2]
    operator = exec_data[3]
    config = exec_data[4]

    results = []
    errors = []
    for param in tqdm(params, desc=f"processing: - chunk_num[{str(chunk_id)}] pid[{str(os.getpid())}]"):
        try:
            if operator is None:
                results.append(func(param))

            if operator == "*":
                results.append(func(*param))

            if operator == "**":
                results.append(func(**param))


        except Exception as e:
            if config["print_errors"]:
                print(e)
            results.append(None)
            errors.append(e)
    return results, errors


def tfrq(func: Callable, params: List, operator=None, num_cores=None, config=None, custom_executor=None):
    import math
    from concurrent.futures import ProcessPoolExecutor
    import os

    if num_cores is None:
        num_cores = os.cpu_count()

    if config is None:
        config = config_default_values

    else:
        for cfg in config_default_values:
            if cfg not in config:
                config[cfg] = config_default_values[cfg]

    chunk_size = math.ceil(len(params) / num_cores)
    chunks = [params[i:i + chunk_size] for i in range(0, len(params), chunk_size)]
    print("Tfrq into", len(chunks), "Chunks for", num_cores, "cores.")
    if custom_executor:
        results = list(
            custom_executor.map(param_list,
                                [(func, chunk_num, chunk, operator, config) for chunk_num, chunk in enumerate(chunks)]))
    else:
        with ProcessPoolExecutor(max_workers=num_cores) as executor:
            results = list(
                executor.map(param_list,
                             [(func, chunk_num, chunk, operator, config) for chunk_num, chunk in enumerate(chunks)]))

    errors = []
    final_results = []
    for res in results:
        final_results.append(res[0])
        errors.append(res[1])

    final_results_flat = []
    for res_per_core in final_results:
        for res in res_per_core:
            if res is None:
                final_results_flat.append(None)
            else:
                final_results_flat.append(res)

    errors_flat = []
    for errs_per_core in errors:
        for err in errs_per_core:
            if err is None:
                errors_flat.append(None)
            else:
                errors_flat.append(err)

    if config["return_errors"]:
        return final_results_flat, errors_flat
    else:
        return final_results_flat
