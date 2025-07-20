# GitHub Codespace Setup Guide

This guide will help you set up and use the TradingAgents project in a GitHub Codespace.

## Quick Start

1. **Open Codespace**: Click the "Code" button on GitHub and select "Create codespace on main"

2. **Wait for setup**: The codespace will automatically:
   - Set up Python 3.10 environment
   - Install VS Code extensions for Python development
   - Install project dependencies

3. **Configure API Keys**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

4. **Validate Setup**:
   ```bash
   python validate_codespace.py
   ```

## Required API Keys

### FinnHub API (Required)
- **Purpose**: Financial data (stocks, news, etc.)
- **Cost**: Free tier available
- **Setup**: 
  1. Go to [FinnHub.io](https://finnhub.io/)
  2. Sign up for a free account
  3. Get your API key from the dashboard
  4. Add to `.env`: `FINNHUB_API_KEY=your_key_here`

### OpenAI API (Required)
- **Purpose**: LLM agents for analysis and trading decisions
- **Cost**: Pay-per-use (recommend starting with gpt-4o-mini for testing)
- **Setup**:
  1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
  2. Create an API key
  3. Add to `.env`: `OPENAI_API_KEY=your_key_here`

### Optional APIs
- **Anthropic API**: For Claude models (`ANTHROPIC_API_KEY`)
- **Google API**: For Gemini models (`GOOGLE_API_KEY`)

## Testing Your Setup

### 1. Basic Validation
```bash
python validate_codespace.py
```

### 2. Test CLI
```bash
python -m cli.main analyze
```

### 3. Test Main Script
```bash
python main.py
```

## Development Features

### VS Code Extensions
The codespace includes:
- Python extension with IntelliSense
- Jupyter support for notebooks
- Code formatting with Black
- Linting with Pylint
- Debugging support

### Debug Configurations
Use F5 or the Debug panel to run:
- **Python: Current File**: Debug any Python file
- **TradingAgents: Main**: Debug the main.py script
- **TradingAgents: CLI**: Debug the CLI with analyze command

### Port Forwarding
Ports 8000 and 8501 are automatically forwarded for:
- Web interfaces (if using Chainlit or similar)
- Development servers

## Troubleshooting

### Common Issues

1. **Import errors**: Run `pip install -e .` to install the package in development mode
2. **API errors**: Ensure your API keys are correctly set in `.env`
3. **Python version**: The codespace uses Python 3.10+ as required

### Getting Help

- Check the main [README.md](README.md) for detailed documentation
- Run `python validate_codespace.py` to diagnose issues
- Ensure you're in the correct directory (`/workspaces/TradingAgents`)

## Cost Considerations

When using the APIs:
- **FinnHub**: Free tier provides 60 calls/minute
- **OpenAI**: Start with `gpt-4o-mini` for testing (much cheaper than `gpt-4`)
- Set the config to use cheaper models initially:
  ```python
  config["deep_think_llm"] = "gpt-4o-mini"
  config["quick_think_llm"] = "gpt-4o-mini"
  ```