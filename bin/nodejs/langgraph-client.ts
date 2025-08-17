#!/usr/bin/env node

interface AssistantConfig {
  graph_id: string;
  name: string;
  default_config: {
    configurable: Record<string, any>;
  };
}

interface RunRequest {
  assistant_id: string;
  input: Record<string, any>;
  config: {
    configurable: Record<string, any>;
  };
}

class LangGraphClient {
  constructor(private baseUrl: string) {}

  async createAssistant(config: AssistantConfig): Promise<string> {
    const response = await fetch(`${this.baseUrl}/assistants`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(config),
    });

    if (!response.ok) {
      throw new Error(`Failed to create assistant: ${response.statusText}`);
    }

    const result = await response.json();
    return result.assistant_id;
  }

  async runAndWait(runRequest: RunRequest): Promise<any> {
    const response = await fetch(`${this.baseUrl}/runs/wait`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(runRequest),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`Request body was:`, JSON.stringify(runRequest, null, 2));
      console.error(`Error response:`, errorText);
      throw new Error(`Failed to run assistant: ${response.statusText} - ${errorText}`);
    }

    return await response.json();
  }
}

// CLI usage
if (import.meta.url === `file://${process.argv[1]}`) {
  const action = process.argv[2];
  const serverUrl = process.argv[3] || 'http://127.0.0.1:2024';
  
  if (!action) {
    console.error('Usage: langgraph-client.ts <create-assistant|run> <server-url> [research-topic]');
    process.exit(1);
  }

  const client = new LangGraphClient(serverUrl);

  if (action === 'create-assistant') {
    const config: AssistantConfig = {
      graph_id: "ollama_deep_researcher",
      name: "deep-research (LMStudio)",
      default_config: {
        configurable: {
          llm_provider: "lmstudio",
          lmstudio_base_url: "http://localhost:1234/v1",
          local_llm: "openai/gpt-oss-20b",
          search_api: "duckduckgo",
          fetch_full_page: true,
          max_web_research_loops: 2,
          use_tool_calling: true,
          strip_thinking_tokens: true
        }
      }
    };

    client.createAssistant(config)
      .then(assistantId => {
        console.log(assistantId);
      })
      .catch(error => {
        console.error('Error:', error.message);
        process.exit(1);
      });
  } else if (action === 'run') {
    const assistantId = process.argv[4];
    const researchTopic = process.argv[5];
    
    if (!assistantId || !researchTopic) {
      console.error('Usage: langgraph-client.ts run <server-url> <assistant-id> <research-topic>');
      process.exit(1);
    }

    const runRequest: RunRequest = {
      assistant_id: assistantId,
      input: {
        research_topic: researchTopic
      },
      config: {
        configurable: {
          llm_provider: "lmstudio",
          lmstudio_base_url: "http://localhost:1234/v1",
          local_llm: "openai/gpt-oss-20b",
          max_web_research_loops: 5,
          fetch_full_page: true,
          use_tool_calling: false
        }
      }
    };

    client.runAndWait(runRequest)
      .then(result => {
        console.log(JSON.stringify(result, null, 2));
      })
      .catch(error => {
        console.error('Error:', error.message);
        process.exit(1);
      });
  } else {
    console.error('Unknown action:', action);
    process.exit(1);
  }
}

export { LangGraphClient };