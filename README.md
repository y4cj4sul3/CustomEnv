Custom Gym Environment
=
Usage
-
  Just import the package ```CustomEnv``` and here you go! <br>
Currently only ```HalfCheetahEx-v2``` is available, which is exactly the original ```HalfCheetah-v2```.
```python
import gym
import CustomEnv

env = gym.make('HalfCheetahEx-v2')
```    

Add new environment
-
To add new custom environment, you need to register your environment in the ```CustomEnv/__init__.py```.
For example,
```python
register(
  id='HalfCheetahEx-v2',
  entry_point='CustomEnv.mujoco:HalfCheetahEnv',
  max_episode_steps=1000,
  reward_threshold=4800.0,
)
```
- The ```id``` is the gym environment id used when calling ```gym.make```. Notice that it should not have the same id with the original gym environmants, or it will cause conflict. <br>
- ```entry_point = '<package_or_file>:<Env_class>'``` link to the environment. 

Custom MuJoCo environment
-
Under the ```mujoco``` folder, you can import your environment in ```__init__.py``` so that it's easier to register the environment. <br>
In the ```assets``` folder are the mujoco ```.xml``` file. When import these models, call ```mujoco_env.MujocoEnv.__init__``` with **absolute path**. Make sure that the path start with ```/```, otherwise it will use the library model. <br>
For instance,
```python
from gym import utils
from gym.envs.mujoco import mujoco_env
from os.path import dirname

class HalfCheetahEnv(mujoco_env.MujocoEnv, utils.EzPickle):
  def __init__(self):
    FILE_PATH = dirname(__file__) + '/assets/half_cheetah_Ex.xml'
    mujoco_env.MujocoEnv.__init__(self, FILE_PATH, 5)
    utils.EzPickle.__init__(self)

```

Reference
-
* [OpenAI Gym](https://github.com/openai/gym) <br>
  Actually this project is modified from ```gym/gym/env```, one can find it's architecture is similar to gym. 
* [Setting Up OpenAI Gym with MuJoCo](https://www.andrewszot.com/blog/machine_learning/reinforcement_learning/gym_with_mujoco)
