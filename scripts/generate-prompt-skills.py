import os

skills = [
    {
        "name": "chain-of-thought",
        "description": "Implements step-by-step reasoning with Chain-of-Thought, Tree-of-Thought, and self-consistency techniques. Use for complex multi-step problems.",
        "tags": ["prompt", "reasoning", "chain-of-thought", "step-by-step", "llm"],
        "template": """# Chain-of-Thought

> Step-by-step reasoning techniques for complex problem-solving.

## Quick Start
```
Solve step by step:
A store has 120 apples. They sell 1/3 of them in the morning,
then 1/4 of the remaining in the afternoon. How many are left?

Step 1: Morning sales = 120 * 1/3 = 40 apples
Step 2: Remaining after morning = 120 - 40 = 80 apples
Step 3: Afternoon sales = 80 * 1/4 = 20 apples
Step 4: Final remaining = 80 - 20 = 60 apples
Answer: 60
```

## When to Use
- Math and logic problems
- Multi-step reasoning tasks
- Decision trees and planning
- Complex analysis with verification

## Techniques

### Chain-of-Thought (CoT)
Ask the model to reason step by step before answering.

### Tree-of-Thought (ToT)
Explore multiple reasoning branches in parallel, then evaluate.

### Self-Consistency
Generate multiple CoT paths, take majority vote as final answer.

### Least-to-Most
Break a complex problem into simpler sub-problems, solve sequentially.

## Dependencies
No additional libraries needed — works with any LLM chat interface.

## Examples
```
Q: If 5 workers can build a wall in 12 days,
how many days would 8 workers take?

Step 1: Find worker-days needed: 5 * 12 = 60 worker-days
Step 2: Divide by new workers: 60 / 8 = 7.5 days
Answer: 7.5 days
```

## Resources
- [Chain-of-Thought Paper (Wei et al.)](https://arxiv.org/abs/2201.11903)
- [Tree-of-Thought Paper (Yao et al.)](https://arxiv.org/abs/2305.10601)

## Validation
1. Model shows intermediate reasoning steps
2. Final answer is correct given the steps
3. Self-consistency improves accuracy across runs"""
    },
    {
        "name": "structured-output",
        "description": "Guides LLMs to produce structured, schema-validated JSON output with type safety and format constraints. Use for programmatic LLM integration.",
        "tags": ["prompt", "json", "structured-output", "schema", "parsing"],
        "template": """# Structured Output

> Getting reliable, schema-validated JSON from LLMs.

## Quick Start
```
Extract the following information as JSON:
"John Doe, 28 years old, john@example.com, lives in New York"

Respond ONLY with valid JSON:
{
  "name": "John Doe",
  "age": 28,
  "email": "john@example.com",
  "city": "New York",
  "is_adult": true
}
```

## When to Use
- API integrations requiring typed data
- Database record generation
- Form filling and data extraction
- Function calling / tool use

## Techniques

### Schema Definition
Define the exact JSON schema in the prompt with types and constraints.

### Format Enforcement
Use "Respond ONLY with valid JSON" to prevent extra text.

### Type Coercion
Specify exact types (string, number, boolean, array, null) for each field.

### Error Handling
Request JSON wrapped in ```json blocks for safe parsing.

## Dependencies
```python
import json
# Use json.loads() with try/except for safety
```

## Examples
Input: "Extract product info: Apple MacBook Pro 2023, $2499, in stock"
```json
{
  "product": "MacBook Pro",
  "brand": "Apple",
  "year": 2023,
  "price": 2499.99,
  "currency": "USD",
  "in_stock": true
}
```

## Resources
- [JSON Schema](https://json-schema.org)

## Validation
1. Output is always valid JSON
2. All required keys are present
3. Values match specified types
4. JSON.parse() succeeds without errors"""
    },
    {
        "name": "few-shot-learning",
        "description": "Designs and curates few-shot examples to guide LLM behavior, including example selection, formatting, and ordering. Use for task specification without fine-tuning.",
        "tags": ["prompt", "few-shot", "examples", "in-context-learning", "llm"],
        "template": """# Few-Shot Learning

> Guiding LLM behavior through carefully curated examples.

## Quick Start
```
Classify the sentiment of each review:

Review: "This product is amazing!"
Sentiment: Positive

Review: "Terrible experience, would not recommend."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "Best purchase I've made all year!"
Sentiment:
```

## When to Use
- Teaching new tasks without fine-tuning
- Specifying output format by example
- Handling edge cases
- Setting response tone and style

## Best Practices

### Example Selection
- Cover edge cases and boundary conditions
- Include 3-5 diverse examples
- Show both positive and negative cases
- Order from simple to complex

### Formatting
- Use consistent separator between examples
- Clearly mark input vs output boundaries
- Keep format identical to expected real use

### Dynamic Selection
- For large datasets: retrieve most similar examples
- Use embedding similarity for example selection
- Limit to context window constraints

## Dependencies
```bash
pip install openai
# For dynamic selection: pip install sentence-transformers
```

## Examples
```
Translate English to French:

English: "Hello"
French: "Bonjour"

English: "Good morning"
French: "Bonjour"

English: "Thank you"
French: "Merci"

English: "How are you?"
French:
```

## Resources
- [OpenAI Few-Shot Guide](https://platform.openai.com/docs/guides/prompt-engineering)

## Validation
1. Model follows example patterns consistently
2. Edge cases handled correctly
3. Adding more examples improves accuracy
4. Format matches examples exactly"""
    },
    {
        "name": "system-prompt-design",
        "description": "Designs effective system prompts for LLM agents, chatbots, and assistants with role definition, constraints, and behavioral guidelines. Use for production AI systems.",
        "tags": ["prompt", "system-prompt", "agent", "chatbot", "persona"],
        "template": """# System Prompt Design

> Crafting system-level prompts for consistent agent behavior.

## Quick Start
```
You are a helpful coding assistant.
- Write clean, well-documented code
- Explain your reasoning briefly
- Provide working examples
- When unsure, say "I'm not sure"
- Never execute code without user approval
```

## When to Use
- Chatbot personality and tone
- Agent role and capability definition
- Safety and boundary constraints
- Multi-turn conversation consistency

## Components

### Role Definition
Who the AI is and what it does.

### Behavior Rules
Explicit do/don't guidelines.

### Output Format
Expected response structure.

### Constraints
Limitations and boundaries (time, scope, knowledge).

### Conversation Flow
How to handle greetings, follow-ups, clarifications.

## Dependencies
No additional libraries — pure prompt design.

## Examples
```
You are an expert SQL analyst.
- Write queries only, no explanations unless asked
- Use PostgreSQL syntax
- Add comments for complex JOINs
- If a query would be destructive, warn and ask for confirmation
- Reference table schemas when relevant
```

## Resources
- [Anthropic System Prompts](https://docs.anthropic.com/claude/docs/system-prompts)

## Validation
1. Agent follows rules consistently across sessions
2. Boundaries are respected (no prompt injection)
3. Response style matches defined persona
4. Multi-turn context is maintained correctly"""
    },
    {
        "name": "prompt-testing",
        "description": "Tests and evaluates prompt quality using systematic methods, A/B testing, regression suites, and automated evaluation with LLM-as-judge. Use for prompt optimization.",
        "tags": ["prompt", "testing", "evaluation", "llm-as-judge", "ab-testing"],
        "template": """# Prompt Testing

> Systematic evaluation and iteration of prompts.

## Quick Start
1. Define ground truth for 10-20 test cases
2. Run prompt against all cases
3. Score each response (correct/partial/incorrect)
4. Iterate prompt based on failure patterns
5. Re-run to measure improvement

## When to Use
- Before deploying prompts to production
- Comparing prompt variants (A/B testing)
- Regression testing prompt changes
- Evaluating model upgrades

## Methods

### Manual Evaluation
Human review of a sample of outputs against criteria.

### LLM-as-Judge
Use a strong model (Opus, GPT-4) to rate outputs.

### Test Suite
Maintain a set of inputs with expected outputs.

### A/B Testing
Compare two prompt versions on the same inputs.

## Dependencies
```bash
pip install pytest
```

## Examples
```
Evaluation Criteria:
1. Correctness (0-5): Is the answer factually correct?
2. Format (0-3): Does output follow specified format?
3. Completeness (0-3): Are all requested elements present?

Prompt: "Extract date, amount, and vendor from invoice text"
```

## Resources
- [Anthropic Eval Tools](https://docs.anthropic.com/claude/docs/evaluation-tools)

## Validation
1. Test suite covers all major input types
2. Score improves with each prompt iteration
3. Edge cases are documented and tested
4. Regression prevents previously fixed issues"""
    },
    {
        "name": "function-calling",
        "description": "Designs prompts and schemas for LLM function calling and tool use, enabling structured interactions with external APIs and services.",
        "tags": ["prompt", "function-calling", "tools", "api", "structured"],
        "template": """# Function Calling

> Prompt patterns for LLM tool use and external API integration.

## Quick Start
```
Available functions:
- get_weather(city: string, unit: "celsius"|"fahrenheit"): object
- get_timezone(city: string): string
- send_email(to: string, subject: string, body: string): boolean

Determine which function to call based on the user request.
Respond with: {"function": "name", "args": {...}}
```

## When to Use
- Building AI assistants with tool access
- API orchestration through LLM
- Database query generation
- Multi-step agent workflows

## Techniques

### Function Declaration
Describe each function with name, parameters, types and descriptions.

### Parameter Extraction
Guide the model to extract arguments from user input.

### Chaining
Chain multiple function calls for complex workflows.

### Error Recovery
Handle cases where arguments are missing or invalid.

## Dependencies
```python
# OpenAI-style function calling
response = client.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  tools=tool_definitions
)
```

## Examples
```json
{
  "name": "search_flights",
  "description": "Search for available flights",
  "parameters": {
    "origin": {"type": "string"},
    "destination": {"type": "string"},
    "date": {"type": "string", "format": "date"}
  }
}
```

## Resources
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use](https://docs.anthropic.com/claude/docs/tool-use)

## Validation
1. Correct function selected for each request
2. All required parameters are extracted
3. Invalid requests are handled gracefully
4. Multi-turn tool use maintains context"""
    },
    {
        "name": "rag-prompting",
        "description": "Designs prompts optimized for Retrieval-Augmented Generation systems, including context integration, citation handling, and hallucination reduction. Use for RAG applications.",
        "tags": ["prompt", "rag", "retrieval", "context", "citations"],
        "template": """# RAG Prompting

> Prompt strategies for retrieval-augmented generation systems.

## Quick Start
```
Answer based ONLY on the provided context.
If the answer is not in the context, say "I cannot answer from the available information."
Cite the source paragraph numbers in your answer.

Context:
[1] Climate change is caused by greenhouse gas emissions.
[2] Carbon dioxide levels have risen 50% since the Industrial Revolution.
[3] The Paris Agreement aims to limit warming to 1.5°C.

Question: What causes climate change?
Answer: Climate change is caused by greenhouse gas emissions [1].
```

## When to Use
- Document Q&A systems
- Knowledge base assistants
- Customer support chatbots
- Research paper analysis

## Techniques

### Context Window Management
Place most relevant documents at the top/bottom of context.

### Citation Format
Define clear citation style (brackets, source IDs, page numbers).

### Hallucination Guard
Explicitly instruct to only use provided context.

### Source Quality
Tag sources by reliability level in the prompt.

## Dependencies
```bash
pip install langchain openai chromadb
```

## Examples
```
You have access to the following product documentation.
Only answer using information from these documents.
If documents don't contain the answer, say so.

Documents:
<doc id="1">The API rate limit is 100 requests per minute.</doc>
<doc id="2">Authentication requires a Bearer token in the header.</doc>
```

## Resources
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering)

## Validation
1. Answers are grounded in retrieved context
2. Citations correctly reference sources
3. Model refuses to answer outside context
4. Multiple documents synthesized correctly"""
    },
    {
        "name": "prompt-compression",
        "description": "Reduces prompt token usage through compression techniques, summarization, and selective context inclusion while maintaining output quality. Use for cost optimization.",
        "tags": ["prompt", "compression", "tokens", "optimization", "cost"],
        "template": """# Prompt Compression

> Reduce token usage while preserving prompt effectiveness.

## Quick Start
```
Before (150 tokens):
"Please analyze the following customer feedback and provide
a detailed summary of the main complaints, positive points,
and suggestions for improvement. The feedback is from our
quarterly survey of 500 users across North America and Europe."

After (40 tokens):
"Analyze this customer feedback. Summarize complaints,
positive points, and improvement suggestions."
```

## When to Use
- Cost-sensitive production systems
- Long context window limits
- Batch processing with many requests
- Mobile or edge deployments

## Techniques

### Instruction Compression
Remove unnecessary words (please, could you, let's).

### Few-Shot Deduplication
Use one example per pattern type instead of multiple.

### Context Summarization
Pre-summarize retrieved documents before including.

### Selective Inclusion
Only include the most relevant context chunks.

### Abbreviation Mapping
Define short codes for repeated concepts.

## Dependencies
```bash
pip install llmlingua  # specialized prompt compression
```

## Examples
```
Instead of:
"For each of the following three customer reviews, classify
the sentiment as either positive, negative, or neutral.
Provide your reasoning for each classification."

Use:
"Classify sentiment (positive/negative/neutral) for each review.
Show reasoning."
Reduction: ~40% tokens
```

## Resources
- [LLMLingua Paper](https://arxiv.org/abs/2310.05736)
- [Anthropic Prompt Optimization](https://docs.anthropic.com/claude/docs/prompt-optimization)

## Validation
1. Output quality maintained after compression
2. Compression ratio measurable (>20% reduction)
3. Critical instructions not lost
4. Compare before/after on test suite"""
    },
]

base = '.claude/skills/ai'
for s in skills:
    path = f'{base}/{s["name"]}'
    os.makedirs(path, exist_ok=True)
    
    tags = '[' + ', '.join(s['tags']) + ']'
    
    content = f"""---
name: {s['name']}
description: {s['description']}
category: ai
tags: {tags}
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
{s['template']}
"""
    with open(f'{path}/SKILL.md', 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'  Created {path}/SKILL.md')

print(f'\nDone! Created {len(skills)} new prompt skills.')
