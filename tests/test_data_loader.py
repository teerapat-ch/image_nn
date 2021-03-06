import pytest
from core.args import TrainingConfig
from core.data_loader import data_loader_builder


@pytest.mark.slow
def test_data_loader_builder():
    config = TrainingConfig()

    loaders, sizes = data_loader_builder(config)
    assert sizes["train"] == 50000
    assert sizes["test"] == 5000

    data = loaders["train"].__iter__()
    print(data)
