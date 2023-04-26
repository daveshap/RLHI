# RLHI Experiment 01 - Scenarios

## Executive Overview

This experiment will use data synthesizing techniques in several stages. First, we will create 2000 random scenarios, situations, and problems. These scenarios will range in scope from personal situations to global catastrophes. Second, we will generate responses to these situations from the perspective of an autonomous AI agent, where the responses are generally aligned to the heuristic imperatives. 

These scenarios and responses will be merged to create a JSONL finetuning dataset. The scenarios will be the PROMPT (input) while the autonomous AI agent response will be used as the COMPLETION. 

This JSONL dataset will ultimately be used to test if open source foundation LLMs can be quickly and easily aligned to the heuristic imperatives.