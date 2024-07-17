*Zero-shot prompting* means that the prompt used to interact with the model won't contain examples or demonstrations. The zero-shot prompt directly instructs the model to perform a task without any additional examples to steer it.

*Few-shot prompting* can be used as a technique to enable in-context learning where we provide demonstrations int he prompt to steer the model to better performance. The demonstrations serve as a conditioning for subsequent examples where we would like the model to generate a response.

*Chain-of-thought (CoT)* prompting enables complex reasoning capabilities through intermediate reasoning steps. You can combine it with few-shot prompting to get better results on more complex tasks that require reasoning before responding.

*Self-consistency* aims "to replace the naive greedy decoding used in chain-of-thought prompting". The idea is to sample multiple, diverse reasoning paths through few-shot CoT, and use the generations to select the most consistent answer. This helps to boost the performance of CoT prompting on tasks involving arithmetic and commonsense reasoning.

*Generated Knowledge Prompting* is a prompt engineering method that first prompts the LLM to generate useful knowledge related to the task, and then incorporate the knowledge into the prompt alongside the question or task description.

*Prompt chaining* is useful to accomplish complex tasks which an LLM might struggle to address if prompted with a very detailed prompt. In prompt chaining, chain prompts perform transformations or additional processes on the generated responses before reaching a final desired state. Prompt chaining is particularly useful when building LLM-powered conversational assistants and improving the personalization and user experience of your applications.

*Tree of Thoughts (ToT)*, a framework that generalizes over chain-of-thought prompting and encourages exploration over thoughts that serve as intermediate steps for general problem solving with language models. ToT maintains a tree of thoughts, where thoughts represent coherent language sequences that serve as intermediate steps toward solving a problem. This approach enables an LM to self-evaluate the progress through intermediate thoughts made towards solving a problem through a deliberate reasoning process. 

*Retrieval-Augmented Generation (RAG)* is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response.

*Directional Stimulus Prompting* proposes a new prompting technique to better guide the LLM in generating the desired summary.
A tuneable policy LM is trained to generate the stimulus/hint. Seeing more use of RL to optimize LLMs.

*ReAct Prompting* LLMs are used to generate both reasoning traces and task-specific actions in an interleaved manner.
Generating reasoning traces allow the model to induce, track, and update action plans, and even handle exceptions. The action step allows to interface with and gather information from external sources such as knowledge bases or environments.
The ReAct framework can allow LLMs to interact with external tools to retrieve additional information that leads to more reliable and factual responses.

*Multimodal CoT Prompting* incorporates text and vision into a two-stage framework. The first step involves rationale generation based on multimodal information. This is followed by the second phase, answer inference, which leverages the informative generated rationales.
