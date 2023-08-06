import os
import torch
from dataclasses import dataclass
from typing import Optional, Tuple, Dict, Any

@dataclass(kw_only=True)
class GlobalConfig:
    USE_CUDE_IF_AVAILABLE: bool = False
    SCREEN_SIZE: Optional[Tuple] = (800, 700)
    ENABLE_WANDB: Optional[bool] = False
    IN_FEATURES: int = 5
    REWARDS_PARENT_CONFIG_DIR: str = ".rewards_ai"
    REWARDS_CONFIG_MODEL_FOLDER_NAME: str = "session_saved_models"
    REWARDS_CONFIG_METRIC_FOLDER_NAME: str = "session_metrics"
    
    REWARDS_CONFIG_ENV_FILE_NAME : str = "environment_config"
    REWARDS_CONFIG_AGENT_FILE_NAME : str = "agent_config"
    REWARDS_CONFIG_TRAINING_FILE_NAME : str = "training_config"
    REWARDS_CONFIG_REWARD_FN_FILE_NAME : str = "reward_functions"
    

CONFIG = GlobalConfig()