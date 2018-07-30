from gym.envs.registration import register

# Mujoco
# ----------------------------------------

register(
  id='HalfCheetahEx-v2',
  entry_point='CustomEnv.mujoco:HalfCheetahEnv',
  max_episode_steps=1000,
  reward_threshold=4800.0,
)
