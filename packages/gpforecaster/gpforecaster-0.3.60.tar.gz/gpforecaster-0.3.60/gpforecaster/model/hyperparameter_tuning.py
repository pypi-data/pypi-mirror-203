from typing import Tuple, Dict, List, Any
import gc
import random

from gpforecaster.model.gpf import GPF
from gpforecaster.utils.logger import Logger
from gpforecaster import __version__


def single_trial(dataset_name: str,
                 hierarchical_data: Dict[str, List],
                 hyperparameter_space: Dict[str, List[Any]],
                 gp_type: str) -> Tuple[float, Dict[str, Any]]:
    """
    Train a single GPF model with randomly sampled hyperparameters from the given hyperparameter space.

    Args:
        dataset_name (str): The name of the dataset.
        hierarchical_data (Dict[str, List]): The hierarchical data for the model.
        hyperparameter_space (Dict[str, List[Any]]): The hyperparameter space to sample from.
        gp_type (str): The type of Gaussian Process model to use (e.g., "exact").

    Returns:
        Tuple[float, Dict[str, Any]]: A tuple containing the validation loss and the hyperparameters used.
    """
    hyperparameters = {
        key: random.choice(values) for key, values in hyperparameter_space.items()
    }

    gpf = GPF(
        dataset=dataset_name,
        groups=hierarchical_data,
        inducing_points_perc=hyperparameters["inducing_points_percs"],
        gp_type=gp_type,
    )
    model, _ = gpf.train(
        lr=hyperparameters["learning_rates"],
        weight_decay=hyperparameters["weight_decays"],
        scheduler_type=hyperparameters["scheduler_types"],
        gamma_rate=hyperparameters["gamma_rates"],
        patience=hyperparameters["patiences"],
    )
    val_loss = gpf.val_losses[-1]
    del model
    del gpf
    gc.collect()

    return (val_loss, hyperparameters)


def hyperparameter_trials(num_trials: int,
                          dataset_name: str,
                          hierarchical_data: Dict[str, List],
                          hyperparameter_space: Dict[str, List[Any]],
                          gp_type: str) -> Tuple[float, Dict[str, Any]]:
    """
    Generator function that yields the result of each trial.

    Args:
        num_trials (int): The number of trials to perform.
        dataset_name (str): The name of the dataset.
        hierarchical_data (Dict[str, List]): The hierarchical data for the model.
        hyperparameter_space (Dict[str, List[Any]]): The hyperparameter space to sample from.
        gp_type (str): The type of Gaussian Process model to use (e.g., "exact").

    Yields:
        Tuple[float, Dict[str, Any]]: A tuple containing the validation loss and the hyperparameters used.
    """
    for trial in range(num_trials):
        yield single_trial(
            dataset_name, hierarchical_data, hyperparameter_space, gp_type
        )


def optimize_hyperparameters(dataset_name: str,
                             hierarchical_data: Dict[str, List],
                             num_trials: int,
                             gp_type: str = "exact") -> Dict[str, Any]:
    """
    Optimize hyperparameters using random search.

    Args:
        dataset_name (str): The name of the dataset.
        hierarchical_data (Dict[str, List]): The hierarchical data for the model.
        num_trials (int): The number of trials to perform.
        gp_type (str): The type of Gaussian Process model to use (e.g., "exact").

    Returns:
        Dict[str, Any]: The best set of hyperparameters found during optimization.
    """
    hyperparameter_space = {
        "learning_rates": (1e-2, 1e-3),
        "weight_decays": (1e-3, 1e-4, 1e-5),
        "scheduler_types": ("step", "exponential", "cosine", "none"),
        "gamma_rates": (0.1, 0.9, 0.95, 0.8),
        "inducing_points_percs": (0.75,),
        "patiences": (4, 6, 8, 10),
    }

    logger_tuning = Logger(
        "hyperparameter_tuning", dataset=f"{dataset_name}_hypertuning", to_file=True
    )
    results = []

    for trial, (val_loss, hyperparameters) in enumerate(
        hyperparameter_trials(
            num_trials, dataset_name, hierarchical_data, hyperparameter_space, gp_type
        )
    ):
        logger_tuning.info(
            f"Trial: {trial}, "
            f"Algorithm: gpf_{gp_type}, "
            f"Version: {__version__}, "
            f"Dataset: {dataset_name}, "
            f"Hyperparameters: {hyperparameters}, "
            f"Validation loss: {val_loss}"
        )
        results.append((val_loss, hyperparameters))

    best_hyperparameters = sorted(results, key=lambda x: x[0])
    logger_tuning.info(
        f"BEST -> "
        f"Algorithm: gpf_{gp_type}, "
        f"Version: {__version__}, "
        f"Dataset: {dataset_name}, "
        f"Best hyperparameters: {best_hyperparameters[1]}, "
        f"Validation loss: {best_hyperparameters[0]}"
    )

    print(
        f"BEST -> "
        f"Algorithm: gpf_{gp_type}, \n"
        f"Version: {__version__}, \n"
        f"Dataset: {dataset_name}, \n"
        f"Best hyperparameters: {best_hyperparameters[1]}, \n"
        f"Validation loss: {best_hyperparameters[0]}")

    return best_hyperparameters
