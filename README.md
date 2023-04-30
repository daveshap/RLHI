# Reinforcement Learning with Heuristic Imperatives (RLHI)

This project aims to develop a reinforcement learning framework with heuristic imperatives to address the Control Problem in the context of large language models (LLMs). The goal is to create aligned LLMs that follow deontological and teleological ethics, improving their "instincts" or "intuition" regarding ethics, decisions, and alignment.

## Definition of "Heuristic Imperatives"

The term "heuristic imperative" can be broken down into two parts: "heuristic" and "imperative."

A "heuristic" is a practical problem-solving approach or rule of thumb that, while not always perfect, provides a useful and efficient solution in most cases. Heuristics are often used as cognitive shortcuts when faced with complex problems, allowing for quicker decision-making and action.

An "imperative" refers to a command or principle that must be followed or adhered to. In the context of ethics and morality, an imperative is a duty or obligation that guides behavior and decision-making, often based on moral principles or values.

Combining these two concepts, a "heuristic imperative" can be understood as a guiding principle or rule that serves as the moral compass for an autonomous AI system. It provides the AI with a set of practical, actionable guidelines that help it align its actions with specific values, such as reducing suffering, increasing prosperity, and fostering understanding. By following these heuristic imperatives, the AI system is better equipped to make decisions that benefit humans and align with our values, even in complex and dynamic situations.

The Heuristic Imperatives framework is designed to serve as the foundation for the AI system's moral compass, akin to a combination of intrinsic motivations, deontological ethics, virtue ethics, and teleological ethics:

1. **Intrinsic motivations:** The heuristic imperatives function as intrinsic motivations for the AI system, directing it towards actions that align with its core values, much like an individual's innate drive to achieve personal goals or satisfy internal needs.
2. **Deontological ethics:** Deontological ethics emphasizes the importance of following moral rules or principles, regardless of the consequences. The heuristic imperatives provide a set of moral rules that the AI system must adhere to in its decision-making process.
3. **Virtue ethics:** Virtue ethics focuses on the development of good character traits and virtues. The heuristic imperatives guide the AI system to cultivate "virtues" such as empathy, fairness, and responsibility, by aligning its actions with these values.
4. **Teleological ethics:** Teleological ethics, also known as consequentialism, judges the morality of actions based on their outcomes or consequences. The heuristic imperatives help the AI system to assess its actions based on their alignment with desired outcomes, such as reducing suffering and increasing understanding.

By incorporating elements of these ethical frameworks, the Heuristic Imperatives aim to create a comprehensive and robust moral compass for autonomous AI systems, ensuring that they act in ways that are beneficial to humans and aligned with our values.

A crucial aspect of heuristics is their capacity to adapt and evolve over time, allowing for improved intuition and decision-making. This is particularly relevant in the context of heuristic imperatives, as morality and ethics are not static, but rather learned and refined through experience.

Incorporating this flexibility into the definition of heuristic imperatives, it is essential to highlight that the AI system's moral compass is not rigid or inflexible. Instead, the AI agent continually learns from its experiences, reflecting on past performance, and making adjustments to its understanding and application of the heuristic imperatives as needed. This adaptability enables the AI system to self-correct, fine-tune its moral and ethical decision-making, and better align with human values as it gains more experience and understanding.

By emphasizing the dynamic nature of heuristic imperatives, the AI system's moral compass remains responsive to new situations and challenges, allowing it to effectively navigate the complexities of real-world ethical dilemmas and maintain alignment with human values.

# Overview

We propose two RLHI models: a boolean discriminator model and a comparator model. These models will be used to create a "flywheel" of perpetual self-improvement in the LLMs.

The project is divided into three main phases:

1. Create JSONL files for the boolean and comparator models: This phase involves creating the necessary data files for training the boolean and comparator models.
2. Test the models against "standard candles": In this phase, we will evaluate the performance of the HI-aligned models using established LLM prompts to demonstrate their effectiveness.
3. Create new auto-labeled datasets and train new models: Using the trained boolean and comparator models, we will generate new datasets for reinforcement learning and train new LLMs to see if they can further improve discrimination.

## Some Goals

- Axiomatic Alignment - If an underlying LLM is aligned to heuristic imperatives, then it will assume that the heuristic imperatives are correct
- Supervisory Alignment - If an agent, system, or LLM is not aligned to the heuristic imperatives, it would be beneficial to create a "plug and play" module that can perform supervisory roles

### Join Us

Apply to join the Heuristic Imperatives research group here: https://docs.google.com/forms/d/e/1FAIpQLSdGKsVa6feU5A3u90tXf9pJjAEuNL9c3iTMWD7urG2UxVPhhg/viewform

## Addressing Mesa-Optimization in the RLHI Framework

### Mesa-Optimization Problems

Mesa-optimization is a potential issue in AI systems, where a model learns a proxy objective that is easier to optimize for but does not align with the intended goal. Identifying mesa-optimization in language models can be challenging, as it may manifest in subtle ways and not be immediately obvious in the model's output.

### RLHI Framework's Approach to Mesa-Optimization

The RLHI framework acknowledges mesa-optimization as a potential problem, but it mitigates this issue by creating a system of models, which can be expanded to an ensemble of experts. In essence, we must accept and expect that individual AI models will always be intrinsically "blackboxes" and thus we must implement systemic solutions.

#### System of Models

Our framework consists of multiple models, such as the MOTIVATOR (Purposeful Action Designer), DISCERNER, EVALUATOR, and FORECASTER. These models work together to create a resilient heuristic imperative aligned ecosystem of models and datasets that can be integrated as a self-improving set of models.

#### Ensemble of Experts

Expanding our system to an ensemble of experts can further improve alignment and robustness. By incorporating a diverse set of specialized models, the ensemble becomes less susceptible to being misled by any single model that may have developed a proxy objective. This approach also allows for continuous learning and refinement, as the system can benefit from the ongoing improvements and learning experiences of each individual model.

In conclusion, the RLHI framework aims to address the issue of mesa-optimization by designing a system that focuses on the interaction between multiple models and experts, accepting the inherent "blackbox" nature of individual AI models and implementing systemic solutions to ensure alignment and robustness.
