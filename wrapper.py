from .tools.benchmark.benchmark import Benchmark

args = {
    'device': 'CPU',
    'number_infer_requests': 8,  # TODO: replace with auto infer?
    'number_iterations': 1,  # TODO: refactor out of Benchmark class
    'duration_seconds': None,  # TODO: refactor out of Benchmark class
    'api_type': 'async',
    'path_to_model': ''
}

config = {args['device']: {
    'CPU_THROUGHPUT_STREAMS': 'CPU_THROUGHPUT_AUTO'
}}
device = args['device']
if __name__ == '__main__':
    benchmark = Benchmark(**args)
    print(benchmark.get_version_info())
