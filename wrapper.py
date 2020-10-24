from .tools.benchmark.benchmark import Benchmark

config = {}

benchmark = Benchmark(args.target_device, args.number_infer_requests,
                              args.number_iterations, args.time, args.api_type)