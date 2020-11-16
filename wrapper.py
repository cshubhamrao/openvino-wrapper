from openvino.inference_engine import IENetwork, IECore

from tools.benchmark.benchmark import Benchmark

args = {
    'device': 'CPU',
    'number_infer_requests': 4,  # TODO: replace with auto infer?
    'number_iterations': 1,  # TODO: refactor out of Benchmark class
    'duration_seconds': None,  # TODO: refactor out of Benchmark class
    'api_type': 'async',
    # 'path_to_model': 'face-detection-0204.xml'
}

config = {args['device']: {
    'CPU_THROUGHPUT_STREAMS': 'CPU_THROUGHPUT_AUTO'
}}
device = args['device']
if __name__ == '__main__':
    benchmark = Benchmark(**args)
    print(benchmark.get_version_info())
    benchmark.set_config(config)
    network = benchmark.read_network('face-detection-0204.xml')
    print(network.input_info['image'].input_data.shape)
    print(network.batch_size)
    exe_network = benchmark.load_network(network)
    print(len(exe_network.requests))
    # print(benchmark.ie.get_metric(device, 'SUPPORTED_CONFIG_KEYS'))


# class Wrapper(object):
#     def __init__(self, device='CPU', num_streams=8, api='async'):
#         self._model_loaded = False
#
#         self.device = device
#         self.nireq = num_streams
#         self.api = api
#         self.ie = IECore()
