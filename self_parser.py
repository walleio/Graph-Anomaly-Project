import argparse

parser = argparse.ArgumentParser(description='OGBN-Arxiv (GNN)')
parser.add_argument('--seed', type=int, default=0)
parser.add_argument('--run', type=int, default=1000)
parser.add_argument('--stru', type=str, default='sage')
parser.add_argument('--epoch_times', type=int, default=50)
parser.add_argument('--ratio', type=float, default=0.1)
parser.add_argument('--dataset', type=str, default='ogbn-arxiv')
parser.add_argument('--ak', type=int, default=0)
parser.add_argument('--device', type=int, default=0)
parser.add_argument('--log_steps', type=int, default=1)
parser.add_argument('--use_sage', action='store_true')
parser.add_argument('--num_layers', type=int, default=3)
parser.add_argument('--hidden_channels', type=int, default=256)
parser.add_argument('--dropout', type=float, default=0.5)
parser.add_argument('--lr', type=float, default=0.01)
# changed from 500
parser.add_argument('--epochs', type=int, default=10)
parser.add_argument('--runs', type=int, default=10)
parser.add_argument('--dataset_name', type=str, default='arxiv_2023')
parser.add_argument('--llm_model', type=str, default='qwen')
args = parser.parse_args()

