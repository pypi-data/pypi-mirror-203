from .agent import Agent 
from .trainer import QTrainer
from .models import LinearQNet
from .utils import (
    create_session, 
    create_folder_struct,
    delete_session, 
    add_dict_inside_session
)

from .config import CONFIG 
from typing import Callable, Optional
from rewards_envs import CarGame 

class RewardsWorkflow:
    def __init__(self, session_id : str, session_root_folder : Optional[str] = None) -> None:
        self.session_id = session_id
        self.session_root_folder = session_root_folder
        self.session_root_dir = create_folder_struct(
            dir=session_root_folder, 
            name = CONFIG['REWARDS_PARENT_CONFIG_DIR']
        )
        
        create_session(
            session_name = session_id, 
            session_root_dir=self.session_root_dir
        )

        self.env_config = None
        self.agent_config = None
        self.training_config = None 
    
    def register_env_parameters(self, env_config):
        env_config_dict = env_config.__dict__.copy() 
        add_dict_inside_session(
            session_id = self.session_id,
            configuration = env_config_dict, 
            config_name=CONFIG['REWARDS_CONFIG_ENV_FILE_NAME'], 
            session_root_folder=self.session_root_folder, 
            rewrite = True, multi_config=False 
        )
        self.env_config = env_config
        
    def register_agent_parameters(self, agent_config):
        agent_config_dict = agent_config.__dict__.copy() 
        add_dict_inside_session(
            session_id = self.session_id, 
            configuration=agent_config_dict, 
            session_root_folder=self.session_root_folder, 
            config_name=CONFIG['REWARDS_CONFIG_AGENT_FILE_NAME'],
            rewrite=True, multi_config=False 
        )
        self.agent_config = agent_config
    
    def register_training__parameters(self, training_tracks : int,  evaluation_tracks : int, num_episodes : int):
        training_params = {
            'traning_tracks' : training_tracks, 
            'evaluation_tracks' : evaluation_tracks, 
            'num_episodes' : num_episodes
        } 
        
        add_dict_inside_session(
            session_id = self.session_id, 
            configuration=training_params, 
            session_root_folder=self.session_root_dir, 
            config_name=CONFIG['REWARDS_CONFIG_TRAINING_FILE_NAME'], 
            rewrite=True, multi_config=False
        )

    def register_reward_function(self, reward_function : Callable, reward_function_name : str):
        ...  
    
    def train(self, env_track : int):
        raise NotImplementedError
    
    def evaluate(self, env_track : int, use_train_track : bool = False):
        raise NotImplementedError

    @property
    def delete_session(self):
        delete_session(
            session_id=self.session_id, 
            session_root_dir=self.session_root_folder
        ) 
        print("=> Session Deleted successfully")

    def push_to_s3(self, aws_session_id, aws_folder_id):
        """
        WORKFLOW:
        --------
        - First it will calculate the rewards for all the training envs 
        - Then it will calculate the rewards for all the evaluation envs 
        - Finally it will calculate all other factors from:
            - agent_params (neural network size)
            - time taken to complete the training 
        package all the information to a json and the model.pth 
        and send to AWS S3 
        """
        raise NotImplementedError
    