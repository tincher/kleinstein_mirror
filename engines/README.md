Engines
===

Welcome to the Engines folder of the Gem Stone Game Repository! This directory contains implementations of various game engines, some powered by traditional algorithms and others by advanced reinforcement learning techniques. Below, you'll find an overview of the engines available in this directory.

Overview
---

1. **Basic Algorithmic Engines:**
These engines are powered by traditional algorithms designed to play the Gem Stone game. They offer a range of strategies, from simple heuristic-based approaches to more complex decision-making algorithms.
  
2. **Reinforcement Learning (RL) Powered Engines:**
These engines utilize reinforcement learning techniques, including temporal difference learning, to play the Gem Stone game. They learn from experience, gradually improving their performance through interaction with the game environment.

Engine ideas
---

| Name | Idea |
|-----------------|-----------------|
| Count | Always do that move which results in the most stones on your side |
| Most |  Always do that move which starts with the most stones |
| Random | Take a random move |
| Steal | Always do that move which results in the enemy having the least stones (corresponds to Count) |
| TD | Use an MLP trained using temporal difference learning similar to [TD-Gammon](https://dl.acm.org/doi/10.1145/203330.203343) |


This readme was generated by ChatGPT, all other contents are created by me.