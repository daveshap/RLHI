# Reinforcement Learning with Heuristic Imperatives (RLHI)

This project aims to develop a reinforcement learning framework with heuristic imperatives to address the Control Problem in the context of large language models (LLMs). The goal is to create aligned LLMs that follow deontological and teleological ethics, improving their "instincts" or "intuition" regarding ethics, decisions, and alignment.

# Overview

We propose two RLHI models: a boolean discriminator model and a comparator model. These models will be used to create a "flywheel" of perpetual self-improvement in the LLMs.

The project is divided into three main phases:

1. Create JSONL files for the boolean and comparator models: This phase involves creating the necessary data files for training the boolean and comparator models.
2. Test the models against "standard candles": In this phase, we will evaluate the performance of the HI-aligned models using established LLM prompts to demonstrate their effectiveness.
3. Create new auto-labeled datasets and train new models: Using the trained boolean and comparator models, we will generate new datasets for reinforcement learning and train new LLMs to see if they can further improve discrimination.
