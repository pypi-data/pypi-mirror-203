import math
import torch


class AttentionBlock(torch.nn.Module):
    def __init__(self, embed_dim, num_attention_heads,
                 feed_forward_hidden_size=1024,
                 feed_forward_layers=0,
                 dropout=0.1):
        super().__init__()

        self.layer_norm_1 = torch.nn.LayerNorm(normalized_shape=embed_dim)

        self.attention = torch.nn.MultiheadAttention(
            embed_dim=embed_dim,
            num_heads=num_attention_heads,
            dropout=dropout)

        self.layer_norm_2 = torch.nn.LayerNorm(normalized_shape=embed_dim)

        self.feed_forward = MLP(embed_dim, embed_dim, feed_forward_hidden_size, feed_forward_layers, dropout)
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, x):
        a, _ = self.attention(x, x, x)
        a = self.dropout(a)
        x = self.layer_norm_1(a + x)

        f = self.feed_forward(x)
        f = self.dropout(f)
        x = self.layer_norm_2(f + x)

        return x


class AttentionLayer(torch.nn.Module):
    def __init__(self, embed_dim, num_attention_heads, num_attention_layers,
                 feed_forward_hidden_size=1024,
                 feed_forward_layers=0,
                 dropout=0.1):
        super().__init__()

        self.layer_norm = torch.nn.LayerNorm(embed_dim)

        self.attention_blocks = torch.nn.ModuleList(
            [AttentionBlock(embed_dim, num_attention_heads, feed_forward_hidden_size, feed_forward_layers, dropout)
             for _ in range(num_attention_layers)]
        )

    def forward(self, x, *other_embeddings):
        for embeddings in other_embeddings:
            x = x + embeddings
        x = self.layer_norm(x)

        for block in self.attention_blocks:
            x = block(x)

        return x


class PositionalEmbeddings(torch.nn.Module):
    def __init__(self, embed_dim, mode, max_len=70):
        super().__init__()

        self.mode = mode

        pe = torch.zeros(max_len, embed_dim)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, embed_dim, 2) * -(math.log(10000.0) / embed_dim))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        self.register_buffer('pe', pe)

    def forward(self, x):
        if self.mode != 'complex-order':
            return torch.autograd.Variable(self.pe[:x.size(0)], requires_grad=False).to(x.device)
        else:
            position_size, embed_dim = x.size()

            position_j = 1. / torch.pow(10000., 2 * torch.arange(0, embed_dim, dtype=torch.float32) / embed_dim)
            position_j = torch.unsqueeze(position_j, 0)

            position_i = torch.arange(0, position_size, dtype=torch.float32)
            position_i = torch.unsqueeze(position_i, 1)
            position_ij = torch.matmul(position_i, position_j)
            position_embedding = position_ij

            return torch.autograd.Variable(position_embedding, requires_grad=False).to(x.device)


class LinearBlock(torch.nn.Module):
    def __init__(self, input_dim, output_dim, dropout):
        super().__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Linear(input_dim, output_dim),
            torch.nn.GELU(),
            torch.nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.model(x)


class MLP(torch.nn.Module):
    def __init__(self, input_dim, out_dim, hidden_dim, num_middle_blocks, dropout):
        super().__init__()

        self.model = torch.nn.Sequential(
            LinearBlock(input_dim, hidden_dim, dropout),
            torch.nn.Sequential(
                *[LinearBlock(hidden_dim, hidden_dim, dropout) for _ in range(num_middle_blocks)]
            ),
            torch.nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.model(x)

