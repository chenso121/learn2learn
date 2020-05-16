#!/usr/bin/env python3

"""
l2l.vision.benchmarks documentation.
"""

import os
import learn2learn as l2l

from collections import namedtuple
from .omniglot_benchmark import omniglot_tasksets

BenchmarkTasksets = namedtuple('BenchmarkTasksets', ('train', 'validation', 'test'))

_TASKSETS = {
        'omniglot': omniglot_tasksets
        }


def list_tasksets():
    """
    Output: 
    """
    return _TASKSETS.keys()


def get_tasksets(
    name,
    train_ways=5,
    train_samples=10,
    test_ways=5,
    test_samples=10,
    num_tasks=-1,
    root='~/data',
    device=None,
    **kwargs,
    ):
    """
    Pass
    """
    root = os.path.expanduser(root)

    if device is not None:
        raise NotImplementedError('Device other than None not implemented. (yet)')

    # Load task-specific data and transforms
    datasets, transforms = _TASKSETS[name](train_ways=train_ways,
        train_samples=train_samples,
        test_ways=test_ways,
        test_samples=test_samples,
        root=root,
        **kwargs,
    )
    train_dataset, validation_dataset, test_dataset = datasets
    train_transforms, validation_transforms, test_transforms = transforms

    # Instantiate the tasksets
    train_tasks = l2l.data.TaskDataset(
        dataset=train_dataset,
        task_transforms=train_transforms,
        num_tasks=num_tasks,
    )
    validation_tasks = l2l.data.TaskDataset(
        dataset=validation_dataset,
        task_transforms=validation_transforms,
        num_tasks=num_tasks,
    )
    test_tasks = l2l.data.TaskDataset(
        dataset=test_dataset,
        task_transforms=test_transforms,
        num_tasks=num_tasks,
    )
    return BenchmarkTasksets(train_tasks, validation_tasks, test_tasks)